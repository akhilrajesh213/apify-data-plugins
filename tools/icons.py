"""Fetches each plugin's icon (the endpoint Actor's Apify Store icon, full size) into
plugins/<name>/.claude-plugin/icon.png as a square 512 px PNG, which the Claude directory takes as the listing icon.

    python tools/icons.py
"""
import base64
import io
import json
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ACTORS = {
    "yahoo-finance-mcp": "yahoo-finance-scraper",
    "youtube-channels-mcp": "youtube-channel-scraper",
    "google-trends-mcp": "google-trends-scraper",
    "google-flights-mcp": "google-flights-mcp-server",
    "shopify-mcp": "shopify-mcp-server",
}


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "apify-data-plugins icon build"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def original(picture_url: str) -> str:
    # images.apifyusercontent.com/<sig>/<ops>/cb:1/<base64url of the S3 original>.webp
    tail = picture_url.rsplit("/", 1)[1].rsplit(".", 1)[0]
    return base64.urlsafe_b64decode(tail + "=" * (-len(tail) % 4)).decode()


def main() -> None:
    for plugin, actor in ACTORS.items():
        data = json.loads(get(f"https://api.apify.com/v2/acts/akhil_rajesh~{actor}"))["data"]
        src = original(data["pictureUrl"]) if "apifyusercontent" in data["pictureUrl"] else data["pictureUrl"]
        img = Image.open(io.BytesIO(get(src))).convert("RGBA")
        side = max(img.size)
        square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
        square.paste(img, ((side - img.width) // 2, (side - img.height) // 2))
        out = ROOT / "plugins" / plugin / ".claude-plugin" / "icon.png"
        square.resize((512, 512), Image.LANCZOS).save(out, "PNG", optimize=True)
        print(plugin, img.size, "->", out.stat().st_size, "bytes")


if __name__ == "__main__":
    main()

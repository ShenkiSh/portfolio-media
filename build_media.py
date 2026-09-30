"""Reassemble and verify the original portfolio recordings for GitHub Pages."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dist"


def safe_path(root: Path, value: str) -> Path:
    result = (root / value).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError("Manifest path must remain inside its root")
    return result


def main() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text())
    total = 0
    for entry in manifest["files"]:
        target = safe_path(OUT, entry["path"])
        target.parent.mkdir(parents=True, exist_ok=True)
        pending = target.with_suffix(".pending")
        digest = hashlib.sha256()
        size = 0
        with pending.open("wb") as output:
            for part in entry["parts"]:
                data = safe_path(ROOT, part["path"]).read_bytes()
                if len(data) != part["bytes"] or hashlib.sha256(data).hexdigest() != part["sha256"]:
                    raise ValueError(f"Corrupt part: {part['path']}")
                output.write(data)
                digest.update(data)
                size += len(data)
        if size != entry["bytes"] or digest.hexdigest() != entry["sha256"]:
            raise ValueError(f"Reassembled file does not match: {entry['path']}")
        pending.replace(target)
        total += size
        print(f"Verified {entry['path']}: {size} bytes")
    if total >= 1_000_000_000:
        raise ValueError("Media site exceeds the GitHub Pages size limit")
    (OUT / ".nojekyll").touch()
    (OUT / "index.html").write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Shani Shlomov — Portfolio media</title>'
        '<h1>Portfolio recordings</h1>'
        '<p>Original films for <a href="https://shenkish.github.io/">'
        'Shani Shlomov’s portfolio</a>.</p></html>'
    )
    print(f"Ready to publish: {total} media bytes")


if __name__ == "__main__":
    main()

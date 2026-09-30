# Shani Shlomov — portfolio recordings

Original full-length Hop! It's the Chef! and ReDream Labs recordings, served at
https://shenkish.github.io/portfolio-media/ for https://shenkish.github.io/.

The two recordings retain their exact original bytes, resolution, soundtrack and
length. Git stores 48 MiB parts because each original exceeds GitHub's per-file
limit. `manifest.json` records each part and complete file's SHA-256 and size.

Run `python3 build_media.py` to reconstruct and verify `dist/`. The manual
**Deploy portfolio media** Actions workflow publishes that directory to GitHub
Pages. Publish this repository before deploying the portfolio itself. Neither
repository's published site exceeds the GitHub Pages 1 GB limit.

The parts are storage artifacts and are not exposed in the published website.
The web players stream the reconstructed MP4 files and support seeking normally.

Copyright © 2026 Shani Shlomov. All rights reserved.

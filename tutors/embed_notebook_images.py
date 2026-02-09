#!/usr/bin/env python3
"""
Embed external image references in a Jupyter notebook as base64 data URLs.
Supports both markdown ![alt](path) and HTML <img src="path" ...> references.
Makes the notebook self-contained (no external image files needed).

Run `python3 embed_notebook_images --help` to see usage.
"""

import argparse
import base64
import json
import re
import shutil
import sys
from pathlib import Path


# MIME types for common image extensions
MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".svg": "image/svg+xml",
    ".webp": "image/webp",
}

# Markdown image: ![alt](path)
MARKDOWN_IMG_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

# HTML img src: <img ... src="path" ...> or src='path'
HTML_IMG_RE = re.compile(r'(<img\s+[^>]*src=)(["\'])([^"\']+)\2([^>]*>)')


def get_mime_type(path: Path) -> str | None:
    """Return MIME type for path, or None if unknown."""
    suffix = path.suffix.lower()
    return MIME_TYPES.get(suffix)


def embed_image(ref_path: str, nb_dir: Path) -> str | None:
    """
    Read image at ref_path (relative to nb_dir), return data URL or None.
    """
    if ref_path.strip().lower().startswith("data:"):
        return None  # already embedded

    # Resolve relative to notebook directory
    clean = ref_path.strip().lstrip("./")
    full_path = (nb_dir / clean).resolve()

    if not full_path.is_file():
        return None

    mime = get_mime_type(full_path)
    if not mime:
        return None

    try:
        data = full_path.read_bytes()
    except OSError:
        return None

    b64 = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{b64}"


def process_line(line: str, nb_dir: Path) -> str:
    """Replace image references in one line with base64 data URLs."""
    # Markdown images
    def md_repl(match):
        alt, path = match.group(1), match.group(2)
        data_url = embed_image(path, nb_dir)
        if data_url is None:
            return match.group(0)
        return f"![{alt}]({data_url})"

    line = MARKDOWN_IMG_RE.sub(md_repl, line)

    # HTML img src
    def html_repl(match):
        prefix, quote, path, suffix = match.group(1), match.group(2), match.group(3), match.group(4)
        data_url = embed_image(path, nb_dir)
        if data_url is None:
            return match.group(0)
        return f"{prefix}{quote}{data_url}{quote}{suffix}"

    line = HTML_IMG_RE.sub(html_repl, line)

    return line


def process_notebook(nb_path: Path, out_path: Path | None, in_place: bool) -> bool:
    """
    Load notebook, embed all images in markdown cells, save.
    Returns True on success.
    """
    nb_path = nb_path.resolve()
    nb_dir = nb_path.parent

    if not nb_path.is_file():
        print(f"Error: not a file: {nb_path}", file=sys.stderr)
        return False

    try:
        raw = nb_path.read_text(encoding="utf-8")
        nb = json.loads(raw)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Error reading notebook: {e}", file=sys.stderr)
        return False

    if "cells" not in nb:
        print("Error: no 'cells' in notebook", file=sys.stderr)
        return False

    modified = 0
    for cell in nb["cells"]:
        if cell.get("cell_type") != "markdown":
            continue
        source = cell.get("source")
        if not source:
            continue
        if isinstance(source, str):
            source = [source]
        new_source = []
        for part in source:
            new_part = process_line(part, nb_dir)
            if new_part != part:
                modified += 1
            new_source.append(new_part)
        cell["source"] = new_source

    if out_path is None:
        out_path = nb_path if in_place else nb_path.parent / f"{nb_path.stem}-embedded{nb_path.suffix}"

    out_path = out_path.resolve()
    if in_place and out_path == nb_path:
        backup = nb_path.with_suffix(nb_path.suffix + ".bak")
        shutil.copy2(nb_path, backup)
        print(f"Backup written to {backup}")

    try:
        out_path.write_text(
            json.dumps(nb, indent=1, ensure_ascii=False),
            encoding="utf-8",
        )
    except OSError as e:
        print(f"Error writing notebook: {e}", file=sys.stderr)
        return False

    print(f"Wrote {out_path} ({modified} line(s) updated)")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Embed image files in a Jupyter notebook as base64 (self-contained notebook)."
    )
    parser.add_argument(
        "notebook",
        type=Path,
        help="Path to the .ipynb notebook",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="Output path (default: <name>-embedded.ipynb, or same file with --in-place)",
    )
    parser.add_argument(
        "-i", "--in-place",
        action="store_true",
        help="Overwrite the notebook in place (creates a .bak backup)",
    )
    args = parser.parse_args()

    ok = process_notebook(args.notebook, args.output, args.in_place)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
scripts/generate_references.py
Automatically scans Markdown files in docs/development/ (excluding references.md),
extracts HTTPS URLs, deduplicates them, groups them by source file, and outputs
docs/development/references.md.
"""

import os
import re
from pathlib import Path

DEVELOPMENT_DIR = Path("docs/development")
OUTPUT_FILE = DEVELOPMENT_DIR / "references.md"
URL_REGEX = re.compile(r'https://[^\s\)\]>"\']+')

def clean_url(url: str) -> str:
    return url.rstrip(".,;:)")

def get_page_title(file_path: Path) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
    except Exception:
        pass
    return file_path.stem.replace("-", " ").replace("_", " ").title()

def main():
    if not DEVELOPMENT_DIR.exists():
        print(f"Error: {DEVELOPMENT_DIR} does not exist.")
        return

    file_references = {}

    for path in sorted(DEVELOPMENT_DIR.rglob("*.md")):
        if path.resolve() == OUTPUT_FILE.resolve():
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Warning: Could not read {path}: {e}")
            continue

        matches = URL_REGEX.findall(content)
        cleaned_urls = set()
        for u in matches:
            cleaned = clean_url(u)
            if cleaned:
                cleaned_urls.add(cleaned)

        if cleaned_urls:
            rel_path = path.relative_to(DEVELOPMENT_DIR)
            page_title = get_page_title(path)
            file_references[rel_path] = {
                "title": page_title,
                "urls": sorted(list(cleaned_urls))
            }

    lines = [
        "# External References",
        "",
        "> [!NOTE]",
        "> This page is **automatically generated** by `scripts/generate_references.py`.",
        "> Do not edit this page manually. Any manual edits will be overwritten during site build.",
        "",
        "This page collects external HTTPS resources and documentation links referenced across the **Development** documentation.",
        ""
    ]

    if not file_references:
        lines.append("*No external references found in the Development section yet.*")
    else:
        grouped = {}
        for rel_path, data in file_references.items():
            parts = rel_path.parts
            if len(parts) > 1:
                section_name = parts[0].replace("-", " ").replace("_", " ").title()
            else:
                section_name = "General Development"
            grouped.setdefault(section_name, []).append((rel_path, data))

        for section, items in sorted(grouped.items()):
            lines.append(f"## {section}")
            lines.append("")
            for rel_path, data in items:
                lines.append(f"### {data['title']}")
                lines.append(f"*Source: `docs/development/{rel_path.as_posix()}`*")
                lines.append("")
                for url in data["urls"]:
                    lines.append(f"- [{url}]({url})")
                lines.append("")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Successfully generated references at {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

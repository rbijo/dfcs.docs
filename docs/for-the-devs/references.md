# Reference Extraction Automation

External links inside `docs/development/` are automatically parsed and grouped.

## How it Works
The Python script `scripts/generate_references.py`:
1. Scans all `.md` files in `docs/development/`.
2. Explicitly skips `docs/development/references.md` to prevent infinite generation loops.
3. Extracts all `https://` URLs using regular expressions.
4. Clean and deduplicate links.
5. Writes formatted output to `docs/development/references.md`.

## Running Manually
```bash
python scripts/generate_references.py
```
This script runs automatically during the GitHub Actions build pipeline.

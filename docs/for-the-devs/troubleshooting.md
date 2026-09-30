# Troubleshooting

Solutions to common authoring or build issues.

## Common Issues & Fixes

### 1. `zensical build` Fails with Strict Mode Warning
- **Cause:** Missing page referenced in `zensical.toml` or broken internal Markdown link.
- **Fix:** Check line numbers reported in build terminal and ensure file exists.

### 2. References Page Not Updating
- **Cause:** Script forgot to run before building.
- **Fix:** Run `python scripts/generate_references.py` manually.

### 3. Icon Not Displaying
- **Cause:** Invalid icon identifier in `zensical.toml`.
- **Fix:** Verify standard icon paths (e.g., `fontawesome/solid/code` or `material/table`).

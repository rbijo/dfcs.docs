# Testing & Validation

Always validate the build locally before pushing to `main`.

## Validation Steps
1. **Regenerate References:**
   ```bash
   python scripts/generate_references.py
   ```

2. **Run Strict Build:**
   ```bash
   zensical build --strict
   ```
   If warnings or broken link errors occur, resolve them immediately.

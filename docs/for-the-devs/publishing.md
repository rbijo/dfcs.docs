# Publishing to GitHub Pages

The website is continuously deployed to GitHub Pages via GitHub Actions.

## Pipeline Trigger
Every push to the `main` branch triggers `.github/workflows/docs.yml`.

## Pipeline Execution Steps
1. Checkout repository branch.
2. Install Python & Zensical.
3. Execute `python scripts/generate_references.py`.
4. Run `zensical build --strict`.
5. Deploy `site/` artifact to GitHub Pages.

Live URL: [https://rbijo.github.io/dfcs.docs/](https://rbijo.github.io/dfcs.docs/)

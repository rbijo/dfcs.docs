# Change Log

This changelog tracks updates, features, theme adjustments, and automation changes for the **Documentation Website**.

> [!NOTE]
> This changelog records changes to the documentation site framework itself (navigation, automation, deployment, styling). It does not track research or model development progress.

---

## 2026-09-30

### feat
- Initialized production-ready Zensical documentation framework.
- Designed editorial technical project landing page with architecture diagrams, Shields.io badge system, and project direction.
- Created complete navigation hierarchy for **Development** (Dataset Build, Fine Tuning, Website, References) and **For the Devs**.
- Configured semantic icons for all top-level and sidebar navigation entries.
- Added automated external reference extraction via `scripts/generate_references.py`.

### ci
- Created GitHub Actions workflow `.github/workflows/docs.yml` for automated testing, reference generation, strict building, and GitHub Pages deployment.

### docs
- Built comprehensive developer guide under **For the Devs** covering local preview, navigation, icon rules, badges, diagrams, studio usage, git workflow, and deployment troubleshooting.

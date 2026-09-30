# Project Structure

Overview of file layout in `dfcs.docs`:

```
.
├── zensical.toml                 # Main Zensical configuration
├── README.md                     # Repository quickstart guide
├── docs/                         # Markdown documentation root
│   ├── index.md                  # Landing page
│   ├── development/              # Research & dev workspace
│   │   ├── dataset-build/        # Dataset collection & cleaning docs
│   │   ├── fine-tuning/          # Model selection & training docs
│   │   ├── website/              # Web app & backend API docs
│   │   └── references.md         # Auto-extracted HTTPS references
│   └── for-the-devs/             # Documentation maintainer guides
│       └── changelog.md          # Website changelog (FIRST PAGE)
├── scripts/
│   └── generate_references.py    # Reference extraction script
└── .github/
    └── workflows/
        └── docs.yml              # GitHub Pages deployment pipeline
```

# Navigation & Icons

Navigation is declared in `zensical.toml` under `[project.nav]`.

## Icon Syntax Rules
In `zensical.toml`, icons are specified using standard Material icon identifiers:

```toml
[[project.nav]]
name = "Home"
url = "index.md"
icon = "fontawesome/solid/house"
```

## Adding a New Page
1. Create your `.md` file under `docs/`.
2. Open `zensical.toml`.
3. Add an entry under the appropriate section in `[[project.nav]]`.
4. Assign a semantically matching icon.

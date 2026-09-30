# Building the Site

How to trigger a clean production build of the static site.

## Build Command
```bash
zensical build
```

## Production Output
The compiled static assets (HTML, CSS, JS, images, search index) are written to the `site/` folder.

> [!NOTE]
> Do NOT commit the `site/` directory to Git. It is automatically generated during CI/CD.

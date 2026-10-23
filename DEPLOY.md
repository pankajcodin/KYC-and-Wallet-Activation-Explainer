# Deploying

The site is plain static files. There is no build step for the page itself.

## Vercel

1. Push this folder to the GitHub repo, with `index.html` at the root.
2. In Vercel, import the repo. Framework preset: Other. Build command: leave empty. Output directory: leave empty (the root).
3. Deploy. Every push to `main` redeploys.

## Before each push

```
python3 scripts/build.py     # rebuilds GUIDE.md, SOURCES.md, pin.txt from index.html
python3 scripts/check.py     # dashes, emoji, source ids, pin matches the guide
python3 scripts/make_pdf.py  # rebuilds the PDF (needs playwright and Chromium)
```

Edit `index.html` only. The other three files are generated from it.

## After deploying

- Open the site and check that the fonts and both logos load (no 404 in the browser's Network tab).
- Open the Part A image link and the PDF link.
- Re-open the official links in the Sources section and update "Last verified" in `index.html`, then run the three commands above.

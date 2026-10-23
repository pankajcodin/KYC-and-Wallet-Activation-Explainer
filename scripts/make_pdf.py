"""Builds KYC-and-Wallet-Activation-Explainer.pdf from index.html. Needs: pip install playwright, then playwright install chromium."""
import pathlib
from playwright.sync_api import sync_playwright
root = pathlib.Path(__file__).resolve().parent.parent
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto((root / "index.html").as_uri())
    pg.wait_for_timeout(800)
    pg.pdf(path=str(root / "KYC-and-Wallet-Activation-Explainer.pdf"), format="A4", print_background=True,
           margin={"top": "14mm", "bottom": "14mm", "left": "10mm", "right": "10mm"})
    b.close()
print("built PDF")

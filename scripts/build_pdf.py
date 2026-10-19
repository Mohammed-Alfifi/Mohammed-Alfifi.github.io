"""Render the portfolio pages to PDF using their print styles."""
import pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = [
    ("index.html", "Portfolio-Mohammed_Alfaifi.pdf"),
    ("ar.html", "Portfolio-Mohammed_Alfaifi-AR.pdf"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for page_file, out in PAGES:
        ctx = browser.new_context(color_scheme="light")
        page = ctx.new_page()
        page.goto((ROOT / page_file).as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(800)
        page.pdf(path=str(ROOT / out), format="A4", print_background=True, prefer_css_page_size=True)
        ctx.close()
        print("built", out)
    browser.close()

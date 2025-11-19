#!/usr/bin/env python3

import asyncio
import sys
from pathlib import Path

def check_playwright():
    try:
        import playwright
        return True
    except ImportError:
        return False

async def convert_html_to_pdf():
    if not check_playwright():
        print("Error: Playwright not found")
        print("Run: ./generate_pdf.sh")
        sys.exit(1)
    
    from playwright.async_api import async_playwright
    
    script_dir = Path(__file__).parent.absolute()
    html_file = script_dir / "index.html"
    pdf_file = script_dir / "Koorosh_Komeili_Zadeh_CV.pdf"
    
    if not html_file.exists():
        print(f"Error: HTML file not found at {html_file}")
        sys.exit(1)
    
    print(f"Converting {html_file} to PDF...")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        await page.goto(f"file://{html_file.absolute()}")
        await page.wait_for_load_state('networkidle')
        await page.wait_for_timeout(2000)
        await page.set_viewport_size({"width": 794, "height": 1123})
        
        await page.pdf(
            path=str(pdf_file),
            format='A4',
            margin={
                'top': '5mm',
                'bottom': '5mm',
                'left': '5mm',
                'right': '5mm'
            },
            print_background=True,
            prefer_css_page_size=False,
            display_header_footer=False,
            scale=1.0
        )
        
        await browser.close()
    
    print(f"PDF created: {pdf_file}")

def main():
    try:
        asyncio.run(convert_html_to_pdf())
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
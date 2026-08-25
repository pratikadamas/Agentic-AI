from playwright.async_api import async_playwright
import asyncio
from pathlib import Path
from datetime import datetime
import os

# ============================================
# CONFIGURATION - Edit your URLs here
# ============================================
URLS = [
  "https://chatgpt.com/share/6a552949-60a8-83e9-8c29-60698becce9f",
  "https://chatgpt.com/share/6a55296b-ab38-83e8-99e7-13c389abfc02",
  "https://chatgpt.com/share/6a5529a7-a184-83e8-a4bc-35acd9b54b9c",
  "https://chatgpt.com/share/6a5529e2-b754-83ee-ac67-dad95de43c97",
  "https://chatgpt.com/share/6a552cc6-5264-83ee-bca4-b1055537b367",
  "https://chatgpt.com/share/6a552d2a-eb84-83e8-b09a-228dc9ef00ef",
  "https://chatgpt.com/share/6a552d92-89cc-83e8-a631-8f34bbbf6fb4",
  "https://chatgpt.com/share/6a552dbf-b454-83ee-8661-62cbdc2f1a52",
  "https://chatgpt.com/share/6a552de7-5e48-83ee-b01c-cbd8ae67b840",
  "https://chatgpt.com/share/6a552e1e-d1b8-83ee-83f4-6e95f1a157a0",
  "https://chatgpt.com/share/6a55c392-5f90-83e8-b3cc-42fc8825ea4d",
  "https://chatgpt.com/share/6a55c40a-86a0-83ee-8b65-715b8729c5db",
  "https://chatgpt.com/share/6a55c439-fdc0-83ee-991f-f27f938c4985",
  "https://chatgpt.com/share/6a55c4b3-10b8-83ee-a0ea-943db3fe568a",
  "https://chatgpt.com/share/6a55c564-1ba0-83e8-b286-9a4b7e8e8f28",
  "https://chatgpt.com/share/6a55c5af-5050-83ee-83c8-ea9067cbcdc1",
  "https://chatgpt.com/share/6a55c727-5830-83ee-a1c7-710d45155903",
  "https://chatgpt.com/share/6a55c85f-4d70-83e8-b2ab-bd3e9df93c39",
  "https://chatgpt.com/share/6a552147-1850-83ee-a8b3-faec16a83aff",
  "https://chatgpt.com/share/6a55caf4-fa90-83ee-a5ad-052702ecb906",
  "https://chatgpt.com/share/6a55cc2d-bb38-83e8-b8c8-496c3a3eaf0e",
  "https://chatgpt.com/share/6a55f398-54d8-83ee-8a80-31b6c99d0cfa",
  "https://chatgpt.com/share/6a565cb8-0b5c-83e8-b84f-77c0cdfdf7e6",
  "https://chatgpt.com/share/6a565d8d-008c-83ee-9d65-6d062ad295c8",
  "https://chatgpt.com/share/6a5522c8-22f8-83e8-96c0-6a3132bd6447",
  "https://chatgpt.com/share/6a565fb0-24f0-83ee-a004-a8bc2c90b1f7",
  "https://chatgpt.com/share/6a566247-0270-83ee-b77f-9f34f1b4a7a0",
  "https://chatgpt.com/share/6a566282-0558-83e8-bfb2-a5a118befe7d",
  "https://chatgpt.com/share/6a56658e-02ec-83e8-92e9-c4933243ded9",
  "https://chatgpt.com/share/6a56664d-13d8-83ee-a546-5adb044a312a",
  "https://chatgpt.com/share/6a566686-068c-83e8-8c9e-4a8f648c0e7d",
  "https://chatgpt.com/share/6a5668f8-7eac-83ee-9162-f56438be2b21",
  "https://chatgpt.com/share/6a56693f-7d74-83ee-8602-436d2d02e20a",
  "https://chatgpt.com/share/6a566eca-7d64-83ee-a071-cb4452de9630",
  "https://chatgpt.com/share/6a566f0c-8fc8-83ee-b296-7787bfc276b1",
  "https://chatgpt.com/share/6a566f34-6edc-83e8-9cd5-86f95c3d3462",
  "https://chatgpt.com/share/6a5670bd-e7c0-83e8-a486-ac009242b865",
  "https://chatgpt.com/share/6a567132-b10c-83e8-a4ab-17dcd8e3e37b",
  "https://chatgpt.com/share/6a56717e-3184-83ee-8c4a-b6cdccdd2a88",
  "https://chatgpt.com/share/6a5671e5-d994-83ee-8dcd-17702c3fb331",
  "https://chatgpt.com/share/6a5672e9-7aa4-83e8-b488-da2d3e3f4e63",
  "https://chatgpt.com/share/6a577c11-874c-83e8-a951-1445bf3daff9",
  "https://chatgpt.com/share/6a577c81-bd24-83ee-a3fc-c2c178087763",
  "https://chatgpt.com/share/6a577ceb-1b74-83ee-b2cc-4101ec02e897",
  "https://chatgpt.com/share/6a577d06-e3f8-83ee-92e5-5cc5e5f46286",
  "https://chatgpt.com/share/6a577d69-b370-83e8-8ce0-c22cc01a9718",
  "https://chatgpt.com/share/6a578c52-e684-83ee-878e-5046eb81ce4b",
  "https://chatgpt.com/share/6a578d00-18e4-83ee-b16e-a77894d8f114",
  "https://chatgpt.com/share/6a578ecc-89b4-83e8-ae87-ecf54e61a8db",
  "https://chatgpt.com/share/6a5798b8-c4e4-83ee-818e-c7e7252f61f3",
  "https://chatgpt.com/share/6a579930-77f0-83ee-88c3-601a93e108ba",
  "https://chatgpt.com/share/6a5799aa-0e98-83ee-81a1-142ca1cbeee8",
  "https://chatgpt.com/share/6a5799e0-a4e8-83e8-a216-27809e96f293",
  "https://chatgpt.com/share/6a579a17-de24-83ee-895d-fdc2bde22cfc",
  "https://chatgpt.com/share/6a579a4e-ecbc-83e8-b70c-cc029b0ed150",
  "https://chatgpt.com/share/6a566eca-7d64-83ee-a071-cb4452de9630",
  "https://chatgpt.com/share/6a566f0c-8fc8-83ee-b296-7787bfc276b1",
  "https://chatgpt.com/share/6a566f34-6edc-83e8-9cd5-86f95c3d3462",
  "https://chatgpt.com/share/6a5670bd-e7c0-83e8-a486-ac009242b865",
  "https://chatgpt.com/share/6a567132-b10c-83e8-a4ab-17dcd8e3e37b",
  "https://chatgpt.com/share/6a567a38-3524-83ee-b415-684e109f9322",
  "https://chatgpt.com/share/6a567b8e-c240-83e8-8239-b2eb837822ca",
  "https://chatgpt.com/share/6a567bf1-11ec-83ee-89fc-a697eb9be68a",
]

OUTPUT_FOLDER = "pdfs"


# ============================================
# HELPER FUNCTIONS
# ============================================

def extract_chat_id(url: str) -> str:
    """Extract chat ID from ChatGPT share URL."""
    parts = url.rstrip("/").split("/")
    for part in parts:
        if len(part) > 10 and "-" in part:
            return part
    return parts[-1] if parts else "chat"


async def scroll_full_page(page):
    """Scroll to load all lazy content."""
    await page.evaluate("""
        async () => {
            const delay = ms => new Promise(r => setTimeout(r, ms));
            for (let i = 0; i < 10; i++) {
                window.scrollTo(0, document.body.scrollHeight);
                await delay(400);
            }
            window.scrollTo(0, 0);
            await delay(300);
        }
    """)
    await asyncio.sleep(1)


async def convert_chat_to_pdf(page, url: str, folder: Path) -> str:
    """Convert one ChatGPT share URL to PDF."""
    chat_id = extract_chat_id(url)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_path = folder / f"{chat_id}_{timestamp}.pdf"
    
    print(f"  → Loading page...")
    
    await page.goto(url, timeout=90000, wait_until="domcontentloaded")
    
    try:
        await page.wait_for_load_state("networkidle", timeout=30000)
    except:
        pass
    
    # Wait for ChatGPT messages to appear
    try:
        await page.wait_for_selector('[data-message-author-role]', timeout=30000)
    except:
        print("    ⚠️  Message selector not found, waiting longer...")
        await asyncio.sleep(5)
    
    await scroll_full_page(page)
    await asyncio.sleep(3)  # Extra render time
    
    await page.pdf(
        path=str(pdf_path),
        format="A4",
        print_background=True,
        display_header_footer=True,
        header_template='<div style="font-size:8px; margin-left:20px; padding-top:5px;">ChatGPT Export</div>',
        footer_template='<div style="font-size:8px; margin:0 auto; width:100%; text-align:center;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
        margin={"top": "50px", "right": "30px", "bottom": "50px", "left": "30px"}
    )
    
    return str(pdf_path)


async def chats_to_pdf(urls: list[str], output_folder: str = OUTPUT_FOLDER) -> list[str]:
    """Convert list of ChatGPT share URLs to PDFs."""
    folder = Path(output_folder)
    folder.mkdir(parents=True, exist_ok=True)
    
    saved = []
    failed = []
    
    print("=" * 55)
    print("ChatGPT → PDF Converter")
    print(f"Output: {folder.absolute()}")
    print(f"URLs:   {len(urls)}")
    print("=" * 55 + "\n")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ]
        )
        
        context = await browser.new_context(
            viewport={"width": 1280, "height": 2000},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        
        page = await context.new_page()
        
        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}] {url}")
            try:
                pdf_path = await convert_chat_to_pdf(page, url, folder)
                size_kb = os.path.getsize(pdf_path) / 1024
                print(f"    ✅ {Path(pdf_path).name} ({size_kb:.1f} KB)\n")
                saved.append(pdf_path)
            except Exception as e:
                print(f"    ❌ Error: {e}\n")
                failed.append((url, str(e)))
        
        await browser.close()
    
    print("=" * 55)
    print(f"Done! {len(saved)}/{len(urls)} saved to ./{output_folder}/")
    if failed:
        print(f"Failed ({len(failed)}):")
        for url, err in failed:
            print(f"  • {url}: {err}")
    print("=" * 55)
    
    return saved


# ============================================
# MAIN ENTRY POINT - This runs the converter
# ============================================
if __name__ == "__main__":
    urls = [u.strip() for u in URLS if u.strip() and not u.strip().startswith("#")]
    
    if not urls:
        print("ERROR: No valid URLs found. Add ChatGPT share links to the URLS list.")
    else:
        asyncio.run(chats_to_pdf(urls))
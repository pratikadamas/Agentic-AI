from playwright.async_api import async_playwright
import asyncio
from pathlib import Path
from datetime import datetime
import os

# ============================================
# CONFIGURATION - Edit your URLs here
# ============================================
URLS = [
    # "https://chatgpt.com/share/6a4f3a1b-b190-83ee-a70b-5ea8dd533286",
    # "https://chatgpt.com/share/6a4f3ab0-e464-83e8-b95e-ed371d6af5cc",
    # "https://chatgpt.com/share/6a4f3cf5-0ae8-83ee-9a10-d2e7693ebb72",
    # "https://chatgpt.com/share/6a4f3dff-0804-83ee-8df2-569f302edc76",
    # "https://chatgpt.com/share/6a4f3e4c-6750-83ee-8a7f-8c8e2f01670e",
    # "https://chatgpt.com/share/6a4f3e96-c840-83ee-9d8f-0fcf8b42adb6",

    # "https://chatgpt.com/share/6a4f4005-70a8-83ee-9639-e6ff9e8ee8b6",
    # "https://chatgpt.com/share/6a4f405c-29fc-83ee-88c2-822f7e72fdd8",
    # "https://chatgpt.com/share/6a4f4093-37cc-83e8-86cc-2e67fd19f85d",
    # "https://chatgpt.com/share/6a4f4173-19d0-83ee-8927-205205906118",
    # "https://chatgpt.com/share/6a4f41b1-1980-83e8-9ec4-2ced476fbcdf",
    # "https://chatgpt.com/share/6a4f470c-e6e8-83e8-be7c-f30e0acffb7e",
    # "https://chatgpt.com/share/6a4f4759-5448-83ee-8d93-6224feb337de",
    # "https://chatgpt.com/share/6a4f4813-3404-83ee-893e-c8da0b045e84",
    # "https://chatgpt.com/share/6a4f48af-90ac-83ee-82b8-0a0436baba09",
    # "https://chatgpt.com/share/6a4f499b-1d00-83ee-b225-8b0548ded174",
    # "https://chatgpt.com/share/6a4f49d8-f514-83ee-98b8-ee5997898065",
    # "https://chatgpt.com/share/6a4f4a1b-015c-83e8-98af-25e5aabfa38f",
    # "https://chatgpt.com/share/6a4f4a4c-52c0-83e8-8cb7-98d342d8f364",
    # "https://chatgpt.com/share/6a4f4b1d-cd30-83e8-a3a7-5b8acaffeb34",
    # "https://chatgpt.com/share/6a4f4b57-42e8-83ee-b678-980e2e3b39e7",
    # "https://chatgpt.com/share/6a4f4e03-66f0-83ee-88f9-67d72c11abfc",
    # "https://chatgpt.com/share/6a4f4e59-ab14-83ee-b96e-074e53f4615a",
    # "https://chatgpt.com/share/6a4f4f6c-c124-83ee-8f3d-8fa78df0cda8",
    # "https://chatgpt.com/share/6a4f4fb5-f70c-83ee-a834-74b58faefa1d",
    # "https://chatgpt.com/share/6a4f50e0-098c-83ee-8c27-afaee54a28d7",
    # "https://chatgpt.com/share/6a4f5200-bbd4-83ee-98d4-c80b9cbabfdb",
    # "https://chatgpt.com/share/6a4f523b-7314-83ee-83ac-0fa9bf3d9b56",
    # "https://chatgpt.com/share/6a4f526c-8968-83ee-bc50-115a6f33e195",
    # "https://chatgpt.com/share/6a4f5321-7160-83ee-8547-78f4051f2edc",
    # "https://chatgpt.com/share/6a4f5384-51c8-83e8-94ea-52c34e717dc1",
    # "https://chatgpt.com/share/6a4f5566-3944-83ee-a46c-7808b97661a1",
    # "https://chatgpt.com/share/6a4f5657-dd24-83ee-aeb6-a45286c79c32",
    # "https://chatgpt.com/share/6a4f588e-9434-83ee-ad5c-df776b6e7a08",
    # "https://chatgpt.com/share/6a4f58ca-bff4-83e8-80d7-f2acb372ed1e",
    # "https://chatgpt.com/share/6a4f590b-3c18-83e9-ab2c-85e8a9269cec",
    # "https://chatgpt.com/share/6a4f595b-4218-83ee-90f9-17f45ad87d64",
    # "https://chatgpt.com/share/6a4f5a54-410c-83e9-ba88-c782acc44c69",
    # "https://chatgpt.com/share/6a4f5a86-1734-83ee-9094-02e67d8fb628",
    # "https://chatgpt.com/share/6a4f5b08-41ec-83e8-b5a1-f83f9c064bac",
    # "https://chatgpt.com/share/6a4f5b98-86b4-83ee-801c-461ed39cbcd9",
    # "https://chatgpt.com/share/6a4f5c13-8b50-83ee-b626-2cc798a2097b",
    # "https://chatgpt.com/share/6a4f5c4e-1a58-83e8-af55-8daf83a58bf5",
    # "https://chatgpt.com/share/6a4f5cb0-b0b8-83ee-b806-33b079f815e9",
    # "https://chatgpt.com/share/6a4f5cd6-29c8-83ee-b0b7-050d91ca9a5a",
    # "https://chatgpt.com/share/6a4f5d26-9000-83ee-a0bb-0e4b0e4ca102",
    # "https://chatgpt.com/share/6a4f5d5e-9dcc-83ee-9aae-05cf9f5775ec"
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
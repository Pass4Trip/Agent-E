from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
import time

def run_recorded_actions():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Recording started at: 2024-11-22 22:45:40

        try:
            # Actions will be recorded here
            try:
                page.goto('https://www.google.com')
                time.sleep(0.5)  # Small delay between actions
            except Exception as e:

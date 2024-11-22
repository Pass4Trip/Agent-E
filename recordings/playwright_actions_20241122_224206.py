from playwright.sync_api import sync_playwright

def run_recorded_actions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Recording started at: 2024-11-22 22:42:06

        page.goto('https://www.google.com')

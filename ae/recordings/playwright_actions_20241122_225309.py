from playwright.sync_api import sync_playwright
import time

def run_recorded_actions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Recording started at: 2024-11-22 22:53:09

        page.goto('https://www.google.com')
        time.sleep(0.5)  # Small delay between actions

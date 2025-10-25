from playwright.sync_api import sync_playwright
import sys

URL = "http://localhost:8501"

def main():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(URL, timeout=30000)
            # wait for body to be present
            page.wait_for_selector("body", timeout=10000)
            content = page.content()
            if "Proyek Analisis Data" in content:
                print("UI test passed: app title found")
                browser.close()
                return 0
            else:
                print("UI test failed: expected text not found")
                print(content[:1000])
                browser.close()
                return 2
    except Exception as e:
        print(f"UI test failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())

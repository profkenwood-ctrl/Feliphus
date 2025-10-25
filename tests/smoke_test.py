import urllib.request
import sys

URL = "http://localhost:8501"
EXPECTED_TEXT = "Proyek Analisis Data"


def main():
    try:
        with urllib.request.urlopen(URL, timeout=10) as resp:
            code = resp.getcode()
            body = resp.read().decode("utf-8", errors="ignore")
            print(f"HTTP status: {code}")
            if code != 200:
                print("Smoke test failed: non-200 status")
                return 2

            if EXPECTED_TEXT in body:
                print("Smoke test passed: expected text found")
                return 0
            # Streamlit renders much of the app client-side; if EXPECTED_TEXT isn't present
            # the initial HTML will still contain static assets. Accept that as a weaker
            # success condition so CI can validate the app is up without executing JS.
            if "static" in body or "streamlit" in body.lower():
                print("Smoke test passed (fallback): server returned HTML with static assets")
                return 0
            else:
                print("Smoke test failed: expected text not found in HTML and no static assets detected")
                print(body[:1000])
                return 3

    except Exception as e:
        print(f"Smoke test failed: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())

import urllib.request
import sys

URL = "http://localhost:8501"

def main():
    try:
        with urllib.request.urlopen(URL, timeout=10) as resp:
            code = resp.getcode()
            print(f"HTTP status: {code}")
            if code == 200:
                print("Smoke test passed")
                return 0
            else:
                print("Smoke test failed: non-200 status")
                return 2
    except Exception as e:
        print(f"Smoke test failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())

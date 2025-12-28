import time

import requests

URL = "http://localhost:36879/"

while True:
    try:
        r = requests.get(URL, timeout=3)
        print(f"Status: {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5)

import requests
def get_culture_meaning(keyword):
    try:
        r = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{keyword}")
        if r.status_code == 200:
            return r.json().get("extract", "No cultural interpretation found.")
    except Exception:
        pass
    return "No cultural data available."

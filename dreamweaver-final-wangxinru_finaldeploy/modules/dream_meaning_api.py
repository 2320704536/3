import requests, streamlit as st
def get_dream_meaning(keyword):
    key = st.secrets.get("ninjas_key", None)
    if not key:
        return "Please set your API Ninjas key in secrets."
    try:
        r = requests.get(f"https://api.api-ninjas.com/v1/dream?word={keyword}", headers={"X-Api-Key": key}, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if data:
                return data[0].get("interpretation", "No dream meaning found.")
    except Exception:
        pass
    return "No dream meaning available."

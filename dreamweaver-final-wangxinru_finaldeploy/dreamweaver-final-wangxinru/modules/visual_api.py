import requests, streamlit as st
def get_visual(keyword):
    key = st.secrets.get("unsplash_key", None)
    if not key:
        return "https://source.unsplash.com/800x600/?dream"
    try:
        r = requests.get(f"https://api.unsplash.com/photos/random?query={keyword}&client_id={key}")
        if r.status_code == 200:
            data = r.json()
            return data['urls']['regular']
    except Exception:
        pass
    return "https://source.unsplash.com/800x600/?dream"

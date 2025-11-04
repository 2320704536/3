import requests, streamlit as st
def get_sound(keyword):
    key = st.secrets.get("pixabay_key", None)
    if not key:
        return "https://cdn.pixabay.com/download/audio/2022/03/15/audio_b9b733d85f.mp3?filename=dreamy-ambient-110857.mp3"
    try:
        r = requests.get(f"https://pixabay.com/api/audio/?key={key}&q={keyword}")
        if r.status_code == 200:
            data = r.json()
            if data["hits"]:
                return data["hits"][0]["audio"]
    except Exception:
        pass
    return "https://cdn.pixabay.com/download/audio/2022/03/15/audio_b9b733d85f.mp3?filename=dreamy-ambient-110857.mp3"

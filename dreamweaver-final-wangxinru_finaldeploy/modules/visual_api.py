import requests, streamlit as st
def get_visual(keyword):
    key = st.secrets.get("pixabay_key", None)
    if not key:
        return "https://cdn.pixabay.com/photo/2018/05/06/09/20/moon-3380450_1280.jpg"
    try:
        r = requests.get(f"https://pixabay.com/api/?key={key}&q={keyword}&image_type=photo&orientation=horizontal&safesearch=true")
        if r.status_code == 200:
            data = r.json()
            if data["hits"]:
                return data["hits"][0]["largeImageURL"]
    except Exception:
        pass
    return "https://cdn.pixabay.com/photo/2018/05/06/09/20/moon-3380450_1280.jpg"

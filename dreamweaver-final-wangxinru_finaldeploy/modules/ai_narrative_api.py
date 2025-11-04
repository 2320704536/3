import requests, streamlit as st
def generate_story(keyword):
    token = st.secrets.get("hf_token", None)
    if not token:
        return "Add your HuggingFace token in secrets to generate narratives."
    prompt = f"Write a short poetic description of a dream about {keyword}."
    try:
        r = requests.post("https://api-inference.huggingface.co/models/gpt2",
                          headers={"Authorization": f"Bearer {token}"}, json={"inputs": prompt})
        if r.status_code == 200:
            return r.json()[0]['generated_text']
    except Exception:
        pass
    return "Dream narrative unavailable."

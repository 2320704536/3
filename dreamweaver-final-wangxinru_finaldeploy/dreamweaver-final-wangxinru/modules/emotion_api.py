import requests, pandas as pd, plotly.express as px, streamlit as st
def plot_emotions(text):
    token = st.secrets.get("hf_token", None)
    if not token:
        return px.bar(x=[], y=[])
    try:
        r = requests.post("https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base",
                          headers={"Authorization": f"Bearer {token}"}, json={"inputs": text})
        data = r.json()[0]
        df = pd.DataFrame(data)
        return px.bar(df, x="label", y="score", title="Dream Emotion Map", color="label",
                      color_discrete_sequence=px.colors.sequential.Purples)
    except Exception:
        return px.bar(x=[], y=[])

import streamlit as st
from modules import dream_meaning_api, emotion_api, visual_api, global_trend_api, cultural_api, ai_narrative_api, sound_api

st.set_page_config(page_title="DreamWeaver • global dream database • wang xinru", page_icon="🌙", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
  background: radial-gradient(circle at 20% 20%, #1a103f 0%, #120a2a 40%, #0a061b 100%);
  color: #e0e7ff;
}
h1, h2, h3, label, p {
  color: #e0e7ff !important;
}
.sidebar .sidebar-content {
  background-color: rgba(20,10,50,0.6);
}
.block {
  background: rgba(255,255,255,0.08);
  padding: 1.5rem;
  border-radius: 12px;
  margin-bottom: 1.5rem;
  box-shadow: 0 0 20px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

st.title("🌙 DreamWeaver • global dream database • wang xinru")
st.caption("Explore the hidden meanings, emotions, and global patterns of dreams.")

# Sidebar
st.sidebar.header("✨ Dream Modules")
dream_input = st.sidebar.text_input("Enter your dream keyword", "water")

modules_selected = st.sidebar.multiselect(
    "Select modules to explore:",
    ["Emotion Map", "Dream Meaning", "Visual Dream", "Global Trends", "Cultural Interpretation", "AI Narrative", "Soundscape", "Save Dream Card"],
    default=["Emotion Map", "Dream Meaning", "Visual Dream", "Cultural Interpretation"]
)

run = st.sidebar.button("💫 Generate Dream Analysis")

if run:
    st.subheader(f"Dream Exploration: '{dream_input}'")

    if "Dream Meaning" in modules_selected:
        with st.spinner("Fetching dream interpretation..."):
            meaning = dream_meaning_api.get_dream_meaning(dream_input)
        st.markdown(f"<div class='block'><h3>💭 Dream Meaning</h3><p>{meaning}</p></div>", unsafe_allow_html=True)

    if "Emotion Map" in modules_selected:
        with st.spinner("Analyzing emotional patterns..."):
            fig = emotion_api.plot_emotions(dream_input)
        st.plotly_chart(fig, use_container_width=True)

    if "Visual Dream" in modules_selected:
        with st.spinner("Loading dream imagery..."):
            img = visual_api.get_visual(dream_input)
        st.image(img, caption=f"Dream Visual: {dream_input}", use_column_width=True)

    if "Global Trends" in modules_selected:
        with st.spinner("Analyzing global dream trends..."):
            map_fig = global_trend_api.show_trends(dream_input)
        st.plotly_chart(map_fig, use_container_width=True)

    if "Cultural Interpretation" in modules_selected:
        with st.spinner("Fetching cultural context..."):
            culture = cultural_api.get_culture_meaning(dream_input)
        st.markdown(f"<div class='block'><h3>🌏 Cultural Interpretation</h3><p>{culture}</p></div>", unsafe_allow_html=True)

    if "AI Narrative" in modules_selected:
        with st.spinner("Generating poetic dream narrative..."):
            story = ai_narrative_api.generate_story(dream_input)
        st.markdown(f"<div class='block'><h3>🧠 AI Dream Narrative</h3><p><i>{story}</i></p></div>", unsafe_allow_html=True)

    if "Soundscape" in modules_selected:
        with st.spinner("Loading dream soundscape..."):
            sound = sound_api.get_sound(dream_input)
        st.audio(sound)

    if "Save Dream Card" in modules_selected:
        st.markdown("<div class='block'><h3>💾 Save Dream Card</h3><p>Click the 'Download Dream Card' button below to save your dream as a PNG.</p></div>", unsafe_allow_html=True)
        st.download_button("Download Dream Card", data="Dream summary placeholder", file_name=f"{dream_input}_dreamcard.txt")

else:
    st.info("Enter a dream keyword and click '💫 Generate Dream Analysis' to begin.")

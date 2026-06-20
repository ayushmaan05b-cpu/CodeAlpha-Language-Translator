import streamlit as st
from deep_translator import GoogleTranslator
if "history" not in st.session_state:
    st.session_state.history = []

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌐",
    layout="centered"
)

st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>
🌐 Language Translation Tool
</h1>
<p style='text-align: center;'>
Translate text between multiple languages instantly.
</p>
""", unsafe_allow_html=True)

text = st.text_area(
    "✍ Enter Text",
    height=150,
    placeholder="Type something here..."
)

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "📥 Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "📤 Target Language",
        list(languages.keys())
    )
    st.button("🔄 Swap Languages")

if st.button("🔄 Translate", use_container_width=True):

    if text.strip():

        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)
        st.session_state.history.append(
    f"{text} ➜ {translated}"
)
        
        st.success("✅ Translation Completed")

        st.text_area(
            "📄 Translated Text",
            translated,
            height=150
        )

    else:
        st.warning("⚠ Please enter some text.")
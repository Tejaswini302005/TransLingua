import streamlit as st
from translator import translate_text
from languages import languages


# Page Config
st.set_page_config(
    page_title="TransLingua Translator",
    page_icon="🌍",
    layout="centered"
)


# Title
st.title("🌍 TransLingua: AI Multi-Language Translator")


st.write("Translate text instantly using Gemini AI")


# Text Input
input_text = st.text_area(
    "Enter Text",
    height=150
)


# Language Selection

col1, col2 = st.columns(2)


with col1:

    source_lang = st.selectbox(
        "Source Language",
        languages
    )


with col2:

    target_lang = st.selectbox(
        "Target Language",
        languages
    )


# Translate Button

if st.button("Translate"):

    if input_text == "":

        st.warning("Please enter text")

    elif source_lang == target_lang:

        st.warning("Source and target languages cannot be same")

    else:

        with st.spinner("Translating..."):

            output = translate_text(
                input_text,
                source_lang,
                target_lang
            )

            st.success("Translation Complete")


            st.text_area(
                "Translated Text",
                value=output,
                height=150
            )


# Footer

st.markdown("---")

st.markdown(
    "Developed using Gemini Pro + Streamlit"
)

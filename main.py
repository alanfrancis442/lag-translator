
import streamlit as st
from googletrans import Translator,LANGUAGES

# Set page title and icon
st.set_page_config(page_title="Language Translator", page_icon="🌐")

# Function to translate text
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Main function to render the web app
def main():
    st.title("Language Translator")

    # Text input box for user input
    input_text = st.text_area("Enter text to translate", "")

    target_language = st.selectbox("Select target language", LANGUAGES.values())

    if st.button("Translate"):
        if input_text == "":
            st.warning("Please enter text to translate.")
        else:
            translated_text = translate_text(input_text, target_language.lower())
            st.success("Translation:")
            st.write(translated_text)

if __name__ == "__main__":
    main()

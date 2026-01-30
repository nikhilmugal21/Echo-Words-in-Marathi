import streamlit as st
import unicodedata

IPA_VOWELS = (
    'i','y','ɨ','ʉ','ɯ','u',
    'ɪ','ʏ','ʊ',
    'e','ø','ɘ','ɵ','ɤ','o',
    'ə',
    'ɛ','œ','ɜ','ɞ','ʌ','ɔ',
    'æ','ɐ',
    'a','ɶ','ɑ','ɒ'
)

def strip_combining(text):
    return ''.join(
        ch for ch in unicodedata.normalize("NFD", text)
        if unicodedata.category(ch) != "Mn"
    )

st.title("Echo Word Generator")
st.write("Echo word formation in Marathi")

base_word = st.text_input("Enter base word (in IPA):").strip().lower()

    scan_word = strip_combining(base_word)

    i = None
    for idx, ch in enumerate(scan_word):
        if ch in IPA_VOWELS:
            i = idx
            break

    if i is None:
        st.error("No vowel found → cannot form echo word.")
    else:
        suffix = base_word[i:]
        suffix1 = base_word[i+1:]

        echo1 = "v" + suffix
        echo2 = "bi" + suffix1

        st.success("Echo Words Generated")
        st.write(f"**Echo Pair 1:** {base_word}-{echo1}")
        st.write(f"**Echo Pair 2:** {base_word}-{echo2}")

import streamlit as st
import joblib

# Load the model
model = joblib.load("language_detector.pkl")

# App title
st.title("🌍 Language Detection App")

# Input method: Text or File
option = st.radio("Choose input method:", ("Type Text", "Upload .txt File"))

text = ""

if option == "Type Text":
    text = st.text_area("Enter your sentence:", "")
elif option == "Upload .txt File":
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")

# Predict button
if st.button("Detect Language") and text.strip() != "":
    prediction = model.predict([text])[0]
    st.success(f"🌐 Detected Language: **{prediction}**")
elif text.strip() == "":
    st.info("Please enter or upload some text to detect.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Scikit-learn and Streamlit")

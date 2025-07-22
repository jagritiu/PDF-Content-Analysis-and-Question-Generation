import streamlit as st
import json
from PIL import Image

st.set_page_config(page_title="PDF Question Generator", layout="wide")
st.title("📘 AI-Powered PDF Question Generator")

# Load the questions JSON
with open("final_output/generated_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Loop through each page
for page in data:
    st.header(f"📄 Page {page['page']}")
    st.subheader("Text:")
    st.write(page["text"])

    st.subheader("Generated Questions from Images:")
    for q in page["questions"]:
        img = Image.open(q["image_path"])
        st.image(img, caption=q["generated_question"], width=300)
        st.markdown("---")

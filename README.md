# 📘 PDF Content Analysis and Question Generation

## 👋 Introduction

This project is developed as part of the AI/Python Internship Assignment. The goal is to create a Python-based tool that:

1. Extracts **text and images** from a PDF file.
2. Organizes the extracted content in a structured **JSON** format.
3. Prepares a foundation for future **AI-based question generation** using visual content.

---

## 🗂️ Folder Structure

```
pdf_content_analysis/
├── main.py
├── output/
│   ├── extracted_images/
│   └── content.json
├── IMO_Maths_Olympiad_Sample.pdf
├── README.md
└── venv/
```

---

## 🚀 Features

- ✅ Extracts all **text content** from the given educational PDF.
- ✅ Extracts all **images** page-wise and saves them.
- ✅ Generates a **structured JSON file** organizing text and image paths.
- ✅ Clean and modular Python code.

---

## 📦 Requirements

Install the following Python libraries:

```bash
pip install PyMuPDF pdfplumber Pillow
```

---

## 🛠️ How to Run

### Step 1: Activate your environment (optional)
```bash
venv\Scripts\activate
```

### Step 2: Make sure the sample PDF file is named:
```
IMO_Maths_Olympiad_Sample.pdf
```

### Step 3: Run the code
```bash
python main.py
```

### Step 4: Check Outputs

- Extracted text and image paths are stored in:  
  `output/content.json`

- All extracted images are saved in:  
  `output/extracted_images/`

---

## 📄 Sample JSON Output

```json
[
  {
    "page": 1,
    "text": "Page text content here...",
    "images": ["output/extracted_images/page1_image1.png"]
  },
  {
    "page": 2,
    "text": "Another page text...",
    "images": ["output/extracted_images/page2_image1.png"]
  }
]
```

---

## 🧠 Next Steps (Optional - For Phase 2)

- Use AI models like BLIP, T5, or GPT to generate **questions** from extracted content.
- Classify question types (MCQ, Image-based, etc.)
- Display output via a web interface (Streamlit/Flask).

---

## 📬 Feedback

Feel free to suggest improvements or raise issues by contacting me or forking this repo!

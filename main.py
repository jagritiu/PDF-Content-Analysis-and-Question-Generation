import fitz  # PyMuPDF
import os
import json

# Create output folders
output_dir = "output"
img_dir = os.path.join(output_dir, "images")
os.makedirs(img_dir, exist_ok=True)

# Open the PDF file
pdf_file = "IMO_Maths_Olympiad_Sample.pdf"
doc = fitz.open(pdf_file)

# Final structured output
output_json = []

# Loop through each page
for page_num, page in enumerate(doc, start=1):
    page_text = page.get_text()
    page_images = []

    # Extract images
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_filename = f"page{page_num}_image{img_index + 1}.{image_ext}"
        image_path = os.path.join(img_dir, image_filename)

        # Save image file
        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)

        page_images.append(image_path)

    # Add this page's data
    output_json.append({
        "page": page_num,
        "text": page_text.strip(),
        "images": page_images
    })

# Save structured JSON
json_path = os.path.join(output_dir, "extracted_content.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(output_json, f, indent=4)

print(f"✅ Extraction complete!\nText and images saved in '{output_dir}' folder.")

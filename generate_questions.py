from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import json
import os

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load extracted JSON
with open("output/extracted_content.json", "r") as f:
    data = json.load(f)

final_output = []

# Loop through pages and generate questions from each image
for entry in data:
    page = entry["page"]
    text = entry["text"]
    questions = []

    for img_path in entry["images"]:
        try:
            image = Image.open(img_path).convert('RGB')
            inputs = processor(images=image, return_tensors="pt")
            out = model.generate(**inputs)
            caption = processor.decode(out[0], skip_special_tokens=True)

            question = f"What can you observe in this image? {caption}"
            questions.append({
                "image_path": img_path,
                "generated_question": question
            })
        except Exception as e:
            print(f"❌ Error with image {img_path}: {e}")

    final_output.append({
        "page": page,
        "text": text,
        "questions": questions
    })

# Save final output
os.makedirs("final_output", exist_ok=True)
with open("final_output/generated_questions.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=4)

print("✅ Questions generated successfully!")

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import os

def main():
    # Ask for the image path
    image_path = input("Enter the path to the image file: ").strip()

    # Validate image file
    if not os.path.isfile(image_path):
        print("❌ File not found. Please check the path and try again.")
        return

    # Load BLIP model and processor
    print("⏳ Loading model...")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Load and process image
    try:
        image = Image.open(image_path).convert('RGB')
    except Exception as e:
        print("❌ Error opening image:", e)
        return

    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs, max_length=50)

    caption = processor.decode(output[0], skip_special_tokens=True)
    print("\n✅ Image description:", caption)

if __name__ == "__main__":
    main()

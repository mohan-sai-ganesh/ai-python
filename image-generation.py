import openai
import base64

response = openai.images.generate(
    model="gpt-image-1",
    prompt="A cute robot reading a book in a library",
    size="auto",  # options: 256x256, 512x512, 1024x1024
    n=1  # number of images to generate
)

image_base64 = response.data[0].b64_json

image_bytes = base64.b64decode(image_base64)

with open("generated_image.png", "wb") as f:
    f.write(image_bytes)

print("Image saved as generated_image.png")

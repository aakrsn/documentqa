import base64
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_API_KEY"
)

image_paths = ["image1.png", "image2.png", "image3.png"]

content = [
    {
        "type": "input_text",
        "text": "Extract all text from these images. "
                "Separate the results by image."
    }
]

for path in image_paths:
    with open(path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    content.append({
        "type": "input_image",
        "image_url": f"data:image/png;base64,{image_base64}"
    })

response = client.responses.create(
    model="nvidia/nemotron-3.5-super-vl:free",
    input=[
        {
            "role": "user",
            "content": content
        }
    ]
)

print(response.output_text)
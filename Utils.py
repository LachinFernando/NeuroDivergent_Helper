import streamlit as st
from openai import OpenAI
import base64
from PIL import Image
from io import BytesIO
import os
import requests

from prompts import RESTAURANT_IMAGE_GENERATION_PROMPT, RESTAURANT_QUESTION_GENERATION_PROMPT


MODEL_VERSION = "gpt-4o-mini"
IMAGE_GENERATION_MODEL = "dall-e-3"
SAVE_IMAGE_NAME = "output.png"


# set up your OpenAI API key and Assembly AI key
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


# create the openai client
client = OpenAI()


# function to generate image
def image_generation(required_prompt: str = RESTAURANT_IMAGE_GENERATION_PROMPT) -> bool:
    try:
        response = client.images.generate(
            model=IMAGE_GENERATION_MODEL,
            prompt=required_prompt,
            size="1024x1024",
            quality="standard",
            response_format="b64_json",
            n=1,
        )

        bytes_data = response.data[0].b64_json
        # generate and save the image
        image = base64.b64decode(bytes_data)
        payload = bytearray(image)
        stream = BytesIO(payload)
        read_image = Image.open(stream).convert("RGB")
        read_image.save(SAVE_IMAGE_NAME)

        return True
    except Exception as error:
        print("Error occured generating the image: {}".format(str(error)))

        return False


# function to generate question and answers
def question_generator(url: str = SAVE_IMAGE_NAME, required_prompt: str = RESTAURANT_QUESTION_GENERATION_PROMPT) -> str:
    # convert the image to bytes
    with open(url, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ["OPENAI_API_KEY"]}"
    }

    payload = {
        "model": MODEL_VERSION,
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": required_prompt
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    json_response = response.json()
    print(json_response)
    final_response = json_response["choices"][0]["message"]["content"]

    return final_response


def question_processor(text: str) -> tuple:
    process_text = text.replace("\n\n", ",")
    text_chunks = [text_.strip() for text_ in process_text.split(",")]
    question = text_chunks[0]
    answers = text_chunks[1:-1]
    final_answers = [ans_ for ans_ in answers if ans_]
    correct_answer = text_chunks[-1].replace(".","")

    return (question, final_answers, correct_answer)
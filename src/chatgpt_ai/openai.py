from dotenv import load_dotenv
import os
import openai

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def create_chatgpt_response(prompt):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    print(f"Response from chat gpt: {response}")
    response_dict = response.get('choices')
    if (response_dict and len(response_dict) > 0):
        # return the prompt response
        return response_dict[0].get('text')

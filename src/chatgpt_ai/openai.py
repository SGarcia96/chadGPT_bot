import openai
from src.constants import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def create_chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=100,
    )
    print(f"Response from chat gpt: {response}")
    response_dict = response.get('choices')
    if (response_dict and len(response_dict) > 0):
        # return the prompt response
        return response_dict[0].get('text')

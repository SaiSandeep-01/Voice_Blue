import openai
from keys import API_KEY

# OpenAI authentication
openai.api_key = API_KEY
        
def Generate_Img(prompt , num):
    words_to_remove = ["Generate","an","Image","of"]
    prompt_words = prompt.split(" ")
    filtered_words = [word for word in prompt_words if word.lower() not in words_to_remove]
    filtered_prompt = " ".join(filtered_words)
    response = openai.Image.create(
        prompt = prompt,
        n = num,
        size="512x512")
    Image_url = response['data'][0]['url']
    return Image_url
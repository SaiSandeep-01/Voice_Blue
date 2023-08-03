import webbrowser

def Maps(prompt):
    words_to_remove = ["where","is","find","the","location","of"]
    prompt_words = prompt.split(" ")
    filtered_words = [word for word in prompt_words if word.lower() not in words_to_remove]
    filtered_prompt = " ".join(filtered_words)
    url = "https://www.google.com/maps/place/" + "" +filtered_prompt
    response = "This is where " + str(filtered_prompt) + " is."
    webbrowser.open(url)

    return response
import webbrowser

def Search(prompt):
    if "google" in prompt.lower():
        words_to_remove = ["search","on","google"]
        prompt_words = prompt.split(" ")
        filtered_words = [word for word in prompt_words if word.lower() not in words_to_remove]
        filtered_prompt = " ".join(filtered_words)
        webbrowser.open(
          "https://www.google.com/search?query=" + "+"+filtered_prompt)
        response = "Searching " + str(filtered_prompt) + " on google"
    elif "youtube" in prompt.lower():
        words_to_remove = ["search","on","youtube","you","tube"]
        prompt_words = prompt.split(" ")
        filtered_words = [word for word in prompt_words if word.lower() not in words_to_remove]
        filtered_prompt = " ".join(filtered_words)
        print(filtered_prompt)
        webbrowser.open(
            "http://www.youtube.com/results?search_query=" +
            "+"+filtered_prompt
        )
        response = "Opening " + str(filtered_prompt) + " on youtube"
    return response
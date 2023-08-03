import wolframalpha
import keys

def Wolfram(user_input):
    user_input=user_input.lower()
    app_id = keys.APP_ID
    client = wolframalpha.Client(app_id)
    query = user_input.split()
    
    keywords = ["calculate", "compute", "math", "solve"]  # Wolfram
    for keyword in keywords:
        if keyword in query:
            ind = query.index(keyword)
            query = query[ind + 1:]
            break
    try:
        res = client.query(" ".join(query))
        answer = next(res.results).text
        response_str = "The answer is " + answer
    except:
        response_str = "Sorry, could you repeat yourself."

    return response_str
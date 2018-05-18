# bot.logic.py

import alfanous

def answer(query):
    response = alfanous.do(flags={"action":"search", "query":query, "unit": "aya", "highlight": "none"})
    if (response["search"]["interval"]["total"]):
         reply = "{" + response["search"]["ayas"][1]["identifier"]["sura_arabic_name"] + " "+ str(response["search"]["ayas"][1]["identifier"]["aya_id"]) + "}";
         reply += "\n{"+ response["search"]["ayas"][1]["aya"]["text"]+"}"
    else:
        reply = None
    return reply

LOGIC_RESPONSES = {
    "thank": [
         "Of course!",
        "Anytime!",
        "You're welcome",
         "You are so welcome!"
    ],
    "thanks": [
        "Of course!",
        "Anytime!",
        "You're welcome",
         "You are so welcome!"
    ],
    'help': [
        "A good place to get help is by going to our forums on http://joincfe.com/ask/",
        "You can always ask questions in our videos or on http://joincfe.com/ask/"
    ],
    'code': [
        "Have you considered looking at our code on http://joincfe.com/github/? That might help you",
        "We don't review code at this time, but you can consider looking at our open-source repo http://joincfe.com/github/"
    ],
}
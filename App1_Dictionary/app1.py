import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def transalte(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead?? Enter y if yes, n if No: " % get_close_matches(w, data.keys())[0])
        if yn.upper() == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.upper() == "N":
            return "The word does not exist. Please double check it." + yn
        else:
            return "Do not understand input." + yn
    else:
        return "This word does not exist"

word = input("Enter word: ")

output = transalte(word)

if type(output)  == list:
    for item in output:
        print(item)
else:
    print(output)
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s ? Enter Y for yes, N for no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn =="N":
            return "Word does not exist"
        else:
            return "Invalid input"
    else:
        return "Word does not exist"


word = input("Enter a  word: ")
word = word.lower()
output = translate(word)
if type(output) == list:
    for s in output:
        print(s)
else:
    print(output)
import json, difflib

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(difflib.get_close_matches(w, data.keys(), 1, .8))  > 0:
        yn = input("Did you mean %s instead? Enter Y is yes, or N if no") % difflib.get_close_matches(w, data.keys(), 1, .8)[0]
        if yn == "Y":
            return data[difflib.get_close_matches(w, data.keys(), 1, .8)[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't under5stand your query"
    else:
        return "There are no similar words in the dictionary to your entry."
        
word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
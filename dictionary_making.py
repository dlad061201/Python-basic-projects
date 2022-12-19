import json
from difflib import get_close_matches

# opening the file
file = open("data.json")
# returns JSON object as dictionary in python
data = json.load(file)

# write a function for the condition
def match(word):
    if word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Do you mean %s instead", get_close_matches(word, data.keys())[0])
        decision = input("Press Y/y for yes and N/n for no")
        if decision == "Y" or decision == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decision == "N" or decision == "n":
            return ("Sorry! We care unable to find your word.")
        else:
            return ("Looks like you've entered the wrong key.")

# main
word = input("Type the word to find it's meaning:")
func_output = match(word)
if type(func_output) == list:
    for item in func_output:
        print(item)
else:
    print(func_output)

import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("english-thesaurus\\data.json"))

def eng_thesaurus(word):
    word = word.lower()

    if word in data:
        found = data[word]
        for i in range(0, len(found)):
            if i == 0:
                print("Meaning 1: ", found[i])
            else:
                print("Meaning ", str(i + 1) + ":", found[i])

    else:
        closet_word = get_close_matches(word, data.keys(), cutoff=0.75)
        for j in range(0, len(closet_word)):
            print("Did you mean the word: ", closet_word[j], "?\n")
            op = input("Press Yes-Y, No-N, Exit-E: ")
            x = data[closet_word[j]]
            if op == 'Y':
                for k in range(0, len(x)):
                    print("Meaning " + str(k + 1), ":", x[k])
                break
            elif op == "N":
                print(
                    "Error: Word doesn't exist!! Please check the entered word."
                )
                break
            elif op == "E":
                exit
print("\nCtrl-C to exit")

while True:
    eng_thesaurus(input("\nEnter the word to find meaning."))




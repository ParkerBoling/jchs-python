                     #.------------------.
#park cursor here --->|                  |
                     #.------------------.

# -- in -- #
# word

# -- process -- #
# separate words
# remove characters other than letters
# move first letter to end
# add ay to the end
# continue or stop

# -- output -- #
# translated sentence
# ask to continue
    
def cleanWord(sentence):
    cleaned = ""
    for char in sentence.lower():
        if char.isalpha() or char == " ":
            cleaned += char
    return cleaned

def pigLatin(words):
    result = []
    vowels = "aeiou"

    for word in words:
        start = ""
        end = ""
        core = word
        
        while core and not core[0].isalpha():
            start += core[0]
            core = core[1:]
            
        while core and not core[-1].isalpha():
            end = core[-1] + end
            core = core[:-1]

        if core == "":
            result.append(word)
            continue

        # pig latin
        if core[0] in vowels:
            pig = core + "way"
        else:
            consonants = 0
            for char in core:
                if char not in vowels:
                    consonants += 1
                else:
                    break
            pig = core[consonants:] + core[:consonants] + "ay"

        result.append(start + pig + end)

    return " ".join(result)


def main():
    sentence = input("Enter the word or phrase you would like to convert into piglatin: ")
    words = sentence.split()
    pigLatinSentence = pigLatin(words)
    print(pigLatinSentence)


if __name__ == "__main__":
    main()
# INPUT #
'''
sentence
shift amount
shift direction
to continue or not
'''
# PROCESS #
'''
convert character into unicode
shift
convert back to alphabetical character
ask to continue
'''
# OUTPUT #
'''
shifted text
ask to continue
'''

# JACKSON --> MAIN
# PARKER --> CIPHER

def caesarCipher(text, shift, direction):
    direction = direction.lower()

    if direction in ["left", "backwards"]:
        shift *= -1
    elif direction in ["right", "forwards"]:
        pass
    else:
        print("INVALID SHIFT INPUT...")
        return text

    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            encryptedChar = chr((ord(char) - start + shift) % 26 + start)
            result += encryptedChar
        else:
            result += char

    return result


def main():
    choice = "yes"

    while choice.lower() == "yes":
        text = input("Enter a word, phrase, or sentence: ")
        shift = int(input("Enter a shift value: "))
        direction = input("Enter the shift direction (left/right, backwards/forwards): ")

        encrypted = caesarCipher(text, shift, direction)
        print("Encrypted sentence:", encrypted)

        choice = input("Would you like to encode another message? (yes/no): ")
        print()


if __name__ == "__main__":
    main()

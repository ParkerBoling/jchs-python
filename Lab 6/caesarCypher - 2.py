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

def caesarCipher(text, shift, dir):
  dir = dir.lower()
  if dir == "left":
    shift *= -1
  
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
    dir = input("Enter the shift direction: ")
    

    encrypted = caesarCipher(text, shift, dir)
    print("Encrypted sentence:", encrypted)

    choice = input("Would you like to encode another message? (yes/no): ")
    print()

if __name__ == "__main__":
  main()
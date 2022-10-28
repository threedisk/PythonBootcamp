alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift):
    cipher_text=""
    for i in text:
        x = alphabet.index(i) + shift
        cipher_text += alphabet[x]
    print(f"The encoded text is {cipher_text}")
#encrypt(text,shift)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(cipher_text,shift):
    cipher_text=input("Type your cipher text? ")
    plain_text=""
    for i in cipher_text:
        x = alphabet.index(i) - shift
        plain_text += alphabet[x]
    print(f"The decoded text is {plain_text}")
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message. encrypt(plain_text=text, shift_amount=shift)
if direction == "encode":
  encrypt(text=text, shift=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift=shift)
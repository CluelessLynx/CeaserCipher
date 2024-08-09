# Task one and two, encrypt and decrypt ceaser cipher
# Beryl Astrid Neubauer S210065305

# defining variables
text = ""
text_encrypted = ""
text_decrypted = ""

#the alphabet was initially thought to only let the person type in text and no numbers, but I haven't managed to finish it in time
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_small = "abcdefghijklmnopqrstuvwxyz"
shift = 0
choose = 0

# defining functions
# decryption function gets the input of the user with the number of the shift
def decryption(unenc_text, shiftnr):
    dec_text = ""

    #the length of the text gets iterated in the for-loop, for every char. First the char-variable gets one letter from the text.
    #then it is decided if it is an uppercase or lowercase letter to get the ascii value of it which is subtracted by the shiftnumber
    #if there is no letter it should just add a space
    #then modulo is used with the number of the alphabet to take out the numbers of how often it is looped over the full alphabet, leaving
    #only the rest in which the alphabet gets shifted
    #the shifted char is added to the text leaving the decrypted message
    for i in range(len(unenc_text)):
        char = unenc_text[i]

        # uppercase letter starts from 65-90 modulo is for the looping in the alphabet
        # ord = return its integer Unicode code value
        if (char.isupper()):
            dec_text += chr((ord(char) - shiftnr - 65) % 26 + 65)

        # lowercase letter ascii starts from 97-122
        elif (char.islower()):
            dec_text += chr((ord(char) - shiftnr - 97) % 26 + 97)
        #defining the dot which should not be changed
        elif(char=='.'):
            dec_text += chr(ord(char))
        # if it is anything else it is a space
        else:
            dec_text += " "
    return dec_text


# encryption
def encryption(unenc_text, shiftnr):
    enc_text = ""

    # getting every char
    for i in range(len(unenc_text)):
        char = unenc_text[i]

        # uppercase letter starts from 65-90 modulo is for the looping in the alphabet
        if (char.isupper()):
            enc_text += chr((ord(char) + shiftnr - 65) % 26 + 65)

        # lowercase letter ascii starts from 97-122
        elif (char.islower()):
            enc_text += chr((ord(char) + shiftnr - 97) % 26 + 97)
            #defining the dot which should not be changed
        elif(char=='.'):
            enc_text += chr(ord(char))
        # if it is anything else it is a space
        else:
            enc_text += " "
    return (enc_text)


# main code beginns with welcoming the user and if the user decides to encrypt or decrypt
print("Hello welcome to the ceaser cypher en- and decrypter \n")
choose = int(input("Please choose \n 1: encrypt \n 2: decrypt \n Input: "))

# encryption: The user has to put in the text which he wants to encrypt and the number to shift the alphabet
# the function of encryption is opened and saved in the variable text_encrypted which is shown to the user.
if choose == 1:
    print("You choose encryption\n")
    text = input("Please input the text to encrypt: ")
    shift = int(input("\nType in the number that the text needs to be shifted: "))
    text_encrypted = encryption(text, shift)
    print("\nYour text is:" + text)
    print("\nThe encryption is:" + text_encrypted + "\n")

# decryption: The user has to put in the text which he wants to decrypt and the number to shift the alphabet
# the function of decryption is opened and saved in the variable text_decrypted which is shown to the user.
elif choose == 2:
    print("You chose decryption\n")
    text = input("Please input the text to decrypt: ")
    shift = int(input("\nType in the number that the text needs to be shifted: "))
    text_decrypted = decryption(text, shift)
    print("\nYour text is:" + text)
    print("\nThe encryption is:" + text_decrypted + "\n")
# if the user types in anything else then 1 or 2 the code closes
else:
    print("This option is NOT possible")

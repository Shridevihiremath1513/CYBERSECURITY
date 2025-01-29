
#Encryption Function
def Encryption(message,shift):
    result = ""
    # perform the iteratation on the given mesasge
    for i in range(len(message)):
        char = message[i]
        
        # Check when there is space in message, and then add it.
        if char==" ":
            result+=" "

        # check if a character is uppercase then encrypt it according to uppercase character
        elif (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)

        # check if a character is lowercase then encrypt it according to lowercase character
        else:
            result += chr((ord(char) + shift-97) % 26 + 97)
    
    return result

#Decryption Function
def Decryption(message,shift):
    return Encryption(message, -shift)

#main function
message = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value: "))

encrypted_message = Encryption(message, shift)
decrypted_message = Decryption(encrypted_message, shift)

print("\nEncrypted message:", encrypted_message)
print("\nDecrypted message:", decrypted_message)
print("\n\n")


        
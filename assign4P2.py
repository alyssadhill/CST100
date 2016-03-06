# Defines the method encrypt that takes a message and key as arguments
def encrypt(message, key):
    # Stores the encrypted message 
    encrypted = ""
    # Loop through the characters of the message 
    for c in message:
        # takes the character and returns its ascii code
        asciiCode = ord(c)
        # encrypt algorithm that takes character and key and encrypts it 
        if asciiCode + key > 126:
            encrypted += chr(((asciiCode + key) - 127) + 32)
        else:
            encrypted += chr(asciiCode + key)
    # return the encrypted message
    return encrypted
    
# Have user input message and key 
encode = input("Enter a regular message to encode: ")
key = input("Enter a key value (between 0 and 100) for encoding: ")
# print the encrypted message and convert key to an interger
print("The encoded message is:", encrypt(encode, int(key)))


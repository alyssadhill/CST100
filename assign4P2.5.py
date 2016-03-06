# Part 2 of Part 2
# Defines the method decrypt that takes a message and key as arguments
def decrypt(message, key):
    # Stores the decrypted message 
    decrypted = ""
    # Loop through the characters of the message 
    for c in message:
        # takes the character and returns its ascii code
        asciiCode = ord(c)
        # decrypt algorithm that takes character and key and decrypts it 
        if asciiCode - key < 32:
            decrypted += chr(((asciiCode - key) + 127) - 32)
        else:
            decrypted += chr(asciiCode - key)
    # return the decrypted message
    return decrypted
    
# Have user input message 
decode = input("Enter an encrypted message to decode: ")
# print the message that the message will be decoded 1 to 100
print("The following are the decoded messages for keys 1 to 100:")
# Loop through keys 1 to 101
for key in range(1,101):
    # Prints messages decrypted with keys 1 to 100
    print("Key: ", int(key),"-> Decoded Message: ", decrypt(decode,key))

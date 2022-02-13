def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) + key) % 26

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result
    
def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % 26

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result
plain = input("enter your message to encrypt : ")
key = int(input("entre the key for encyption : "))
cipher = encrypt(key,plain)
print("your cipher is : " + cipher)

dcipher = input("enter your cipher text to dencrypt : ")
dkey = int(input("entre the key for decyption : "))
plain_text = decrypt(dkey,dcipher).lower()
print("your plain text is : " + plain_text)

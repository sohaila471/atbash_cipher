def atbash_cipher(plaintext):     # atbash_cipher is our function name
    
    result = " "
    for c in plaintext:  
        if c.isalpha():   # it check the Character 
            if c.isupper(): # used for Uppercase
                result +=chr(ord('Z') - (ord(c)- ord('A')))
            else: # used for lowecase
                result += chr(ord('z') - (ord(c)- ord('a')))
        else:
             result += chr  # used for not changing the non-alphabetic characters ( spaces etc.)
    return result
    
plaintext = input( " enter a plaintext :")   # user input 
ciphertext=atbash_cipher( plaintext)   # encrypt the msg
print("ciphertext :", ciphertext )
plaintext = atbash_cipher( ciphertext)  # decryt the msg
print(" plaintext :", plaintext)
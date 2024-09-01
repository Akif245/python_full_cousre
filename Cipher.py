alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'
          ,'t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'
          ,'t','u','v','w','x','y','z']
direction=input("Type '1' to to encrypt ,Type '2' to decrypt\n")

text=input("Type your message \n").lower()

shift=int(input("Type the number to shift \n"))
if direction=="1":
    def encrypt(usertext,Shiftnum):
        cipher_letter=""
        for letter in usertext:
            position=alphabet.index(letter)
            new_pos=position+Shiftnum
            new_letter=alphabet[new_pos]
            cipher_letter=cipher_letter+new_letter
        print(f"The Encrypted letter is {cipher_letter}")

    encrypt(text,shift)

elif direction=="2":
    def decrypt(usertext1,Shiftnum1):
        cipher_letter1=""
        for letter in usertext1:
            position=alphabet.index(letter)
            new_pos=position-Shiftnum1
            new_letter=alphabet[new_pos]
            cipher_letter1=cipher_letter1+new_letter
        print(f"The Decrypted letter is {cipher_letter1}")

    decrypt(usertext1=text,Shiftnum1=shift)
else:
   print("You have Intered wrong direction\n")


























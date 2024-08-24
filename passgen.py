import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
         't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L',
         'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','@','#','$','%','^','&','*','+']

print("Welcome to password generator !\n")

pass_letters=int(input("How many Letters you want in your password\n"))

pass_symbols=int(input("How many Symbols you want in your password\n"))

pass_num=int(input("How many Numbers you want in your password\n"))

password=" "

for char in range(1, pass_letters + 1):
   password += random.choice(letters)

for char in range(1, pass_symbols + 1):
   password += random.choice(symbols)
for char in range(1, pass_num + 1):
   password += random.choice(numbers)

print(password)
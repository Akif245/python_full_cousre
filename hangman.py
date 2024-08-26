import random
word_list=["akif","ahmed","abdul"]

chosen_word=random.choice(word_list)
print(chosen_word)
guess=input("Guess a letter\n").lower()
#print(guess)

for letter in chosen_word:
    if letter==guess:
        print("Right")
    else:
        print("Wrong")
display=[]
for letter in chosen_word:
    display.append("_")
print(display)
if chosen_word==guess:
    display.append(guess)
    print(display)
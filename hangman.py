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
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)
guess=input("Guess a letter\n").lower()
for position in range(word_length):
    letter = chosen_word[position]
if letter==guess:
    display[position]=letter
print(display)
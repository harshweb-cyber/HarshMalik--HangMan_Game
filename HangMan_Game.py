# uses of random 
# uses of filefunction


import random

# use file from your computer to use also give full path if not in same folder
 f = open("hangmanTxt.txt", "r") 
data = f.read() 
f.close()  


words = data.split()


word = random.choice(words).upper()


total_chances = 7
guessed_word = "-" * len(word)


while total_chances != 0:
    print(guessed_word)
    letter = input("Guess a letter: ").upper()

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
        if guessed_word == word:
            print("Congratulations! You won!!")
            break
    else:
        total_chances -= 1
        print("Incorrect Guess")
        print("The remaining chances are:", total_chances)

else:
    print("Game Over")
    print("You Lose")
    print("All the chances are exhausted")

print("The correct word is =", word)

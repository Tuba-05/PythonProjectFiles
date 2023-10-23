from string import ascii_lowercase
import time

def highscore():
    file1 = open("highscore.txt","a+")
    file1.seek(0)
    f = file1.read().split()
    high = 0
    for i in f:
        if high<int(i[-2:]):
            high = int(i[-2:])
    return high

# game mode
print('1=user''\n''2=admin')
time.sleep(1.5)
option = int(input('you are playing as: '))
# player mode:
if option == 1:
    fh = open('highscore.txt', 'r')
    f = open('words.txt', 'r')
    word_file = f.read()  # reading a word file
    word_file = word_file.split()
    f.close()
    # importing a random word from file
    import random
    word = random.choice(word_file)
    secret_word = '_' * len(word)
    user_name = input('enter your name')
    print('welcome to the game hangman!')
    time.sleep(1)
    print('I am thinking of a word that is', len(word),'letters long')
    time.sleep(1)
    print('You have 3 wranings and 6 guesses')
    time.sleep(1)
    # available_letters = 'abcdefghijklmnopqrstuvwxyz' or 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    available_letters = [i for i in ascii_lowercase]
    print('available letters =', "".join(available_letters))
    print(secret_word)
    time.sleep(1)
    warn = warning = 3
    guess = 6
    guessed_letters = []
    while guess!=0:
        letter = input('enter a guess')
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    secret_word = secret_word[:i] + letter + secret_word[i + 1:]
                    print(secret_word)
        elif letter not in word:
            print(secret_word)
            if letter in ('a','e','o','i','u') and letter in available_letters:
                guess-=2
                if letter not in ('a','e','o','i','u'):
                guess-=1

        if letter in guessed_letters or letter =="" or letter not in available_letters:
            warn-=1
            if warn>=0:
                warning-=1
            if warn<0:
                warning=0
                guess-=1
        time.sleep(1)
        print('you have', guess, 'guess', 'and', warning, 'warning left')
        time.sleep(1)
        try:
            available_letters.remove(letter)
            guessed_letters.append(letter)
        except:
            pass
        for j in range(len(available_letters)):
            if letter in available_letters:
                if available_letters[j]==letter:
                    available_letters = available_letters[ :j] + available_letters[j+1: ]
        print('available letters =',"".join(available_letters))
        time.sleep(1.5)
        if secret_word == word:
            break

    if secret_word == word:
        print('CONGRATULATION!! YOU GUESSED CORRECTLY')
        time.sleep(1.5)
        print('The word is ', secret_word)
    else:
        print('OOPS SORRY YOU GUESSED WRONG\nThe correct word is ', word)
    score = guess * len(set(word))
    file1 = open("highscore.txt", "a")
    file1.write(str(score) + " ")
    file1.close()
    time.sleep(1.5)
    print("Your score is", score)
    time.sleep(1.5)
    print("The Highscore is", highscore())
# administrative mood:
else:
    print('1=Add a word in the text file\n2=Reset the highscore')
    time.sleep(1)
    choice = int(input('enter your choice: '))
    if choice == 1:
        file1 = open('words.txt', 'a+')
        f = file1.read().split()
        new_word = input('enter a word: ')
        if new_word in f:
            print('Entered word is already in the file')
            time.sleep(1.5)
            another_word = input('Enter another word: ')
            file1.write(another_word + " ")
        else:
            file1.write(new_word + " ")
    else:
        fh = open('highscore.txt', 'w').close()





from string import ascii_lowercase
import random

def highscore():
    ''''''
    file1 = open("highscore.txt", "a+")
    file1.seek(0)  # --> Incase if the file already exist then it will take the pointer to the start.
    #
    read = file1.read().split()
    player_highscore = 0
    highscorer_name = ""
    for i in read:
        if "=" in i[-2:]:
            if player_highscore < int(i[-1:]):
                highscorer_name = i[:-2]
                player_highscore = int(i[-1:])
        else:
            if player_highscore < int(i[-2:]):
                highscorer_name = i[:-3]
                player_highscore = int(i[-2:])

    print(f"{highscorer_name} is the best player with a score of {player_highscore}")


def admin_mode(choice):
    if choice == 1:
        file1 = open('words.txt', 'r+')
        f = file1.read().split()
        new_word = input('Enter all the words with comma seperation: ').split(",")
        for word in new_word:
            if word not in f:
                file1.write(word + " ")
        print("The words are added successfully")
    elif choice == 2:
        open('highscore.txt', 'w').close()
        print("Scores are reset")
    elif choice == 3:
        game()
    elif choice == 4:
        return None
    else:
        print("Invalid Option")
    print('1=Want to Add more words in the text file\n2=Reset the Highscore\n3=To play the game\n4=TO Exit')
    choice = int(input('Enter your choice: '))
    admin_mode(choice)


def Secret_word():
    '''Takes no argument and returns the secret word from the words file.'''
    file1 = open("words.txt")
    f = (file1.read()).split()
    file1.close()
    return random.choice(f)


def player_score(word, guess, username):

    score = guess * len(set(word))
    file1 = open("highscore.txt", "a")
    file1.write(f"{username}={str(score)} ")
    file1.close()
    print("Your score is", score)
    highscore()


def game():
    word = Secret_word()
    print(word)
    secret_word = '_' * len(word)
    print(f'Welcome to the Game Hangman!\nI am thinking of a word that is {len(word)} letters long\nYou have 6 '
          f'Guesses and 3 Warnings')
    available_letters = [i for i in ascii_lowercase]
    print('available letters =', " ".join(available_letters))
    print(secret_word)
    warn = warning = 3
    guess = 6
    guessed_letters = []
    while guess>0:
        letter = input('Enter a Guess : ')
        if len(letter)==1:
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        secret_word = secret_word[:i] + letter + secret_word[i + 1:]

            elif letter not in word:
                if letter in ('a', 'e', 'o', 'i', 'u') and letter in available_letters:
                    guess -= 2
                if letter not in ('a', 'e', 'o', 'i', 'u'):
                    guess -= 1

            if letter in guessed_letters or not letter.isalpha():
                warn -= 1
                if warn >= 0:
                    warning -= 1
                if warn < 0:
                    warning = 0
                    guess -= 1

            print(secret_word)

            print(f'you have {guess} guesses and {warning} warnings left')
            try:
                available_letters.remove(letter)
                guessed_letters.append(letter)

            except ValueError:
                pass
            #
            # for j in range(len(available_letters)):
            #     if letter in available_letters:
            #         if available_letters[j] == letter:
            #             available_letters = available_letters[:j] + available_letters[j + 1:]
            print('available letters =', " ".join(available_letters))
            if secret_word == word:
                break

        else:
            print("Enter Only 1 letter")

    if secret_word == word:
        print('CONGRATULATION!! YOU GUESSED CORRECTLY\nThe Word is ', word)
        player_score(secret_word, guess, user_name)
    else:
        print('OOPS SORRY YOU GUESSED WRONG\nThe correct word is ', word)
        highscore()
        choose = (input("TO Play Again : Press 1\nTO Exit : Press any key except 1 : "))
        if choose == "1":
            game()
        else:
            return None




print('1=User\n2=Admin')
option = int(input('you are playing as: '))
if option == 1:
    user_name = input('Enter your name : ')
    game()
elif option == 2:
    print('1=Add a word in the text file\n2=Reset the Highscore\n3=To play the game\n4=To Exit')
    choice = int(input('Enter your choice: '))
    admin_mode(choice)
else:
    print('Invalid Input')
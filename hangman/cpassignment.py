# mode selection:
print('press 1 or 2', '\n', '1.Player mode', '\n', '2.Administrative mode')
fh = open('scores.txt', 'r')
for line in fh:
    print(line, end='')
fh.close()
print()
mode_ = int(input('select option:'))
# player mode:
if mode_ == 1:
    print('player mode')
    f = open('words.txt', 'r')
    c = f.read().split()
    f.close()

    # entering name:
    user_name = input('enter your name:')
    # importing a random word from file:
    import random
    word = random.choice(c)
    # guess word puzzle game starts:
    warnings = 3
    guess = 6
    print(f' Welcome to the game Hangman!\nI am thinking of a word that is', len(word),'letters long\nYou 3 warnings left\nYou have 6 guess left ')
    K = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
    print('available letters:', K)
    alpha = 'abcdefghijklmnopqrstuvwxyz' or 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    L = len(word) * '_'
    print(L)
    while guess != 0:
        # when your guesses are not equal to zero or either you guess the letter:
        while word != L and guess > 0:
            letter = input('plz guess a letter:').lower()
            if letter in K and letter in word:
                print('good guess:', letter)
                for i in range(len(word)):
                    if word[i] == letter:
                       L = L[:i] + letter + L[i + 1:]
                print(L)
                print('you have', warnings, 'warnings left')
            elif letter not in K and not(letter.isalpha()):
                print('that letter is not valid')
                if warnings == 0 or warnings == 'no warnings':
                    print('you have no warnings left so you lose one guess')
                    guess -= 1
                    warnings = 'no warnings'
                else:
                    warnings -= 1
                    guess -= 1
                    print('you have', warnings, 'warnings left')
            elif letter not in K and letter.isalpha():
                print('you have already guessed that letter')
                if warnings == 0 or warnings == 'no warnings':
                    print('you have no warnings left so you lose one guess')
                    guess -= 1
                    warnings = 'no warnings'
                else:
                    warnings -= 1
                    guess -= 1
                print('you have', warnings, 'warnings left')
            elif letter not in word and letter in K:
                print('oops!that letter is not in my word')
                if warnings == 0 or warnings == 'no warnings':
                    print('you have no warnings left so you lose one guess')
                    guess -= 1
                    warnings = 'no warnings'
                else:
                    warnings -= 1
                    guess -= 1
                    print('you have', warnings, 'warnings left')
            for j in range(len(K)):
                if letter in K:
                    if K[j] == letter:
                       K = K[:j] + K[j + 1:]
            print('available letters:', K)
            print('you have', guess, 'guess left')
        # if guesses becomes zero:
        else:
            print('you guessed the word which was', word)
            print('you have', guess, 'guess left\nyou have', warnings, 'warnings left')
            print('available letters:', K)
            break
    else:
        print('')
    # win or lose:
    if guess == 0:
        print('OOPS SORRY! You Lost The Game\nthe correct word was', word)
    else:
        print('CONGRATYLATIONS!!! You Won The Game')
    # For unique words:
    W = []
    for letter in word:
        if letter not in W:
            W.append(letter)
    # score:
    score = int(guess) * int(len(W))
    # storing score:
    # D={}
    # Key_=user_name
    # Value_=score
    # D[Key_]=Value_
    fh = open('scores.txt', 'a+')
    fh.write(f'{str(user_name)}={str(score)}\n')
    fh.seek(0)
    s = fh.read()
    s = s.split()
    # for highest score:
    h_score = s[0]
    for i in range(len(s)):
        if s[i] > h_score:
            h_score = s[i]
    # printing user's score either it's a highscore or not:
    if str(score) > h_score:
        print('HIGH SCORE!!!, your score is', score)
    else:
        print('your score is', score)
    fh.close()
# administrative mode:
if mode_ == 2:
    print('Administrative mode')
    for_more_words_ = ' Y '
    while for_more_words_ != " N ":
        print(f"Do you want add more words?\nIf 'YES' press 'Y' or If 'NO' press 'N'")
        for_more_words_ = input('').upper()
        if for_more_words_ == "Y":
            print(f'In this mode what do you want to do\na. to add words in file\nb. to reset score')
            choice_ = input('Select from given options:').lower()
            if choice_ == 'a':
               f = open('words.txt', 'a+')
               m = input('enter word:').lower()
               f.write(m)
               f.seek(0)
               c = f.read().split()
               f.close()
            elif choice_ == 'b':
               fh = open('scores.txt', 'w')
               fh.write()
               fh.close()
            else:
               print('Hello! you are entering wrong choice.')
        else:
            break

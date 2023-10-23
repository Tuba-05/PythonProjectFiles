warnings=3
guess=6
print(f'Welcom to the game Hangman!\nI am thinking of a word that is 4 letters long\nYou 3 warnings left\nYou have 6 guess left')
W=[]
word='apple'
list1=['@', '#','!','$','%','*','^','&','?','<','>','/','(',')','~',' ']
K='abcdefghijklmnopqrstuvwxyz' or 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('available letters:',K)
while guess>0:
   while len(word)!=len(W) and guess>0:
      letter=input('plz guess a letter:')
      if letter in K and letter in word and letter not in W:
         print('good guess:',letter)
         W.append(letter)
         print(W)
         print('you have', warnings, 'warnings left')
      elif letter in W:
         print('you have already guessed that letter')
         if warnings==0 or warnings=='no warnings':
            print('you have no warnings left so you lose one guess')
            guess-=1
            warnings='no warnings'
         else:
            warnings-=1
            guess-=1
         print('you have', warnings, 'warnings left')
      elif letter not in word:
         print('oops! that letter is not in my word')
         if warnings == 0 or warnings=='no warnings':
            print('you have no warnings left so you lose one guess')
            guess-=1
            warnings='no warnings'
         else:
            warnings-=1
            guess-=1
         print('you have', warnings, 'warnings left')
      elif '0'<=letter<='9' or letter in list1:
         print('that is not a valid letter')
         if warnings == 0 or warnings=='no warnings':
            print('you have no warnings left so you lose one guess')
            guess-=1
            warnings='no warnings'
         else:
            warnings-=1
            guess-=1
            print('you have',warnings,'warnings left')
      print('you have', guess, 'guess left')
   else:
      print('you guessed the word which was',W)
      print('you have', guess, 'guess left\nyou have', warnings, 'warnings left')
   break
else:
   print('')
if guess==0:
   print('you lost the game\nthe correct word was',word)
else:
   print('you won the game')



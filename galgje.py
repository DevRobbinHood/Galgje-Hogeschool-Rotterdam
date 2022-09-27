HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  |   |
  0   |
 /|\  |
 / \  |
========='''
]

word = input('Enter a word: ')
print(word)

play = True
mistakes = 0
wordlist = []
for index in word: 
    wordlist += '_'
    
while play: 
    letter = input('Enter a letter: ')
    
    letterInWord = letter in word 
    if letterInWord == False:
        print(HANGMANPICS[mistakes])
        mistakes = mistakes + 1
        print('You made a mistake. Try again!')
        
        if mistakes >= 9:
            print('You have lost game over. Try again!')
            play = False
    
    else:
        for index in range(len(word)):
            if word[index] == letter:
                wordlist[index] = letter
            
        guessedWord = ''.join(wordlist)
        if(guessedWord == word):
            print('Congratulations you won!')
            play = False
            
        print(wordlist)

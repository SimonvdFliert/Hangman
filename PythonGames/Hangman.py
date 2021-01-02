import random
import PySimpleGUI as sg


word_list = [] 

def get_Words():
    # Open file to be able to read content
    textOfWords = open("Words.txt", "r")

    # Go through file and append it to an empty list
    for word in textOfWords:
        word_list.append(word.rstrip('\n'))

    #Close file when done reading its content
    textOfWords.close()

    # Choose a random number from 1 to length of list - 1
    chosenWordIndex = random.randint(1, (len(word_list) - 1))

    # Retrieve the word from the list of words that lies at the random generated number index
    return word_list[chosenWordIndex]


# Create the hangman bord
def play_Game(word):
    
    #given_word = chosenword
    previousGuesses = []
    wordGuessed = False
    lives = 5

    
    message = f"The length of the word is {len(word)}. Your word is {word}. "
    wordCompletion = "_" * len(word)
   # print(welcomeMessage + '\n')
    #print(message + '\n')
   # print( wordCompletion+ '\n' * 2)

  #  while lives > 0 and wordGuessed == False:

        #User Input
    #    chosen_letter = input("Please enter a letter:" ).lower()

     #   if len(chosen_letter) == 1 and chosen_letter.isalpha():
            
         #   if chosen_letter in previousGuesses:
          #      print(f"You have already guessed this letter. The letters you have guessed are: {previousGuesses}")
            
          #  elif chosen_letter not in word:
          #      print(f"{chosen_letter} is not in the word. You have {lives - 1} left.")
          #      previousGuesses.append(chosen_letter)
          #      lives -= 1

         #   else:
         #       print('\n' + f'Nice! The letter {chosen_letter} is in the word.' '\n')
          #      previousGuesses.append(chosen_letter)

            # Change the string to a list to fill in the letter of the word
          #      wordCompletionAsList = list(wordCompletion)
          #      letterIndices = [i for i, letter in enumerate(word) if letter == chosen_letter]

                # Replace the "_" with the chosen letter 
           #     for index in letterIndices:
           #         wordCompletionAsList[index] = chosen_letter
           #     wordCompletion = "".join(wordCompletionAsList)

            #    if "_" not in wordCompletion:
           #         wordGuessed = True

           #     print(wordCompletion + '\n')

       # elif len(chosen_letter) != 1:
          #  print("You have not entered the right amount of letters. Please only guess one letter per turn.")

     #   else:
          #  print("You have not entered a letter of the alphabet.")

    #Lose    
   # if lives == 0:
       # print(f"Game Over! You have run out of lives. The correct word was {word}" + '\n')

    #Win
   # if wordGuessed == True:
     #   print(f"Congratulations! You have correctly guessed the word. The word was {word}. You had {lives} lives remaining.")
    
    # Ask the player if he or she want to play the game ---> Starting Screen
    
    layout = [[sg.Text("Hello")],
        [sg.Text(message)],
        [sg.Text(wordCompletion)],
        [sg.Input(key='-INPUT-')],
        [sg.Text(size=(40,1), key='-OUTPUT-')],
        [sg.Button('Guess'), sg.Button('Quit')]]

        # Create the window
    game_window = sg.Window('Hangman', layout)


    #Goes into an infinite loop waiting for a button pressed. Due to the crash of the gui the button is never pressed.
    while lives > 0 and wordGuessed == False:
   
        # Display and interact with the Window using an Event Loop
        game_event, game_values = game_window.Read(timeout=100)

        # See if user wants to quit or window was closed
        if game_event == sg.WINDOW_CLOSED or game_event == 'Quit':
            lives = 0
            break

        if game_event == 'Guess':
            if len(game_values['-INPUT-']) == 1 and game_values['-INPUT-'].isalpha(): #CRASHES HERE!!!!!
                
                if game_values['-INPUT-'] in previousGuesses:
                    game_window['-OUTPUT-'].update(f"You have already guessed this letter. The letters you have guessed are: {previousGuesses}")
                
                elif game_values['-INPUT-'] not in word:
                    game_window['-OUTPUT-'].update(f"{game_values['-INPUT-']} is not in the word. You have {lives - 1} left.")
                    previousGuesses.append(game_values['-INPUT-'])
                    lives -= 1

                else:
                    game_window['-OUTPUT-'].update(f"Nice! The letter {game_values['-INPUT-']} is in the word.")
                    previousGuesses.append(game_values['-INPUT-'])

                # Change the string to a list to fill in the letter of the word
                    wordCompletionAsList = list(wordCompletion)
                    letterIndices = [i for i, letter in enumerate(word) if letter == game_values['-INPUT-']]

                    # Replace the "_" with the chosen letter 
                    for index in letterIndices:
                        wordCompletionAsList[index] = game_values['-INPUT-']
                    wordCompletion = "".join(wordCompletionAsList)

                    if "_" not in wordCompletion:
                        wordGuessed = True

                    game_window['-OUTPUT-'].update(wordCompletion)

            elif len(game_values['-INPUT-']) != 1:
                game_window['-OUTPUT-'].update("You have not entered the right amount of letters. Please only guess one letter per turn.")

            else:
                game_window['-OUTPUT-'].update("You have not entered a letter of the alphabet.")
  
    #Lose    
    if lives == 0:
        game_window['-OUTPUT-'].update(f"Game Over! You have run out of lives. The correct word was {word}" + '\n')

    #Win
    if wordGuessed == True:
        game_window['-OUTPUT-'].update(f"Congratulations! You have correctly guessed the word. The word was {word}. You had {lives} lives remaining.")


    # Finish up by removing from the screen
    game_window.close()

    start_game()





def start_game():
    startingLayout = [[sg.Text("Welcome to the game of Hangman. In this game, you will be presented with a word. Guess the word by entering different letters. You start with 5 lives. \n \
        Please press 'Start' to begin playing. If you do not wish to play, you can exit the program by pressing 'Stop' or by exiting the window.")],
        
        [sg.Button('Start'), sg.Button('Stop'), sg.Button('Replay')]]

        # Create the window
    window = sg.Window('Hangman', startingLayout)

    event, values = window.read()
    
    if event == 'Start':
        window.hide()
        chosenWord = get_Words()
        play_Game(chosenWord)
        window.un_hide()
    
    if event == 'Replay': # Ideally this is dealt through a pop up
        window.hide()
        chosenWord = get_Words()
        play_Game(chosenWord)
        window.un_hide()
        

    if event == sg.WINDOW_CLOSED or event == 'Stop':
        window.close()

    window.close()


def main():
    start_game()
    #while input("Play Again? (Y/N)").upper() == "Y":
     #   chosenWord = get_Words()
      #  play_Game(chosenWord)

if __name__ == "__main__":
    main()



















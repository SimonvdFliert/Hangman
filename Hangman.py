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

    message = f"The length of the word is {len(word)}."
    wordCompletion = "_" * len(word)
    
    layout = [
        [sg.Text("Hello")],
        [sg.Text(message)],
        [sg.Text(wordCompletion)],
        [sg.Input(key='-INPUT-')],
        [sg.Multiline(size=(150,7), key='-OUTPUT-', background_color='light blue', text_color='black')  ],
        
        [sg.Button('Guess'), sg.Button('Quit')]]

        # Create the window
    game_window = sg.Window('Hangman', layout, size= (650, 400))

    while lives > 0 and wordGuessed == False:
   
        # Display and interact with the Window using an Event Loop
        game_event, game_values = game_window.Read(timeout=100)

        # See if user wants to quit or window was closed
        if game_event == sg.WINDOW_CLOSED or game_event == 'Quit':
            lives = 0
            break

        if game_event == 'Guess':
            if len(game_values['-INPUT-']) == 1 and game_values['-INPUT-'].isalpha():
                
                if game_values['-INPUT-'] in previousGuesses:
                    game_window['-OUTPUT-'].update(f"You have already guessed this letter. \n\nThe letters you have guessed are: {previousGuesses}. \n\nThe word: {wordCompletion}")
                    game_window['-INPUT-'].update("")
                
                elif game_values['-INPUT-'] not in word:
                    game_window['-OUTPUT-'].update(f"{game_values['-INPUT-']} is not in the word. \n\nYou have {lives - 1} lives left. \n\nWord: {wordCompletion}")
                    game_window['-INPUT-'].update("")
                    previousGuesses.append(game_values['-INPUT-'])
                    lives -= 1

                else:
                    game_window['-INPUT-'].update("")
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

                    game_window['-OUTPUT-'].update(f"Nice! The letter {game_values['-INPUT-']} is in the word. Word: {wordCompletion} \n\nPrevious Guesses: {previousGuesses}")

            elif len(game_values['-INPUT-']) != 1:
                game_window['-OUTPUT-'].update(f"You have not entered the right amount of letters. Please only guess one letter per turn.\
                    \n\nThe letters you have guessed are: {previousGuesses}. \n\nThe word: {wordCompletion}")
                game_window['-INPUT-'].update("")

            else:
                game_window['-OUTPUT-'].update(f"You have not entered a letter of the alphabet.\
                    \n\nThe letters you have guessed are: {previousGuesses}. \n\nThe word: {wordCompletion}")
                game_window['-INPUT-'].update("")
  
    #Lose    
    if lives == 0:
        lose_message = f"Game Over! You have run out of lives. The correct word was {word}"
        sg.popup("You Lost!", lose_message)
    #Win
    if wordGuessed == True:
        win_message = f"Congratulations! You have correctly guessed the word. The word was {word}. You had {lives} lives remaining."
        sg.popup("You Won", win_message)

    # Finish up by removing from the screen
    game_window.close()

    replay_game()


def start_game():
    startingLayout = [[sg.Text("Welcome to the game of Hangman. In this game, you will be given a word which you will have to guess by entering different letters. You start with 5 lives. \n \
        Please press 'Start' to begin playing. If you do not wish to play, you can exit the program by pressing 'Stop' or by exiting the window.")],
        [sg.Text()],
        [sg.Text()],
        [sg.Button('Start'), sg.Button('Stop')]]

        # Create the window
    window = sg.Window('Hangman', startingLayout)

    event, values = window.read()
    
    if event == 'Start':
        window.close()
        chosenWord = get_Words()
        play_Game(chosenWord)

    if event == sg.WINDOW_CLOSED or event == 'Stop':
        window.close()

    window.close()


def replay_game():
    replayLayout = [
        
        [sg.Text("Thank you for playing Hangman! If you would like to replay, please press the 'Replay' button. You can exit the application by pressing 'Stop' or by closing the window.")],
        [sg.Text()],
        [sg.Text()],
        [sg.Button('Replay'), sg.Button('Stop')]]

    replayWindow = sg.Window('Hangman', replayLayout)

    replay_event, replay_values = replayWindow.read()

    if replay_event == "Replay":
        replayWindow.close() 
        chosenWord = get_Words()
        play_Game(chosenWord)
         
    if replay_event == sg.WINDOW_CLOSED or replay_event == 'Stop':
        replayWindow.close()

    replayWindow.close()    

def main():
    start_game()

if __name__ == "__main__":
    main()



















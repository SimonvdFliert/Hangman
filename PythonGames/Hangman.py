import random

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
    welcomeMessage = f"Welcome to the game of Hangman. In this game, you will be presented with a word. Guess the word by entering different letters. You start with {lives} lives. "
    
    message = f"The length of the word is {len(word)}. Your word is {word}. "
    wordCompletion = "_" * len(word)
    print(welcomeMessage + '\n')
    print(message + '\n')
    print( wordCompletion+ '\n' * 2)

    while lives > 0 and wordGuessed == False:

        #User Input
        chosen_letter = input("Please enter a letter:" ).lower()

        if len(chosen_letter) == 1 and chosen_letter.isalpha():
            
            if chosen_letter in previousGuesses:
                print(f"You have already guessed this letter. The letters you have guessed are: {previousGuesses}")
            
            elif chosen_letter not in word:
                print(f"{chosen_letter} is not in the word. You have {lives - 1} left.")
                previousGuesses.append(chosen_letter)
                lives -= 1

            else:
                print('\n' + f'Nice! The letter {chosen_letter} is in the word.' '\n')
                previousGuesses.append(chosen_letter)

            # Change the string to a list to fill in the letter of the word
                wordCompletionAsList = list(wordCompletion)
                letterIndices = [i for i, letter in enumerate(word) if letter == chosen_letter]

                # Replace the "_" with the chosen letter 
                for index in letterIndices:
                    wordCompletionAsList[index] = chosen_letter
                wordCompletion = "".join(wordCompletionAsList)

                if "_" not in wordCompletion:
                    wordGuessed = True

                print(wordCompletion + '\n')

        elif len(chosen_letter) != 1:
            print("You have not entered the right amount of letters. Please only guess one letter per turn.")

        else:
            print("You have not entered a letter of the alphabet.")

    #Lose    
    if lives == 0:
        print(f"Game Over! You have run out of lives. The correct word was {word}" + '\n')

    #Win
    if wordGuessed == True:
        print(f"Congratulations! You have correctly guessed the word. The word was {word}. You had {lives} lives remaining.")

def main():
    chosenWord = get_Words()
    play_Game(chosenWord)
    while input("Play Again? (Y/N)").upper() == "Y":
        chosenWord = get_Words()
        play_Game(chosenWord)

if __name__ == "__main__":
    main()



















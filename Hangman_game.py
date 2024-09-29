import random  # Import the random module

# List of words
list_of_words = ["apple", "banana", "cherry", "orange", "Horizon","Whisper","Echo","Cascade","fMirage","Ember","Quiver","Lantern","Nexus","Orbit","Fern","Glimmer","Twilight","Tundra","Serene","Velocity","Mosai","Ember","Solstice","Drift"]

# Function to select a random word from the list
def select_random_word(word_list):
    return random.choice(word_list)  # random.choice selects a random word

random_word = select_random_word(list_of_words)
letter_count = len(random_word)
guessed_letters = []

print("\nWelcome to Hangman! Guess the word to save yourself!")
print("If you enter 10 incorrect letters, you will lose the game.")

for i in range(letter_count):
    print("_", end=' ')
    guessed_letters.append("_")

    
def check_letter_in_word(letter, word):
    # Convert both letter and word to lowercase to make the check case-insensitive
    letter = letter.lower()
    word = word.lower()
    # Iterate over each character in the word
    for index, char in enumerate(word):
        if char == letter and guessed_letters[index] == "_":  # Check if the letter matches and hasn't been guessed yet
            guessed_letters[index] = letter
            return True  # If the letter is found, return True
    return False  # If the loop completes without finding the letter, return False

false_count = 0 
correct_count = 0

while false_count <= 10:
        print("\n")
        letter = input("\nPlease enter a letter: ")

        # Check if the input is a single character
        if len(letter) != 1:
            print("Please enter only one character at a time.")
            continue  # Skip the rest of the loop if input is invalid

        # Check the letter against the word
        if check_letter_in_word(letter, random_word):
            print("Correct!")
            correct_count += 1
            for i in guessed_letters:
                print(i, end=' ')
            if correct_count == letter_count:
                print("\nCongratulations! You guessed the word correctly.")
                break  # Exit the loop if the word is guessed correctly
        else:
            print("Incorrect!")
            false_count += 1  # Increment the false count
            if false_count <= 10:
                print(f"You have {10-false_count} incorrect guesses left")


print("You've exceeded 10 incorrect attempts!")



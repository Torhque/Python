#Julio Ureta, CSC 102
user_input = 'nothing'
all_vowels = 'aeiou'
num_words = 0
total_count = 0
choice = 'YES'

while choice.lower() == 'yes':

    # Ask whether the user wants to count consonants or vowels.
    while user_input.lower() != 'vowels' and user_input.lower() != 'consonants':

        user_input = input("Do you want to count consonants, or vowels? ")

        # Error message for when user doesn't enter correct input.
        if user_input.lower() != 'vowels' and user_input.lower() != 'consonants':
            print("Error. Please enter 'consonants' or 'vowels'.")

        # Sets the mode.
        if user_input.lower() == 'vowels':
            vow_mode = True
        else:
            vow_mode = False

    # Ask the user for a word
    word = input("Which word would you like to use? ")

    num_words += 1
    count = 0

    # Count number of vowels in the word.
    if vow_mode == True:
        for letter in word.lower():
            if letter in all_vowels:
                count += 1
                total_count += 1

    # Count number of consonants in word
    if vow_mode == False:
        for letter in word.lower():
            if letter not in all_vowels:
                count += 1
                total_count += 1
                
    # Displays number of vowels or consonants in the word.            
    print("Number of", user_input.lower(), "in word:", str(count))

    # Calculate average number of vowels or consonants per word.
    average = total_count/num_words

    # Ask if the user wants to enter another word.
    choice = input("Is another word available (yes/no)? ")

    # Error message when user doesn't enter correct input.
    while choice.lower() != 'yes' and choice.lower() != 'no':
        print("Error. Please enter 'yes' or 'no'.")

        choice = input("Is another word available (yes/no)? ")

# Display average number of vowels or consonants per word.
print("Average number of", user_input.lower(), "per word:", average)
print("Done.")

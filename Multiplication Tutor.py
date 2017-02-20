# Julio Ureta CSC102
from random import randint

user_problems = -1
index = 1
tries = 0

# Define the function that will display the problem.
def display_problem(factor_one, factor_two):
        print("What is", factor_one, "*", factor_two)
        
while int(user_problems) < 1 or int(user_problems) > 10:
    
    # Ask the user how many problems they want to solve. 
    user_problems = input("How many problems do you want to solve? ")

    #Error message for when user doesn't enter correct input.
    if int(user_problems) < 1 or int(user_problems) > 10:
        print("Error. Please enter any number between 1 and 10 (inclusive).")
        
while index <= int(user_problems):

    # Initialize two random factors to use later.
    first_factor = randint(0, 12)
    second_factor = randint(0, 12)

    # Call the function to display the problem, then ask the user for their answer.
    display_problem(first_factor, second_factor)
    user_answer = input("Answer -->")

    # Store the correct answer to the problem to compare later.
    real_answer = first_factor * second_factor

    # Check to see if the user's input is correct, and increment number of tries.
    if int(user_answer) == real_answer:
        print("Good job!")
        tries += 1

    while int(user_answer) != real_answer:
        
        print("Sorry, incorrect.")
        tries += 1

        # Give hint to the user if their answer is too low or too high.
        if int(user_answer) < real_answer:
            print("Too low.")
        else:
            print("Too high.")
        # Display the problem again by calling the function once more, then asking for another answer.    
        display_problem(first_factor, second_factor)
        user_answer = input("Answer -->")

        # Check to see if new answer is correct.
        if int(user_answer) == real_answer:
            print("Good job!")
            tries += 1
    index += 1
# Calculate and display the average number of tries the user took to answer the problem(s).    
print("Average number of tries:", tries/int(user_problems))

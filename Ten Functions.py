# Julio Ureta CSC102

# 1. A function that displays your name and your major.
def display_name_and_major(name, major):
    
    print("Name:", name)
    print("Major:", major)

# 2. A function that prompts the user to enter their age and returns the user's input as an int
def get_age():
    
    user_age = input("Gimme your age: ")
    return print(int(user_age))

# 3. A function that takes one argument - the argument will be a name that is a string. Then displays a message:
def hello_user(user_name):
    
    print("Hello", user_name + "!")

# 4. A function that takes an integer argument called number and returns the inverse of that number.
def inverse_integer(number):
    
    number = int(number)
    inverse = -(number)
    return print(inverse)

# 5. A function that takes an integer argument called count and a string argument called message.
#    The function will display the message <count> times.
def string_count(count, message):
    
    while count > 0:
        print(message)
        count -= 1

# 6. A function called get_biggest that takes two int arguments called num1 and num2.
#    The function will return the largest of the two argument values. If the arguments are equal,
#    then it will return the first argument value.
def get_biggest(num1, num2):
    
    if num1 > num2:
        return print(num1)
    elif num1 == num2:
        return print(num1)
    else:
        return print(num2)

# 7. A function that takes a string argument and counts,
#    and returns the number of capital letters in the argument string.
def capital_count(string):

    count = 0
    alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in string:
        if letter in alphas:
            count += 1
    return count

# 8. A function that takes three int arguments and returns the middle value. 
def get_middle_value(int1, int2, int3):
    
    if (int1 > int2 and int1 < int3) or (int1 < int2 and int1 > int3) or (int1 == int2 or int1 == int3):
        return int1
    elif (int2 > int1 and int2 < int3) or (int2 < int1 and int2 > int3):
        return int2
    else:
        return int3
    

# 9. A function that takes two string arguments and returns a string with only the characters that
#    are in both of the argument strings. There should be no duplicate characters in the return value.
def get_common_letters(string1, string2):

    chars = ""
    for letter in string1:
        if letter in string2:
            if letter not in chars: #Here is where I revised the code (:
                chars += letter
    return print(chars)

# 10. A function that calls each of the functions above,
#     but prompts the user for necessary variable(s).
def call_all_functions_above():

    # Ask the user for their name and major.
    name_of_user = input("What is your name? ")
    major_of_user = input("What is your major? ")

    # Display their name and major.
    display_name_and_major(name_of_user, major_of_user)

    # Get the user's age using the function.
    get_age()

    # Say hello to the user by calling the function.
    hello_user(name_of_user)

    # Prompt the user for an integer, then return the inverse of it by using the function.
    user_integer = input("Please enter an integer you want to get the inverse of: ")
    inverse_integer(user_integer)

    # Prompt the user for a word, then call the function.
    user_word = input("Enter a word, any word: ")
    user_count = input("How many times do you want to display this word? ")
    user_count = int(user_count)
    
    string_count(user_count, user_word)

    # Ask the user for two integers, then call the function to display the bigger number.
    user_num1 = input("Enter a nonnegative whole number: ")
    user_num1 = int(user_num1)

    user_num2 = input("Enter another nonnegative whole number: ")
    user_num2 = int(user_num2)

    print("The larger number of the two is:")
    get_biggest(user_num1, user_num2)
    
    # Prompt the user to enter a word, then call the function to count the capitals.
    user_string = input("Enter a word or sentence: ")
    print("There is/are", capital_count(user_string), "capital letter(s) in there.")
    
    # Ask the user for three numbers, then display the middle value using the function.
    user_first_number = input("Enter your first number: ")
    user_first_number = int(user_first_number)

    user_second_number = input("Enter your second number: ")
    user_second_number = int(user_second_number)

    user_third_number = input("Enter your third number: ")
    user_third_number = int(user_third_number)

    print("The middle value is:", get_middle_value(user_first_number, user_second_number, user_third_number))

    # Prompt the user for two words,
    # then display the letters that are shared between them by calling the function.
    user_string1 = input("Enter one word: ")
    user_string2 = input("Enter another word: ")

    print("Those words share the letters below.")
    get_common_letters(user_string1, user_string2)

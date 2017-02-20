# Julio Ureta CSC102

# 1. Function that takes a list of any size as an argument, and returns a list 
#    where all adjacent, equal elements have been reduced to a single element.
def remove_adjacent_equal_elements(a_list):
    reduced_list = []
    element = 1

    # Append the first first element
    reduced_list.append(a_list[0])

    # Compare each element to the previous one to make sure
    # duplicates aren't adjacent
    while element < len(a_list):
        if a_list[element] != a_list[element - 1]:
            reduced_list.append(a_list[element])
        element += 1

    return reduced_list

# 2. Function that takes a list of numbers of any size as an argument and
#    returns true if the list is sorted or false otherwise.
def check_if_sorted(a_list):
    semi_sorted_list = []
    index = 1

    # Append the first first element
    semi_sorted_list.append(a_list[0])

    # Check to see if the element at said index is greater than
    # the previous element, then add it to the semi-sorted list.
    while index < len(a_list):
        if a_list[index] > a_list[index - 1]:
            semi_sorted_list.append(a_list[index])
        index += 1           

    # Compare the original list to the semi-sorted list, and
    # return True if they match. Otherwise, return False.
    if a_list == semi_sorted_list:
        return True
    else:
        return False

# 3. Function that takes a list of numbers of any size as an argument,
#    and returns the sum of the numbers.
def return_sum_of_values(a_list):
    total = 0

    # Go through each number in the list,
    # and then add it to the total. 
    for number in a_list:
        total += number
    
    return total

# 4. Write a function that takes a list of any type and size as an argument,
#    and returns a list where the elements are in reverse list order.
def reverse_list(a_list):
    reversed_list = []
    index = len(a_list) - 1

    # Start with the last element in the list, and then
    # append each previous element till the remaining element. 
    while index >= 0:
        reversed_list.append(a_list[index])
        index -= 1

    return reversed_list

# 5. Function that takes two sorted lists as arguments, and returns a
#    single sorted list.
def combine_sorted_lists(list_one, list_two):
    combined_sorted_lists = []

    # Append all the elements in the first list to the
    # empty list.
    for element in list_one:
        combined_sorted_lists.append(element)

    # Append all the elements in the second list on top
    # of the previous list.
    for element in list_two:
        combined_sorted_lists.append(element)

    # Sort the final, combined list.
    combined_sorted_lists.sort()
    
    return combined_sorted_lists

# 6. Function that demonstrates and tests each of the above functions.
def demo_and_test_functions():
    # Call function 1.
    print("My first function will reduce [2,3,3,4,3,3] to a list where" +
          " all adjacent, equal elements are reduced to one element.")
    
    print("Like this:", remove_adjacent_equal_elements([2,3,3,4,3,3]))

    print("")

    # Call function 2.
    print("My second function will return False if the list is not " +
          "sorted, but will return True if is already sorted.")

    print("Like this, [0, 2, 4, 3] returns:", check_if_sorted([0, 2, 4, 3]))
    print("And this, [0,3,6,8] returns:", check_if_sorted([0,3,6,8]))

    print("")


    # Call function 3.
    print("My third function will return the sum of the elements in " +
          "the list.")
    print("Like this, [2,5,6,10] returns: ", return_sum_of_values([2,5,6,10]))

    print("")

    # Call function 4.
    print("My fourth function returns a list in its reverse order.")
    print("Like this, ['wow', 'whoa', 'neat'], returns: ",
          reverse_list(['wow', 'whoa', 'neat']))

    print("")

    # Call function 5.
    print("My fifth function takes two sorted lists, and returns a" +
          " single sorted list.")
    print("Like this, [1, 5, 9] and [3, 7, 11] returns: ",
          combine_sorted_lists([1, 5, 9], [3, 7, 11]))
    

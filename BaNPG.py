# Define the function "number_pattern" with the parameter set as "n"
def number_pattern(n):
    # Checks if the value inserted in the parameter is an integer
    if not isinstance(n, int):
        # Returns a string clarifying that the value but be an integer value
        return 'Argument must be an integer value.'
    # Check if the integer is less than 1
    elif n < 1:
        # Returns a string clarifying that the value but be greater than 0
        return 'Argument must be an integer greater than 0.'

    # Create a variable with an empty string in which
    # It stores the sequence of numbers
    numbers = ""
    # For loop in which we create a sequence of numbers starting from 1 and ending
    # at the number inserted, in this case, 3 and 11.
    # "num" is each number within the sequence.
    # Adding a one at the end of n (Example: n+1) will result later on in "1 2 3 4 "
    # Additional whitespace is not allowed. It is why str(n) is added at the return.
    for num in range(1, n):
        # " " is the space thats added ad the end of each string number
        # str(num) turns each numbers from the sequence of numbers into strings
        # The augmented assignment operator (+=) is used to add the string numbers
        # Within the empty string variable from above
        numbers += str(num) + " "
    # Return numbers (with new values which is the sequence of numbers in strings)
    # and add the input parameter at the end to include the input
    return numbers + str(n)


# Call the function within the print statement with an arguement of 4
print(number_pattern(4))
# Call the function within the print statement with an arguement of 12
print(number_pattern(12))

## sum of digits function 
def sumofdigits():
    # Prompt the user to input a number for which the sum of digits will be calculated
    num = int(input("This is the sum of digits function - Enter a number: "))
    # Convert the number to a string and iterate over each digit, converting it back to an integer and summing them up
    return sum(int(digit) for digit in str(num))

## palindrome function
def ispal():
    # Prompt the user to input a number to check if it's a palindrome
    num = int(input("This is the palindrome function - Enter a number: "))
    # Convert the number to a string and check if it's equal to its reverse
    return str(num) == str(num)[::-1]
s

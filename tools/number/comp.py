
## sum of digits function 
def sumofdigits():
    num = int(input(" this is  sum of digits func - Enter a number: "))
    return sum(int(digit) for digit in str(num))
## palindrom function
def ispal():
    num = int(input("this is  oalindrom func - Enter a number: "))
    return str(num) == str(num)[::-1]
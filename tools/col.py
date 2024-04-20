## zip function
def myzip():
    # Prompt the user to input elements for the first list separated by space
    list1 = input("Enter elements for the first list separated by space: ").split()
    # Prompt the user to input elements for the second list separated by space
    list2 = input("Enter elements for the second list separated by space: ").split()
    
    ## Convert input strings to appropriate data types 
    # Convert each element in list1 to the appropriate data type using eval()
    list1 = [eval(element) for element in list1]
    # Convert each element in list2 to the appropriate data type using eval()
    list2 = [eval(element) for element in list2]

    # Use the zip() function to pair elements from list1 and list2 together
    # and return a list of tuples containing these pairs
    return list(zip(list1, list2))


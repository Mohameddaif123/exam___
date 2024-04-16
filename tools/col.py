
## zip function
def myzip():
    list1 = input("Enter elements for the first list separated by space: ").split()
    list2 = input("Enter elements for the second list separated by space: ").split()
    
    ## Convert input strings to appropriate data types 
    list1 = [eval(element) for element in list1]
    list2 = [eval(element) for element in list2]

    return list(zip(list1, list2))

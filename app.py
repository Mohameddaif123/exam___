# Import necessary modules and functions
from tools.number import simp, comp 
from tools import col

# Define a function to test functions in the simp module
def test_simp_module():
    print("Testing simp module:")
    # Call the add and subtract functions from the simp module
    result_add = simp.add()
    result_subtract = simp.subtract()

    # Print the results of the add and subtract functions
    print("Add:", result_add)
    print("Subtract:", result_subtract)

# Define a function to test functions in the comp module
def test_comp_module():
    print("Testing comp module:")
    # Call the sumofdigits and ispal functions from the comp module
    result_sum_digits = comp.sumofdigits()
    result_is_palindrome = comp.ispal()

    # Print the results of the sumofdigits and ispal functions
    print("Sum of Digits:", result_sum_digits)
    print("Is Palindrome:", result_is_palindrome)

# Define a function to test functions in the col module
def test_col_module():
    print("Testing col module:")
    # Call the myzip function from the col module
    result_zip = col.myzip()

    # Print the result of the myzip function
    print("Zip:", result_zip)

# Define the main function
def main():
    simp_called = False  # Flag to track if a function in simp module is called

    try:
        # Test functions in simp module
        test_simp_module()
        simp_called = True  # Set the flag to True indicating that a function in simp module was called

        # Test functions in comp module
        if not simp_called:
            raise Exception("Functions in comp module cannot be called before calling at least one function in simp module.")
        test_comp_module()

        # Test functions in col module
        test_col_module()
        

    except Exception as e:
        # Handle any exceptions that occur during testing
        print(f"Exception: {e}")

# Entry point of the script
if __name__ == "__main__":
    # Call the main function
    main()
    # Print a message indicating that tests are done
    print("Tests are done")

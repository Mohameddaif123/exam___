
from tools.number import simp, comp 
from tools import col

def test_simp_module():
    print("Testing simp module:")
    result_add = simp.add()
    result_subtract = simp.subtract()

    print("Add:", result_add)
    print("Subtract:", result_subtract)

def test_comp_module():
    print("Testing comp module:")
    result_sum_digits = comp.sumofdigits()
    result_is_palindrome = comp.ispal()

    print("Sum of Digits:", result_sum_digits)
    print("Is Palindrome:", result_is_palindrome)

def test_col_module():
    print("Testing col module:")
    result_zip = col.myzip()

    print("Zip:", result_zip)

def main():
    simp_called = False  ## Flag to track if a function in simp module is called

    try:
        ## Test functions in simp module
        test_simp_module()
        simp_called = True  # Set the flag to True

        ## Test functions in comp module (should raise an exception if simp module is not called)
        if not simp_called:
            raise Exception("Functions in comp module cannot be called before calling at least one function in simp module.")
        test_comp_module()

        ## Test functions in col module
        test_col_module()
        

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()
    print("tests are done")
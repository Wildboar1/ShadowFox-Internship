def check_pi_type():
    """
    1. Stores pi as 22/7 and checks its data type.
    """
    print("--- 1. Variable pi and Data Type Check ---")
    
    # 1.1 Store 22/7 in a variable named pi
    pi = 22 / 7
    
    # Check the data type of the variable pi
    data_type_pi = type(pi)
    
    print(f"The value of pi is: {pi}")
    print(f"The data type of pi is: {data_type_pi}")
    print("Observation: The type is <class 'float'> because division in Python 3+ results in a float.")
    
    print("-" * 40)

def check_reserved_keyword():
    """
    2. Demonstrates why 'for' cannot be used as a variable name.
    """
    print("--- 2. Reserved Keyword Check ('for') ---")
    
    # 1.2 Create a variable called for and assign it a value 4
    # The actual line 'for = 4' would raise a SyntaxError.
    
    print("Attempting to use 'for' as a variable name...")
    try:
        # Note: We comment out the actual problematic line to allow the script to run, 
        # and demonstrate the error with the print statement.
        # for = 4 
        print("If 'for = 4' were uncommented, a SyntaxError would occur.")
    except SyntaxError as e:
        # This block won't execute because the problematic line is commented, 
        # but it shows the intent of error handling.
        print(f"Error encountered: {e}") 
    
    print("Reason: **'for' is a reserved keyword** in Python and cannot be used as a variable name.")
    
    print("-" * 40)

def calculate_simple_interest():
    """
    3. Calculates Simple Interest using the formula P * R * T / 100.
    """
    print("--- 3. Simple Interest Calculation ---")
    
    # 1.3 Store P, R, T in variables
    principal = 1000  # P (Principal Amount)
    rate = 5          # R (Rate of Interest)
    time = 3          # T (Time in years)
    
    # Calculate Simple Interest
    # Formula: Simple Interest = P x R x T / 100
    simple_interest = (principal * rate * time) / 100
    
    print(f"Principal (P): ${principal}")
    print(f"Rate (R): {rate}%")
    print(f"Time (T): {time} years")
    print(f"Calculated Simple Interest: **${simple_interest:.2f}**")
    
    print("-" * 40)

# Main execution block
if __name__ == "__main__":
    check_pi_type()
    check_reserved_keyword()
    calculate_simple_interest()
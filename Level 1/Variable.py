def check_pi_type():

    print("--- 1. Variable pi and Data Type Check ---")
    pi = 22 / 7
    data_type_pi = type(pi)
    
    print(f"The value of pi is: {pi}")
    print(f"The data type of pi is: {data_type_pi}")
    print("Observation: The type is <class 'float'> because division in Python 3+ results in a float.")
    
    print("-" * 40)

def check_reserved_keyword():

    print("--- 2. Reserved Keyword Check ('for') ---")
    print("Attempting to use 'for' as a variable name...")
    try:

        print("If 'for = 4' were uncommented, a SyntaxError would occur.")
    except SyntaxError as e:
     print(f"Error encountered: {e}") 
    
    print("Reason: **'for' is a reserved keyword** in Python and cannot be used as a variable name.")
    
    print("-" * 40)

def calculate_simple_interest():
    print("--- 3. Simple Interest Calculation ---")
    
    principal = 1000  # P (Principal Amount)
    rate = 5          # R (Rate of Interest)
    time = 3          # T (Time in years)
    
    # Formula: Simple Interest = P x R x T / 100
    simple_interest = (principal * rate * time) / 100
    
    print(f"Principal (P): ${principal}")
    print(f"Rate (R): {rate}%")
    print(f"Time (T): {time} years")
    print(f"Calculated Simple Interest: **${simple_interest:.2f}**")
    
    print("-" * 40)

if __name__ == "__main__":
    check_pi_type()
    check_reserved_keyword()
    calculate_simple_interest()
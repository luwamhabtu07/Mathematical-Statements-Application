# logic_app.py

def get_user_input():
    while True:
        try:
            a = int(input("Enter value for A (0 or 1): "))
            b = int(input("Enter value for B (0 or 1): "))
            if a in [0, 1] and b in [0, 1]:
                return a, b
            else:
                print("Please enter only 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter numeric 0 or 1.")

def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_not(a):
    return 1 if a == 0 else 0

def logical_implication(a, b):
    return 1 if (not a) or b else 0

def logical_biconditional(a, b):
    return 1 if a == b else 0

def display_results(a, b):
    print("\nResults:")
    print(f"A AND B: {logical_and(a, b)}")
    print(f"A OR B: {logical_or(a, b)}")
    print(f"NOT A: {logical_not(a)}")
    print(f"A -> B (Implication): {logical_implication(a, b)}")
    print(f"A <-> B (Biconditional): {logical_biconditional(a, b)}\n")

def generate_truth_table():
    print("\n=== Truth Table ===")
    print("A B | AND OR NOT A Implication Biconditional")
    print("-------------------------------------------")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"{a} {b} |  {logical_and(a, b)}   {logical_or(a, b)}   {logical_not(a)}      {logical_implication(a, b)}            {logical_biconditional(a, b)}")

def main():
    print("=== Logical Operations App ===")
    while True:
        print("\nChoose an option:")
        print("1. Evaluate Logical Operations for A and B")
        print("2. Generate Full Truth Table")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            a, b = get_user_input()
            display_results(a, b)
        elif choice == '2':
            generate_truth_table()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

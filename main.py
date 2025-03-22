import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_number(a, b):
    logging.info(f"Adding {a} and {b}")
    return a + b

def sub_number(a, b):
    logging.info(f"Subtracting {a} and {b}")
    return a - b

def mul_number(a, b):
    logging.info(f"Multiplying {a} and {b}")
    return a * b

def div_number(a, b):
    logging.info(f"Dividing {a} and {b}")
    return a / b

if __name__ == "__main__":
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operations = {
        "1": add_number,
        "2": sub_number,
        "3": mul_number,
        "4": div_number
    }
    
    choice = input("Choose an operation: ")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    if choice in operations:
        result = operations[choice](a, b)
        print(result)
    else:
        print("Invalid choice")
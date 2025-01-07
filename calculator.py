
# Importing the operation functions from other files
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    if choice == '1':
        print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()

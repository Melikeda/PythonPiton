def main():
    print("Simple calculator")
    print("--------------------")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the action you want to make (+, -, *, /): ")
    
    result = None
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Dividing by zero!")
            return
    else:
        print("Error: Invalid operation!")
        return
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

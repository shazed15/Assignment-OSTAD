print("Project-1(Simple Calculator)")
operation = print("First you have to choose your Operation -\nFor addition(Press 1),\nFor subtraction(Press 2), \nFor multiplication(Press 3), \nFor division(Press 4), \nFor modulus(Press 5): ")
operation = input("Enter choice (1/2/3/4/5):")
operation = float(operation)
operation = round(operation, 2)
arg1 = input("Enter Your First Argument: ")
arg1 = float(arg1)
arg1 = round(arg1, 2)
arg2 = input("Enter Your Second Argument: ")
arg2 = float(arg2)
arg2 = round(arg2, 2)
def simple_calc():
    if operation == 1:
        print("Addition: " ,str(arg1), "+", str(arg2) ,"=" ,arg1+arg2 )
    elif operation == 2:
        print("Substraction: ",str(arg1), "-", str(arg2) ,"=" ,arg1-arg2)
    elif operation == 3:
        print("Multiplication: " ,str(arg1), "*", str(arg2) ,"=" ,arg1*arg2)
    elif operation == 4:
        try:
            print("Divition: " ,str(arg1), "/", str(arg2) ,"=" ,arg1/arg2)
        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero")
    elif operation == 5:
        print("Modulous: ",str(arg1), "%", str(arg2) ,"=" ,arg1%arg2)
simple_calc()

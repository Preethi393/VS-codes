try:
    userInput = input("Enter Any Number: ")
    result = 100/int(userInput)
    print("Result: ", result)
except ValueError:
    print("Not a valid number, please enter only numbers")

except ZeroDivisionError:
    print("Please, Enter a number greater than zero")
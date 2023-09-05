try:
    fh = open("ExceptionHandling.txt", 'w')
    fh.write("Opening the file. \n")

    userInput = input("Enter Any Number: ")
    fh.write("The user has entered a number {}\n".format(userInput))

    result = 100/int(userInput)
    fh.write("The final result is {}\n".format(result))

    # fh.write("Closing the file \n")
    # fh.close()


except ValueError:
    print("Not a valid number, please enter only numbers")

except ZeroDivisionError:
    print("Please, Enter a number greater than zero")

finally:
    fh.write("Closing the file \n")
    fh.close()
    
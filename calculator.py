def addition(first_number, second_number):
    return first_number + second_number


def subtraction(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


def power(first_number, second_number):
    return first_number ** second_number
def hacky_stuff(first_number, operator, second_number):
    try:
        return int(eval(str(first_number)+operator+str(second_number)))
    except Exception as e:
        return "Invalid Input!"


def calculate(first_number, operator, second_number):
    result = "Invalid Input!"
    if operator == "+":
        result = addition(first_number, second_number)
    elif operator == "-":
        result = subtraction(first_number, second_number)
    elif operator == "*":
        result = multiply(first_number, second_number)
    elif operator == ":":
        result = divide(first_number, second_number)
    elif operator == "**":
        result = power(first_number, second_number)
    else:
        result = hacky_stuff(first_number, operator, second_number)
    print("Result is: ", result)


def receive_input():
    val = input().split()
    first_number = int(val[0])
    operator = val[1]
    second_number = int(val[2])
    calculate(first_number, operator, second_number)


if __name__ == "__main__":
    print("Welcome to the simplest calculator ever(maybe)!")
    print("Input two values you wanted to calculate and its operator in this following format:")
    print("first_number operator second_number")
    print("Example: ")
    print("123 * 232")
    receive_input()



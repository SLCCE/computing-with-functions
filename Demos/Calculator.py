# Adds value1 and value2 then returns the result
def add (value1, value2):
    return value1 + value2

# Subtracts value2 from value1 and returns the result
def subtract (value1, value2):
    return value1 - value2

# Multiplies value1 by value2 and returns the result
def multiply (value1, value2):
    return value1 * value2

# Divides value1 by value2 and returns the result
def divide (value1, value2):
    if (value2 == 0):
        return 'Cannot divide by 0'
    return value1 / value2

# Divides value1 by value2 and returns the floor of the result
def floor_divide (value1, value2):
    if (value2 == 0):
        return 'Cannot divide by 0'
    return value1 // value2

# Returns the remainder of the result of value1 divide by value2
def modulus (value1, value2):
    return value1 % value2

# Returns the result of value1 raised to the power of value2
def exponent (value1, value2):
    return value1 ** value2

# Converts value to an int or float returns False if thats not possible
def convert_value_number (value):
    number = False
    # try to convert value to int
    try:
        number = int(value)
    except ValueError:
        # try to convert value to float
        try:
            number = float(value)
        except ValueError:
            # value cannot be expressed as an int or float
            return False
    return number

# Evaluates expression in the order of [exponents], [multiply, divide, floor divide, modulus], [add, subtract]
# Returns the evaluated value or an error message
def evaluate_expression (expression):
    # Count number of all operators
    addCount = expression.count('+')
    subtractCount = expression.count('-')
    multiplyCount = expression.count('*')
    divideCount = expression.count('/')
    floorDivideCount = expression.count('//')
    modulusCount = expression.count('%')
    exponentCount = expression.count('^')
    # Beacuse the function reduces the length of the expression list the exit condition will be when expression has only one term
    while len(expression) > 1:
        # Check exponent first, because it has a higher order of operations than other operators recognized by this calculator
        if exponentCount > 0:
            # Find earliest index of '^', use the term right before and after to as value1 and value2 to be passed to function
            operatorIndex = expression.index('^')
            value1 = expression[operatorIndex - 1]
            value2 = expression[operatorIndex + 1]

            # Replace the terms evaluated terms with the result and decrement the count
            expression[operatorIndex - 1] = exponent(value1, value2)
            expression.pop(operatorIndex)
            expression.pop(operatorIndex)
            exponentCount -= 1

        # Check multiple counts of the same order of operations
        if multiplyCount > 0 or divideCount > 0 or floorDivideCount > 0 or modulusCount > 0:
            # Set default indicies to infinity to avoid considering operators that dont exist
            multiplyIndex = float('inf')
            divideIndex = float('inf')
            floorDivideIndex = float('inf')
            modulusIndex = float('inf')
            # Find earliest index of operators if it exists
            if multiplyCount > 0:
                multiplyIndex = expression.index('*')
            if divideCount > 0:
                divideIndex = expression.index('/')
            if floorDivideCount > 0:
                floorDivideIndex = expression.index('//')
            if modulusCount > 0:
                modulusIndex = expression.index('%')

            # Find index of operator that occurs the earliest
            minIndex = min([multiplyIndex, divideIndex, floorDivideIndex, modulusIndex])

            value1 = expression[minIndex - 1]
            value2 = expression[minIndex + 1]
            
            # Call the repective function if the lowest index matches the operator's index, and decrements the count
            if minIndex == multiplyIndex:
                expression[minIndex - 1] = multiply(value1, value2)
                multiplyCount -= 1

            elif minIndex == divideIndex:
                result = divide(value1, value2)
                # Check for error string
                if type(result) is str:
                    return result
                expression[minIndex - 1] = result
                divideCount -= 1

            elif minIndex == floorDivideIndex:
                result = floor_divide(value1, value2)
                # Check for error string
                if type(result) is str:
                    return result
                expression[minIndex - 1] = result
                floorDivideCount -= 1

            else:
                expression[minIndex - 1] = modulus(value1, value2)
                modulusCount -= 1

            # Remove evaluated terms
            expression.pop(minIndex)
            expression.pop(minIndex)

        # Check multiple counts of the same order of operations
        if addCount > 0 or subtractCount > 0:
            # Set default indicies to infinity to avoid considering operators that dont exist
            addIndex = float('inf')
            subtractIndex = float('inf')

            # Find earliest index of operators
            if addCount > 0:
                addIndex = expression.index('+')
            if subtractCount > 0:
                subtractIndex = expression.index('-')

            # Find index of operator that occurs the earliest
            minIndex = min([addIndex, subtractIndex])

            value1 = expression[minIndex - 1]
            value2 = expression[minIndex + 1]

            # Call the repective function if the lowest index matches the operator's index, and decrements the count
            if minIndex == addIndex:
                expression[minIndex - 1] = add(value1, value2)
                addCount -= 1
            else:
                expression[minIndex - 1] = subtract(value1, value2)
                subtractCount -= 1
            
            # Remove evaluated terms
            expression.pop(minIndex)
            expression.pop(minIndex)
    #Return reduced result
    return expression[0]

# Reads user input of expression and checks that its in the proper form, calls evaluate_expression
def calculator ():
    # Set of operators that the calculator recognizes
    valid_operators = ['+', '-', '*', '/', '//', '%', '^']
    # Continually prompts user for an expression to evaluate
    while (True):
        # error flag
        error = False
        # Reads user input, strips excess whitespace, and splits each term into an entry in a list
        expression = input('Enter expression: ').strip().split()
        # Check that each term is a legal symbol or number
        for index, term in enumerate(expression):
            # Check for quit command
            if term == 'quit' or term == 'q':
                exit(0)
            # Check that expression does not start with an operator
            if index == 0 and expression[index] in valid_operators:
                print(f"Expression cannot start with: {expression[index]}")
                error = True
                break

            convert_result = convert_value_number(term)
            # Check if term is a number
            if type(convert_result) is int or type(convert_result) is float:
                expression[index] = convert_result
                # Check that two numbers are not side by side (eg 5 5 + 5)
                if index != len(expression) - 1 and expression[index + 1] not in valid_operators:
                    print(f"Expression contains an illegal sequence: {expression[index]} {expression[index + 1]}")
                    error = True
                    break
            # Term is not a number, now check if its not a valid operator
            elif term not in valid_operators:
                print(f"Expression contains an illegal term: {term}")
                error = True
                break
            else:
                # Term is a valid operator, now check that next term is not also an operator (eg 5 + + 5) if it exists
                if index != len(expression) - 1 and expression[index + 1] in valid_operators:
                    print(f"Expression contains an illegal sequence: {expression[index]} {expression[index + 1]}")
                    error = True
                    break
        if error:
            continue
        # Print result from evaluated expression
        print(evaluate_expression(expression))


print('''Welcome to the Calculator
There are some rules for using this calculator:
\t1. Each term must have spaces separating terms (eg 5 + 5 not 5+5)
\t2. This calculator only recognizes numbers and this set of symbols (+, -, *, /, //, %, ^)
\t3. Type \'q\' or \'quit\' to exit the program''')

calculator()

exit(0)
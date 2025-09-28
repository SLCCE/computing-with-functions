import random
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from Calculator import *

# Array to hold random values to use in tests
randListNums = []
# Populates randListNums with 20 random numbers
# Does not use 0 to avoid tests trying to divide by zero
for _ in range(20):
    randListNums.append(random.randint(1, 999))

# Runs all tests 
def testAll ():
    # Exercise tests
    testAdd()
    testSubtract()
    testMultiply()
    testDivide()

    # Bonus Tests:
    testExponent()
    testModulus()
    testFloorDivide()

# Tests the implemented add function by calling student function on two random values 20 times. Compares
# student result to expected value. Will print which operation failed or expection messages if they occur.
# Including when the function is not implemented.
def testAdd ():
    try:
        for val in randListNums:
            randVal = random.randint(1, 999)
            studentResult = add(val, randVal)
            expectedResult = val + randVal
            if studentResult != expectedResult:
                print(f"{val} + {randVal} resulted in {studentResult} when it should be {expectedResult}")
                return
        print("Addition tests Pass!")
    except Exception as e:
        print(e)

# Tests the implemented subtract function by calling student function on two random values 20 times. Compares
# student result to expected value. Will print which operation failed or expection messages if they occur.
# Including when the function is not implemented.
def testSubtract():
    try:
        for val in randListNums:
            randVal = random.randint(1, 999)
            studentResult = subtract(val, randVal)
            expectedResult = val - randVal
            if studentResult != expectedResult:
                print(f"{val} - {randVal} resulted in {studentResult} when it should be {expectedResult}")
                return
        print("Subtraction tests Pass!")
    except Exception as e:
        print(e)

# Tests the implemented multiply function by calling student function on two random values 20 times. Compares
# student result to expected value. Will print which operation failed or expection messages if they occur.
# Including when the function is not implemented.
def testMultiply ():
    try:
        for val in randListNums:
            randVal = random.randint(1, 999)
            studentResult = multiply(val, randVal)
            expectedResult = val * randVal
            if studentResult != expectedResult:
                print(f"{val} * {randVal} resulted in {studentResult} when it should be {expectedResult}")
                return
        print("Multiplication tests Pass!")
    except Exception as e:
        print(e)

# Tests the implemented divide function by calling student function on two random values 20 times. Compares
# student result to expected value. Will print which operation failed or expection messages if they occur.
# Including when the function is not implemented.
def testDivide ():
    try:
        for val in randListNums:
            randVal = random.randint(1, 999)
            studentResult = divide(val, randVal)
            expectedResult = val / randVal
            if studentResult != expectedResult:
                print(f"{val} / {randVal} resulted in {studentResult} when it should be {expectedResult}")
                return
        print("Division tests Pass!")
    except Exception as e:
        print(e)


# ===================================================
#          Bonus Tests:
# ===================================================

# Tests the implemented exponent function by calling student function on two random values 20 times. Compares
# student result to expected value. Will print which operation failed or expection messages if they occur.
# Does nothing if the function does not exists, but will run tests if the student has implemented the function
def testExponent ():
    try:
        for val in randListNums:
            randVal = random.randint(1, 999)
            studentResult = exponent(val, randVal)
            expectedResult = val ** randVal
            if studentResult != expectedResult:
                print(f"{val} ^ {randVal} resulted in {studentResult} when it should be {expectedResult}")
                return
        print("Exponentiation tests Pass!")
    except NameError:
        return
    except Exception as e:
        print(e)

# Tests the implemented modulus function by calling student function on two random values 20 times. Compares
# student result to expected value. Will print which operation failed or expection messages if they occur.
# Does nothing if the function does not exists, but will run tests if the student has implemented the function
def testModulus ():
    try:
        for val in randListNums:
            randVal = random.randint(1, 999)
            studentResult = modulus(val, randVal)
            expectedResult = val % randVal
            if studentResult != expectedResult:
                print(f"{val} % {randVal} resulted in {studentResult} when it should be {expectedResult}")
                return
        print("Modular Arithmetic tests Pass!")
    except NameError:
        return
    except Exception as e:
        print(e)

# Tests the implemented floor_divide function by calling student function on two random values 20 times. Compares
# student result to expected value. Will print which operation failed or expection messages if they occur.
# Does nothing if the function does not exists, but will run tests if the student has implemented the function
def testFloorDivide ():
    try:
        for val in randListNums:
            randVal = random.randint(1, 999)
            studentResult = floor_divide(val, randVal)
            expectedResult = val // randVal
            if studentResult != expectedResult:
                print(f"{val} // {randVal} resulted in {studentResult} when it should be {expectedResult}")
                return
        print("Floor Divide tests Pass!")
    except NameError:
        return
    except Exception as e:
        print(e)


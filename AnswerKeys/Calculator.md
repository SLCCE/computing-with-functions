# Exercise

We want to implement the subtract, multiply and divide functions. All of the functions take in 2 parameters, you can name these whate ever you want. For this example I will have the paramerters match the add function.
```python
def example (value1, value2):
    return
```

## Subtract x - y
The function has two parameters but it doesnt do anything with them yet. Lets make a variable for our our result and store the difference between value1 and value2 in it. Then return the result.
```python
def subtract (value1, value2):
    result = value1 - value2
    return result
```
## Multiply x * y

This will be similar to subtract but we will replace - with * for multiplication.
```python
def multiply (value1, value2):
    result = value1 * value2
    return result
```

## Divide x / y
This will be similar to subtract but we will replace - with / for division.
```python
def divide (value1, value2):
    result = value1 / value2
    return result
```
But we're not done yet. What if someone passes in 0 for value2? If we leave it like this the program will throw an error. Lets let the caller know when value2 is 0 by returning a message before division occurs.
```python
def divide (value1, value2):
    if (value2 == 0):
        return 'Cannot divide by 0'
    result = value1 / value2
    return result
```

# Bonus
We want to implement the exponent, modulus and floor_divide functions.
## Exponent x ^ y
This will be similar to subtract but we will replace - with ** for exponentiation.
```python
def exponent (value1, value2):
    result = value1 ** value2
    return result
```
## Modulus x % y
This will be similar to subtract but we will replace - with % for modular arithmetic.
```python
def modulus (value1, value2):
    result = value1 % value2
    return result
```
## Floor Divide x // y
This will be similar to subtract but we will replace - with // for floor division.
```python
def floor_divide (value1, value2):
    result = value1 // value2
    return result
```
We'll run into the same issue we had with divide we need to check for dividing by zero.
```python
def floor_divide (value1, value2):
    if (value2 == 0):
        return 'Cannot divide by 0'
    result = value1 // value2
    return result
```


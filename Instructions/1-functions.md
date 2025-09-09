# Introduction to Branching

## What are Functions?

Functions are simply a block of code. They help with reusability and clarity. Like in math, they can take some inputs and produce some outputs but they don't always have to. 

Let's take a look at a function. The following function prints Hello World. It has zero inputs and doesn't return anything. 

```python
def f():
    print("Hello World")
```

Here's how to call the function:

```python
# prints Hello World
f()
```

Let's take a look at a function that takes an input, doubles it, and returns the doubled value. 
```python
def g(x):
    return 2 * x
```

To pass in a parameter, we can pass a value into the parentheses of the function we call. 
```python
g(3)
g(3.14)
```

To use the return value, we can set a variable equal to the result of the function. 

```python
n = 3
doubleN = g(n)
# doubleN = 6
```

We can also use functions with other types of data:

```python
def h(s):
    # if a string is passed in, it gets concatenated
    return s + s
single = "asdf"
double = h(single)
# double = asdfasdf
x = 1
y = h(x)
# y = 2
```

Here's a function that doesn't return any value and prints what's entered 10 times:
```python
def printInput(s):
    for i in range(10):
        print("Your input was", s)
printInput("Hello World!")
```

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

Let's take a look at a function that takes an input and doubles it. 
```python
def g(x):
    return 2 * x
```

To use it, we can set a variable equal to the result of the function. 

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
# double = asdfasdf
double = h(single)
x = 1
# y = 2
y = h(x)
```

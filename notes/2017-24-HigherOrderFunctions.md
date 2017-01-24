# Environments & Higher-Order Functions

There are several **frames** that store different names for lookup.

Frame levels include:
- global (includes all the built-in functions)
- function frames (created when a function is executed)

Frames can point to parent frames to get names outside the function.
Frames do not store the values that the names reference, but do keep track of *where* those names
point to.


## Functional Abstraction

Functions have **inputs**: usually called *arguments* or *parameters.*  
Functions have **outputs**: usually called *return values.*  
Functions can change the global state: also known as *side effects* and classified as a *non-pure*
function. (These should be kept separate: there shouldn't be both side effects and a return value)


## Higher-Order Functions

Use other functions as inputs or outputs

**Composing** functions: taking the results of one function and applying it to another

### Examples
```python
def sqr(x):
    return x * x

def double(x):
    return x + x

# composition:
double(sqr(5)) # 50
```

**Currying** functions: splitting a function with multiple arguments into a sequence of functions,
each with one argument.
```python
# returns a function that takes one argument adds the called argument to the
# initial argument the function generator was called with.
def add(x):
  def addx(y):
    return x + y
  return addx

add3 = add(3)
add3(4) # 7
```

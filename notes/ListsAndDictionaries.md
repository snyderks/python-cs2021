# Lists & Dictionaries

You can access the elements of an iterable type in order using a `for` or `while` loop.

```python
s = [1, 2, 3, 4]
# prints all the elements of s
for i in s:
    print(i)
```

In Python, most iterable types are also **sequence** types.
- Sequences can be indexed as well as iterated through.
- Indexing is done with square brackets: `my_list[0]`
- Sequence types are indexed using *integers.*

**Dictionaries** are also indexable, but with almost any type of key.

```python
d = dict(one=1, two=2, three=3)
print(d['one'])
```

These are also called *maps*, *hashes*, and several other names.

To iterate through a dictionary:
```python
d = dict(one=1, two=2, three=3)
for key in d:
    print(key) # prints the key

for key, value in d:
    print(key, value) # prints the key and value

for _, value in d:
    print(value) # prints the value
```

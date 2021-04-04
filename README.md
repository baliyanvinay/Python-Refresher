## Top-Level Script Environment 
Python Programs can be executed as stand-alone scripts or as a module which we import from other file in our program. If the __name__ of the current program is __main__ then it will be executed as a script.
```python
# Execute only the program is run as a script/stand-alone program 
if __name__ == '__main__':
  # Do script related actions
  pass
else:
  # what happens when treated as module
  pass
```

## Enumerate it right
Enumerate returns an enumerate object, iterable must be a sequence. The \__next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
```python
# enumerate(iterable, start=0)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

for season in enumerate(seasons, start=1):
  print(season)
```

## What is it? It is None.
Like other python data types, None is an object of NoneType class which represents the absence of a value, as when default arguments are not passed to a function. 
```python
>>> type(10)
>>> <class 'int'>
>>> type(True)
>>> <class 'bool'>
>>> type(None)
>>> <class 'NoneType'>
```
```python
if not None:
  print('Truth value of None is False')
  
# func default return is None object
def func():
  print('Something')
obj = func() # prints Something
print(obj)  # prints None
```

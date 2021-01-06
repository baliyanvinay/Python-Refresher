# Python Interview Preparation

## Explain 'Everything in Python is an object'.

## What is mutable and immutable objects/data types in Python?
Mutation generally refers to 'change'. So when we say that an object is mutable or immutable we meant to say that the value of object can/cannot change. <br>
When an object is created in Python, it is assigned a type and an id. An object/data type is mutable if with the same id, the value of the object changes after the object is created. 
##
<b>Mutable objects in Python</b>
-- Objects that can change after creation. Lists, byte arrays, sets, and dictionaries.
```python
>>> list_var = [17, 10]
>>> list_var
[17, 10]
>>> id(list_var)
2289772854208
>>> list_var += [17]
>>> list_var
[17, 10, 17]
>>> id(list_var)
2289772854208
```
ID of the object didn't change.

## 
<b>Immutable objects in Python</b>
-- Numeric data types, strings, bytes, frozen sets, and tuples.
```python
>>> # Example of tuples
>>> tuple_var = (17,)
>>> tuple_var
(17,)
>>> id(tuple_var)
1753146091504
>>> tuple_var += (10,)
>>> tuple_var
(17,10)
>>> id(tuple_var)
1753153466880
```
ID changes when made changes in object.

## What is the difference between list and tuples in Python?

# Module 11

Iterable :
can be passed to iter() to produce an iterator 

iterator 
can be passed to next() to get the next value in the sequence

```python
>>> iterable =['spring','Summer', 'Autumn','Winter']
>>> #list as iterable source object
>>> #iterable object gives us an iterator using iter()
>>> iterator =iter(iterable)
>>> next(iterator)
'spring'
>>>
>>> next(iterator)
'Summer'
>>> next(iterator)
'Autumn'
>>> next(iterator)
'Winter'
>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

- **Iterator**
    
    In Python, an iterator is an object that allows you to iterate over collections of data, such as lists, tuples ,dictionaries and sets.
    
- **Generator**
    
    In Python, a generator is a type of iterable that generates a sequence of values on the fly, rather than storing them all in memory at once. Generators are often used when dealing with large datasets or when you need to generate values one at a time, instead of all at once.
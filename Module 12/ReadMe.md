# Module 12

Comprehensions in Python are a concise syntax for describing lists, sets or dictionaries in a
declarative or functional style. This short-hand is readable and expressive, meaning that
comprehensions are very effective at communicating intent to human readers.

- **list Comprehension**
    
    As hinted at above, a list comprehension is a short-hand way of creating a list. It's an expression using a succinct syntax that describes how list elements are defined.
    
    The general form for a list comprehension is:
    
    ```python
    [ expr(item) for item in iterable ]
    ```
    
    Example 
    
    ```python
    >>> from math import factorial
    >>> f=[factorial(x) for x in range(20)]
    >>> f
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000]
    >>> from math import factorial
    >>> f=[len(str(factorial(x))) for x in range(20)]
    >>> f
    [1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]
    >>> type(f)
    <class 'list'>
    >>>
    ```
    
- **Set comprehensions**
    
    Sets support a similar comprehension syntax using, as you might expect, curly braces. Our
    previous "number of digits in factorials" result contained duplicates, but by building a set
    instead of a list we can eliminate them:
    
    ```python
    >>> from math import factorial as f
    >>> s={len(str(f(x) for x in range(20)))}
    >>> s
    {50}
    >>> s={len(str(f(x))) for x in range(20)} 
    >>> s
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18}
    ```
    
- **Dictionary Comprehension**
    
    The third type of comprehension is the dictionary comprehension. Like the set
    comprehension syntax, the dictionary comprehension also uses curly braces. It is
    distinguished from the set comprehension by the fact that we now provide two colon separated expressions — the first for the key and the second for the value — which will be
    evaluated in tandem for each new item in the resulting dictionary. Here's a dictionary we
    can play with:
    
    ```python
    {key_expression: value_expression for element in iterable}
    ```
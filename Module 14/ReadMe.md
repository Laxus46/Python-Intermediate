# Module 14

- **OOP Concepts: Inheritance, Encapsulation, Polymorphism, Abstraction**
    - **Inheritance:**
    Inheritance is a way to create new classes from existing ones. It allows a new class to take on the attributes and methods of an existing class, called the parent or superclass. The new class is called the child or subclass. In Python, you can define a subclass by specifying the superclass in parentheses after the class name
    - **Encapsulation:**
    Encapsulation is the practice of hiding implementation details of an object and exposing only the necessary interfaces to interact with it. In Python, this can be achieved through the use of private and protected variables and methods. Private variables and methods are denoted with a double underscore prefix, while protected variables and methods are denoted with a single underscore prefix.
    - **Polymorphism**:
    Polymorphism is the ability of objects to take on many forms. In Python, this can be achieved through method overriding and method overloading. Method overriding is when a subclass provides its own implementation of a method that is already defined in its superclass. Method overloading is when a class defines multiple methods with the same name but different parameters.
    - **Abstraction in python** is defined as a process of handling complexity by hiding unnecessary information from the user. This is one of the core [](https://stackify.com/oops-concepts-in-java/)concepts of object-oriented programming (OOP) languages
- **Composition**
    
    **Composition** is a concept that models a **has a** relationship. It enables creating complex types by combining objects of other types. This means that a class `Composite` can contain an object of another class `Component`. This relationship means that a `Composite` **has a** `Component`.
    
- **Instance Attributes and Class Attributes**
    
    **Instance Attributes** are unique to each object, (an instance is another name for an object). Here, any `Dog` object we create will be able to store its name and age. We can change either attribute of either dog, without affecting any other dog objects we’ve created.
    
    ```python
    class Dog:
    
        def __init__(self, name, age):
            self.name = name
            self.age = age
    ```
    
    This `__init__` is called the **initializer**. It is automatically called when we instantiate the class. It’s job is to make sure the class has any attributes it needs. It’s sometimes also used to make sure that the object is in a valid state when it’s instantiated, like making sure the user didn’t enter a negative age for the dog.
    
    **Class Attributes** are unique to each class. Each instance of the class will have this attribute. It’s sometimes used to specify a default value that all objects should have after they’ve been instantiated. Here, our class attribute is species
    
    ```python
    class Dog:
    
        species = 'mammal'
    
        def __init__(self, name, age):
            self.name = name
            self.age = age
    ```
    
- ****Instance, Class, and Static Methods****
    
    ```python
    class MyClass:
        def method(self):
            return 'instance method called', self
    
        @classmethod
        def classmethod(cls):
            return 'class method called', cls
    
        @staticmethod
        def staticmethod():
            return 'static method called'
    ```
    
    - **Instance Method**
        - An instance method is a type of method that is associated with instances of a class.
        - The first parameter of an instance method is always **`self`**, which refers to the instance of the class that the method is being called on.
        - Instance methods can freely access attributes and other methods of the same object, giving them the ability to modify an object's state.
        - Instance methods can also access the class itself through the **`self.__class__`** attribute, which allows them to modify class state as well.
        - Instance methods are the most commonly used type of method in Python and are used to define behavior that is specific to individual instances of a class.
    - **Class Method**
        - A class method is a type of method in Python that is associated with the class itself, rather than individual instances of the class.
        - Class methods are defined using a @classmethod decorator and take a **`cls`** parameter instead of a **`self`** parameter.
        - The **`cls`** parameter points to the class itself, rather than an instance of the class.
        - Because class methods don't have access to individual instances of the class, they can't modify instance-specific state. However, they can modify class-level state that is shared across all instances of the class.
        - Class methods are useful for defining behavior that applies to the class as a whole, rather than individual instances of the class.
        - The main difference between class methods and instance methods is that class methods operate on the class itself, while instance methods operate on individual instances of the class.
    - **Static Method**
        - A static method is a type of method in Python that is not associated with either the class itself or individual instances of the class.
        - Static methods are defined using a @staticmethod decorator and take no **`self`** or **`cls`** parameter.
        - Because static methods don't have access to either individual instances of the class or the class itself, they can't modify instance-specific state or class-level state. They are restricted in what data they can access.
        - Static methods are primarily a way to namespace methods within a class.
        - Static methods are useful for defining utility functions that don't require access to object or class state.
        - The main difference between static methods and instance methods or class methods is that static methods don't have access to either object or class state.
    
- **Overloading and Overriding**
    
    In Python, method overriding is a feature of inheritance that allows a subclass to provide its implementation for a method that is already defined in its parent class. When a method in the subclass has the same name as a method in the parent class, the method in the subclass overrides the method in the parent class.
    
- **Name mangling**
    
    Name mangling is a mechanism in Python that changes the name of class variables to prevent accidental access from outside the class. It is done by adding a double underscore prefix to the variable name.
    Name Mangling is nothing but the mechanism, by which any identifiers with 2 leading underscores ( like **__age**) are textually replaced with `***classname*_age**.`
    
- **Introspection**
    
    Introspection is the ability of a program to examine its own structure and state; a process of
    looking inward to perform self-examination.
    
    - **Introspecting types**
        
        ```python
        >>> i =10  
        >>> type(i)
        <class 'int'>
        >>> int
        <class 'int'>
        >>> repr(int)
        "<class 'int'>"
        ```
        
    - **Introspecting objects**
        
        ```python
        >>> a=43
        >>> dir(a)
        ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
        >>> getattr(a,'numerator') 
        43
        >>> getattr(a,'conjugate') 
        <built-in method conjugate of int object at 0x00000202C8DC6E70>
        >>> callable(getattr(a,'conjugate'))
        True
        >>> hasattr(a,'index')
        False
        >>> hasattr(a,'bit_length')
        True
        ```
        
    - **Introspecting Scope**
        
        ```python
        >>> globals()
        {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'i': 10, 'a': 43}
        >>> locals()
        {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'i': 10, 'a': 43}
        ```
        
    - **Inspect Module**
        
        This module provides functions for examining the properties of objects at runtime. For example, **`inspect.getmembers()`** can be used to get a list of all the members of an object, while **`inspect.getargspec()`** can be used to get the arguments of a function.
        
- **Abstract class**
    
    Abstract base classes exist to be inherited, but never instantiated. Python provides the `abc` module to define abstract base classes.
    
    This change has two nice side-effects:
    
    1. You’re telling users of the module that objects of type `Employee` can’t be created.
    2. You’re telling other developers working on the `hr` module that if they derive from `Employee`, then they must override the `.calculate_payroll()` abstract method.
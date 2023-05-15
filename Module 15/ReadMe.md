# Module 15

- **Exception Handling**
    
    Exception handling is a way to manage errors and exceptions that may occur during the execution of a program. Python provides built-in exception handling mechanisms to handle errors and exceptions that may arise in your code.
    
- **Creating And serving Exception**
    
    You can create and raise an exception in Python using the **`raise`** keyword. For example, if you want to raise an exception when a particular condition is met, you can use the following code:
    
    ```python
    if x < 0:
        raise ValueError("x should be greater than zero")
    ```
    
- **User Defined Exceptions**
    
    We can also create our own custom exceptions by creating a new class that inherits from the built-in **`Exception`** class. For example, if we want to create a custom exception called **`MyException`**, we can use the following code:
    
    ```python
    class MyException(Exception):
        pass
    ```
    
- **Raising exceptions**
    
    In Python, we can raise an exception using the **`raise`** statement. When we raise an exception, we are essentially telling the Python interpreter that an error or exceptional condition has occurred and that the program cannot continue with its normal execution.
    
    The **`raise`** statement can be used with any built-in or user-defined exception class. Here's an example of how to raise a **`ValueError`** exception:
    
    ```python
    class MyCustomException(Exception):
        pass
    
    raise MyCustomException("Something went wrong")
    ```
    
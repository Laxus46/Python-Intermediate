# def outer_func():
#     message='hello_world'
#     def inner_func():
#         print(message)
#     return inner_func
# my_fun=outer_func()
# print(my_fun.__name__)
# my_fun()

#practical example of closure

import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
    def log_func(*arg):
        logging.info('Running"{}"with arugments {}'.format(func.__name__,arg))
        print(func(*arg))
    return log_func
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
add_logger=logger(add)
sub_logger=logger(sub)
add_logger(3,4)
sub_logger(21,10)
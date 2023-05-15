from typing import Any

class decorator_class(object):
    def __init__(self,origin_func):
        self.origin_func=origin_func
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('call method executed this before {}'.format(self.origin_func.__name__))
        return self.origin_func(*args,**kwds)
@decorator_class
def display():
    print('Display function ran')

@decorator_class
def display_info(name,age):
    print('display_info ran with arguments({},{})'.format(name,age))
display_info('laxman','22')
display()
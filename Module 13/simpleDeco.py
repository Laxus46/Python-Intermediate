def decorator_func(origin_func):
    def wrapper_func(*args,**kwargs):
        return origin_func(*args,**kwargs)
    return wrapper_func

@decorator_func
def display():
    print('Display function ran')

@decorator_func
def display_info(name,age):
    print('display_info ran with arguments({},{})'.format(name,age))
display_info('laxman','22')
display()

# decorator_display=decorator_func(display)
# decorator_display()
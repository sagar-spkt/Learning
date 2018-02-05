def decorator_with_arg(arg1):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print('passed param value {}'.format(arg1))
            print('wrapper executed this before {}'.format(original_function.__name__))
            return original_function(*args, **kwargs)
        return wrapper_function
    return decorator_function


class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_with_arg('Nepal')
def display():
    print('display function ran')


@decorator_with_arg('India')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


# @DecoratorClass
# def display():
#     print('display function ran')
#
#
# @DecoratorClass
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))


display()
display_info('Sagar', 35)

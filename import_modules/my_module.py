print('Importing my module')

name = 'John'


def say_hello(name=''):
    print(f'Hi{"" if not name else f", {name}"}!')

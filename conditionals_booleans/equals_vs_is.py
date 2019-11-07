a = [1, 2, 3]
b = [1, 2, 3]

print(f'''
    a = {a}
    b = {b}

    id(a) = {id(a)}
    id(b) = {id(b)}

    a == b => {a == b}
    a is b => {a is b}
    is: id(a) == id(b) => {id(a)} == {id(b)}

    Boolean evaluations 
    bool(False) => {bool(False)}
    bool(None) => {bool(None)}
    bool(0) => {bool(0)} but bool(-10) => {bool(-10)}
    bool('') => {bool('')}   but   bool('some') => {bool('some')}
    bool(()) => {bool(())}   but   bool((1,2,3)) => {bool((1,2,3))}
    bool([]) => {bool([])}   but   bool([1,2,3]) => {bool([1,2,3])}
    bool({{}}) => {bool({})}   but   bool({{'key': 'value'}}) => {bool({'key': 'value'})}
''')

print(help(id))

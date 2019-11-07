def stud_info(*args, **kwargs):
    print(f'''
args => {args}
kwargs => {kwargs}
    ''')


courses = ('Math', 'Art')
info = {'name': 'John', 'age': 22}

stud_info('Math', 'Art', name='John', age=22)
stud_info(*courses, **info)

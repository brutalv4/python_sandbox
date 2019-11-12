nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

heroes_names = {h: n for h, n in zip(heroes, names) if n != 'Peter'}

mess_nums = [1, 1, 1, 1, 2, 1, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9, 9, 9]
my_set = {n for n in mess_nums if n % 2 == 0}

print(f'''
nums => {nums}
[n for n in nums if n % 2 == 0] => {[n for n in nums if n % 2 == 0]}
list(filter(lambda n: n % 2 == 0, nums)) => {list(filter(lambda n: n % 2 == 0, nums))}
[(l, n) for l in 'abcd' for n in nums] => {[(l, n) for l in 'abcd' for n in nums]}
heroes_names = {{h: n for h, n in zip(heroes, names) if n != 'Peter'}} 
    => {heroes_names}
my_set = {{n for n in mess_nums}}
    => my_set = {my_set}  
''')

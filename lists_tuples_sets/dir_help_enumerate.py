for c in (list, tuple, set):
    print(f'\n{c}')
    for i, m in enumerate(list(filter(lambda i: not i.startswith('__'), dir(c))), start=1):
        print(f'{i}: {m}')

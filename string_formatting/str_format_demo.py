import datetime

print('{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(datetime.datetime.now()))

person = {'name': 'John', 'age': 29}
print('it was {name} and he is {age} year(s) old'.format(**person))

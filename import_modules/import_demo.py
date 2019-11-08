from my_module import say_hello, name
import sys
import datetime
import calendar
import os
import antigravity
import this

say_hello(name)
print('', 'sys.path is:', *sys.path, sep='\n')

print(f'''
today = datetime.datetime.today() => {datetime.datetime.today()}
isleap = calendar.isleap(2020) => {calendar.isleap(2020)}
os.getcwd() => {os.getcwd()}
os.__file__ => {os.__file__}
''')

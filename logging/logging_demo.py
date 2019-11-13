'''
DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
'''
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# https://docs.python.org/3/library/logging.html#logrecord-attributes
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('events.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def add(x, y):
    logger.debug(f'add({x}, {y})')
    return x + y


def subt(x, y):
    logger.debug(f'sub({x}, {y})')
    return x - y


def mult(x, y):
    logger.debug(f'mul({x}, {y})')
    return x * y


def div(x, y):
    logger.debug(f'div({x}, {y})')
    return x / y


num1 = 20
num2 = 50

logger.info(f'{num1} + {num2} = {add(num1, num2)}')
logger.info(f's{num1} - {num2} = {subt(num1, num2)}')
logger.info(f'm{num1} * {num2} = {mult(num1, num2)}')
logger.info(f'{num1} / {num2} = {div(num1, num2)}')

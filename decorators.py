# def outer_function(msg):
#     message = msg 
#     def inner():
#         print(message)
#     return inner

# obj = outer_function('hi')
# obj()


# def outer_funnction(original_function):
#     def inner_function():
#         print('before executing inner function ')
#         # return original_function()   # if we return it will not execute below
#         original_function()   # if we return it will not execute below
#         print('after executing inner funnction ')
#     return inner_function


# @outer_funnction
# def function():
#     print('Hi MY name is rahul ')

# # obj = outer_funnction(function)  # replacing it with decorator 
# # obj()

# function()

# def outer_funnction(original_function):
#     def inner_function(*args,**kwargs):
#         print('before executing inner function ')
#         # return original_function()   # if we return it will not execute below
#         original_function(*args,**kwargs)   # if we return it will not execute below
#         print('after executing inner funnction ')
#     return inner_function


# @outer_funnction
# def function(name , age ):
#     print(f'my name is {name} and my age is {age}')

# # obj = outer_funnction(function)  # replacing it with decorator 
# # obj()

# function('rahul' , 18)


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s : %(asctime)s : %(message)s')
handler = logging.FileHandler('test.log')
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)


def outer_funnction(original_function):
    def inner_function(*args,**kwargs):
        # print('before executing inner function ')
        # return original_function()   # if we return it will not execute below
        original_function(*args,**kwargs)   # if we return it will not execute below
        # print('after executing inner funnction ')
    return inner_function


@outer_funnction
def function(x,y):
    return x*y

x=2
y=3
logger.debug(f'{x}*{y}={function(2,3)}')
logger.info(f'{x}*{y}={function(2,3)}')
logger.warning(f'{x}*{y}={function(2,3)}')
logger.error(f'{x}*{y}={function(2,3)}')
logger.critical(f'{x}*{y}={function(2,3)}')




import time 

def outer_funnction(original_function):
    def inner_function(*args,**kwargs):
        # print('before executing inner function ')
        # return original_function()   # if we return it will not execute below
        original_function(*args,**kwargs)   # if we return it will not execute below
        # print('after executing inner funnction ')
    return inner_function

@outer_funnction
def time_function():
    
    time.sleep(2)
    print('inside the time_function ')

# time_function()
    
    
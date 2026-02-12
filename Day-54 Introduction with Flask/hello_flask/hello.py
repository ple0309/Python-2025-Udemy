from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()






#################################################################
# def multiply(n1,n2):
#     return n1*n2
#
# def add(n1,n2):
#     return n1+n2
#
# def divide(n1,n2):
#     return n1/n2
#
# def minus(n1,n2):
#     return n1-n2
#
#
#
#
# #Functions are first-class objects, can be passed around as arguments
# #e.g. int/string/float etc.
# def calculate(calc_function, n1, n2):
#     return calc_function(n1,n2)
#
# result = calculate(add,2,3)
# print(result)
#
#
#
#
# #Nested Functions
# def outer_function():
#     print("I'm outer")
#
#     #Only access by outer_function():
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
# outer_function()
#
#
###################################################################
# # functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     #Only access by outer_function():
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function()
#
#
# ##Python Decorator
# import time
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before
#         function()
#         function()
#         #Do something after
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# @delay_decorator
# def say_bye():
#     print("Bye")
#
# def say_greeting():
#     print("How are you?")
#
# decorated_function = delay_decorator(say_greeting)
# decorated_function()
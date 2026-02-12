from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return ('<h1 style="text-align:center">Hello, World!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGI3ajVydHFhOThta2R0YW43OWd2Y29ieWcxM2xscjIwbzVvaTBnbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KLB8IXYVZevYY/giphy.gif" width=200px>')

#Different routes using the app.rout decorator
#u = Underline
#em = Italic
#b = Bold
def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"

#/<name> is the variable so all the string after username/ will be the name in this case
# If I want to do with other variable, I can do it with the converter types int
# also put number in parameter.
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old."

# #Another example about if I want to get the path inside variable.
# #path:name inside <> will return all the path with slash after username/
# @app.route("/username/<path:name>")
# def greet(name):
#     return f"Hello there {name}"

if __name__ == "__main__":
    #run the app in debug mode to auto-reload.
    app.run(debug=True)






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


###############################################################
## Advanced Python Decorator Functions with *args and **kwargs
class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0]) #put the args[0] like user in this case.
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Jaden")
new_user.is_logged_in = True
create_blog_post(new_user)
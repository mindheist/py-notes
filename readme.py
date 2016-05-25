# Assigning functions to variables in python

def greet(name):
    return "Hello " + name

print greet("Jane") # the function can be called traditionally like this.

greet_someone = greet # Assigning a function to a variables
print greet_someone("John")

# Demonstrating functions within functions
def greet(name):
    def get_message():
        return "Hello"

    result = get_message()+name
    return result

print greet("John")
# outputs: Hello John

# functions can return other functions
def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print greet()

#ouputs : Hello there

def get_text(name):
    return "Hello there , {0}".format(name)

def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

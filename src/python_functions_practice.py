def return_10():
    return 10

def add(a, b):
 add_result = a + b
 return(add_result)

def subtract(c, d):
     subtract_result = c - d 
     return(subtract_result) 

def multiply(e, f):
    multiply_result = e * f
    return(multiply_result)

def divide(g, h):
    divide_result = g / h
    return(divide_result)

def length_of_string(string):
    length_of_string = (len(string))
    return(length_of_string)

def join_string(string1, string2):
    join_string = (string1 + string2)
    return(join_string)

def add_string_as_number(a, b):
    add_result = int(a) + int(b)
    return(add_result)

def number_to_full_month_name(a):
    months = [None, "January"]
    result = months[a]
    return(result)

def number_to_full_month_name(a):
    months = [None, "January", "February", "March"]
    result = months[a]
    return(result) 

def number_to_full_month_name(a):
    months = [None, "January", "February", "March", "April", "May", "June", "July", "August", "September"]
    result = months[a]
    return(result)

def number_to_short_month_name(a):
    months = [None, "Jan"]
    result = months[a]
    return(result)

def number_to_short_month_name(a):
    months = [None, "Jan", "Feb", "Mar", "Apr"]
    result = months[a]
    return(result)

def number_to_short_month_name(a):
    months = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct"]
    result = months[a]
    return(result)

def volume_of_cube(side):
    return side * side * side

def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)
# Francisco Rodriguez
# UWYO COSC 1010
# Submission Date
# Lab 01
# Lab Section: MON 3:10 pm
# Sources, people worked with, help given to: https://stackoverflow.com/questions/17322208/multiple-try-codes-in-one-block
# your
# comments
# here
import math

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def check_int_or_float(number):  
    
    try: 
        float(number)
        return number
    except ValueError:
        pass
    try: 
        int(number)
        return number
    except:
        return False
int_or_float = input("Enter a number: ")
print(check_int_or_float(int_or_float))



    
    
    
        
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def point_slope(m,b,lx,hx): 
    try: 
        lx= int(lx)
        hx= int(hx)
        m=float(m)
        b=float(b)
        y_vals= []
        if hx >= lx:
            for i  in range(lx,hx+1):
                y = m*i+b
                y_vals.append(int(y))
        return y_vals
    except ValueError:
        return False
    
    
while True: 
    user_m= input("enter an M value or exit to exit anytime: ")
    if user_m == "exit" :
        break
    user_b= input("enter an b value: ")
    if  user_b == "exit" :
        break
    user_lx= input("enter an lower bound value: ")
    if  user_lx == "exit" :
        break
    user_hx= input("enter an upper bound value: ")
    if  user_hx == "exit":
        break
    if user_m == "exit" or user_b == "exit" or user_lx == "exit" or user_hx == "exit":
        break
    else: 
        print(point_slope(user_m,user_b,user_lx,user_hx))

            
     


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def quad_form(a,b,c):
    a= int(a)
    b= int(b)
    c= int(c)
    disc= b**2 - (4*a*c)
    if disc< 0:
        return "null"
    else:
        x_one = (-b + math.sqrt(disc)) / (2*a)
        x_two = (-b - math.sqrt(disc)) / (2*a)
    return (x_one,x_two)
while True: 
    user_a= input("enter an a value or exit to exit anytime: ")
    if user_a == "exit" :
        break
    user_bb= input("enter an b value: ")
    if  user_bb == "exit" :
        break
    user_c= input("enter an c value: ")
    if  user_c == "exit" :
        break
    
    else: 
        print(quad_form(user_a,user_bb,user_c,))

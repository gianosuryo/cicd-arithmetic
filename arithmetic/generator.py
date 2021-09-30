from __future__ import print_function

def validator(a, b):
    if(not (((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float)))):
        return False
    elif(b == 0):
        return False
    else:
        return True

def division(a = 1, b = 1):
    if(validator(a, b)):
        return a / b
    else:
        return 'Invalid input!'


if __name__ == "__main__":
    print(validator(4, '3'))
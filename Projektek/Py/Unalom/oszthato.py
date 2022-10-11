from tkinter import Y


def oszthato(x):
    if x % 2 == 0 and x % 3 == 0:
        return True
    else:
        return False
    
x = int(input())

print(oszthato(x))
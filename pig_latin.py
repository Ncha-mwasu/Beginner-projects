#!/usr/bin/python3
def funct(string):
    term = string
    arr = []
    splinter = term.split()
    for items in range(len(splinter)):
        pig_latin = splinter[items][1:] + splinter[items][0] + "ay"
        arr.append(pig_latin)
    string = " ".join(arr)
    return string


print(funct("never mind them"))

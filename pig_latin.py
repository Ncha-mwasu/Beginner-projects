#!/usr/bin/python3
print("English to pig latin converter")
term = input("Write up: ")
arr = []
splinter = term.split()
for items in range(len(splinter)):
    pig_latin = splinter[items][1:] + splinter[items][0] + "ay"
    arr.append(pig_latin)
string = " ".join(arr)
print(string)

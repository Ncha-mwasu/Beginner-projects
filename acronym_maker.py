#!/usr/bin/python3
Term = input("Phrase? ")
cap = Term.title()
acronym = ""
if "of" in Term:
    quest = input("would you like to keep the 'of' (y/n)? ")
    if quest == "n":
        acro_list = cap.replace("Of", "").split()
    else:
        acro_list = cap.split()
for items in acro_list:
    acronym = acronym + items[0] + "."
print(f"the acronym of {Term} is {acronym}")

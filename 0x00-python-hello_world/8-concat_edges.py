#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find("object-oriented programming"):str.find(" language")] + " with python"
print(str)

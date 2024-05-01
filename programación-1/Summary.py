# -*- coding: utf-8 -*-

# ✧⁠*₊˚ 🦢・₊✧ RESUMEN DE MÉTODOS Y FUNCIONES ✧⁠*₊˚ 🦢・₊✧


# ✧⁠*〜⁠*〜⁠*〜⁠* List / Array Methods 〜⁠*〜⁠*〜⁠*✧
# https://www.w3schools.com/python/python_ref_list.asp

# ༺ append() Adds an element at the end of the list ➤ arr.append()
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange") # ➤ ['apple', 'banana', 'cherry', 'orange']

# ༺ count() Returns the number of elements with the specified value ➤ arr.count()
# fruits = ["apple", "banana", "cherry", "cherry", "cherry"]
# x = fruits.count("cherry") # ➤ 3

# ༺ index() Returns the index of the first element with the specified value ➤ arr.index()
# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry") # ➤ 2 

# ༺ insert() Adds an element at the specified position ➤ arr.insert()
# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(1, "orange") # ➤ ['apple', 'orange', 'banana', 'cherry']

# ༺ list() Returns a list ➤ 
# fruits = list(('apple', 'banana', 'cherry')) # ➤ ['apple', 'banana', 'cherry']

# ༺ pop() Removes the element at the specified position ➤ arr.pop()
# fruits = ['apple', 'banana', 'cherry']
# fruits.pop(1) # ➤ ['apple', 'cherry']

# ༺ remove() Removes the first item with the specified value ➤ arr.remove()
# fruits = ['apple', 'banana', 'cherry']
# fruits.remove("banana") # ➤ ['apple', 'cherry']

# ༺ reverse() Reverses the order of the list ➤ arr.reverse()
# fruits = ['apple', 'banana', 'cherry']
# fruits.reverse() # ➤ ['cherry', 'banana', 'apple']

# ༺ sort() Sorts the list ➤ arr.sort()
# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort() # ➤ ['BMW', 'Ford', 'Volvo']

# ✧⁠*〜⁠*〜⁠*〜⁠* String Methods 〜⁠*〜⁠*〜⁠*✧
# https://www.w3schools.com/python/python_ref_string.asp

# ༺ isalnum() Returns True if all characters in the string are alphanumeric ➤ string.isAlNum()
# txt = "Company12"
# x = txt.isalnum() # ➤ True

# ༺ isalpha() Returns True if all characters in the string are in the alphabet ➤ string.isAlpha()
# txt = "CompanyX"
# x = txt.isalpha() # ➤ True

# ༺ isdecimal() Returns True if all characters in the string are decimals ➤ string.isDecimal()
# txt = "1234"
# x = txt.isdecimal() # ➤ True

# ༺ isdigit() Returns True if all characters in the string are digits ➤ string.isDigit()
# txt = "50800"
# x = txt.isdigit() # ➤ True

# ༺ isnumeric() Returns True if all characters in the string are numeric ➤ string.isNumeric()
# txt = "565543"
# x = txt.isnumeric() # ➤ True

# ༺ join() Converts the elements of an iterable into a string ➤ element or symbol.join(string)
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple) # ➤ John#Peter#Vicky

# ༺ lower() Converts a string into lower case ➤ string.lower()
# txt = "Hello my FRIENDS"
# x = txt.lower() # ➤ hello my friends

# ༺ split() Splits the string at the specified separator, and returns a list ➤ string.split()
# txt = "welcome to the jungle"
# x = txt.split() # ➤ ['welcome', 'to', 'the', 'jungle'] 

# ༺ upper() Converts a string into upper case ➤ string.upper()
# txt = "Hello my friends"
# x = txt.upper() # ➤ HELLO MY FRIENDS


# ✧⁠*〜⁠*〜⁠*〜⁠* Exists in 〜⁠*〜⁠*〜⁠*✧

# ༺ in ➤ To check if a value is present in a list, tuple, etc. in LITERAL order ➤ str in str
# fruits = ["apple", "banana", "cherry"]
# if "banana" in fruits:
#   print("yes")

# a = 'abc'
# b = 'abcd'
# print(a in b) #--> true (aparece literalmente en el orden)

# ༺ subset() Returns whether another set contains this set or not ➤ str.issubset(str2) IMPORTANT to test with an original set
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y) # ➤ True 
# print(z)

# c = set('aeiou')
# d = 'murcielago'
# print(c.issubset(d)) #---> true (acá no necesitan estar en orden, solo aparecer)

# ✧⁠*〜⁠*〜⁠*〜⁠* Dictionary Methods 〜⁠*〜⁠*〜⁠*✧
# https://www.w3schools.com/python/python_ref_dictionary.asp

# ༺ get() Returns the value of the specified key ➤ dic.get(key)
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.get("model") # ➤ Mustang

# ༺ items() Returns a list containing a tuple for each key value pair ➤ dic.items()
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.items() # ➤ dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]) 

# ༺ keys() Returns a list containing the dictionary's keys ➤ dic.keys
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.keys() # ➤ dict_keys(['brand', 'model', 'year'])

# ༺ values() Returns a list of all the values in the dictionary ➤ dic.values
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.values() # ➤ dict_values(['Ford', 'Mustang', 1964])

 


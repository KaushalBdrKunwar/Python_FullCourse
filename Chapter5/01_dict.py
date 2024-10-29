marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}

print(marks, type(marks))

# print(marks[0]), not possible

print(marks["Harry"]) #tells marks of harry.

#properties of python dictonaries
# 1.It is unordered
# 2.It is mutable
# 3. It is indexed
# 4. Cannot contain duplicate keys.

#-----------Methods in Dictonary------#
print(marks.items())# gives all items in form of tuples

print(marks.keys())# prints keys
print(marks.values())# prints values

marks.update({"Harry": 99})#updates due to mutable
print(marks)

print(marks.get("Harry"))#gets marks of Harry.





# -*- coding: utf-8 -*-
"""Python4_List

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fQgxBVO2AOq9TrLu_nTG-_iq9KB1yRlS

**Today we will discuss the properties and methods applicable to list datatype.**

As the name indicates, a list can contain multiple data points... so a list is a collection of data

Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary.
"""

#  Creating a list

numbers = [0,2,1,3,5,4]
# Creating a list with six elements 0,2,1,3,5,4 - notice the square brackets

# To print our list and length of the list

print(numbers)
length=len(numbers)
print("Number of elements in list = ", length)

# We can sum the numbers in our list using:

y = sum(numbers)
print("The sum of numbers in the list is ", y)

# Accessing elements of a list by index
# In python the indexing begins at 0, meaning the first item in the list has an index of 0
# Next is 1, then 2, and so on
print(numbers)
print(numbers[0])

print(numbers[1])
#prints the second item in the list as indexing begins at 0

print(numbers[1:4])
#prints elements starting at index 3

print(numbers[:3])
#prints elements from index 0 to n-1

print(numbers[3:])
#prints elements in the list starting from index n till the last item in the list

# To sort the numbers i.e. arrange numbers in order (e.g. accending order)
numbers.sort()
print(numbers)

# To sort in reverse order i.e. decending order
numbers.sort(reverse=True)
print(numbers)

# Modifying the list - append, insert, delete

# Let us start by learning appending
subjects = ["Physics", "Chemistry", "Biology", "Maths"]
print(subjects)
subjects.append("Computers")
print(subjects)
# Note: this is the difference between lists and strings. While strings cannot be modified, lists can be modified. Also notice that numeric data (numbers) do not require double qoutes like alphabets.

# Sorting list in alphabetical order
subjects.sort()
print(subjects)

# Sorting list in reverse alphabetical order
print(subjects)
subjects2=sorted(subjects, reverse=True)
print(subjects)
print(subjects2)

# Alternatively, we can use the following direct command. However, this will lead to converting the original file
print(subjects)
subjects.reverse()
print(subjects)

# To mutate or add an object to a list, we use the "insert" function:
subjects.insert(1, "English")
print(subjects)

# To add objects at the end, we use the "extend" function:
subjects.extend(["Communication_skills", "Soft_skills"])
print(subjects)

# Pop- removes the last element by default, or an element by index specified in ()
print(subjects)
print(subjects.pop())
print(subjects, "\n")
subjects.pop(1)
print(subjects, "\n")

# remove is used to remove selected object from the list
subjects.remove("Physics")
print(subjects)

# del is used to delete a specified index from the list
del(subjects[1])
print(subjects)

# To add two lists together
subjects=["a","b","c","d"]
marks=[10,9,8,9]
subjects_marks=subjects+marks
print(subjects_marks)

# To find out how many times a particular object appears in a list:
x=subjects_marks.count("a")
print(x)

# To copy a list into a new variable name:
y=subjects_marks.copy()
print(y)
from typing import List


num1 = "sd"
print(type(num1))
num1 = 2
print(num1)
print(type(num1))


num3: List[str] = [2,4.3,34,2,2,2]
print(num3)

num4: set[str] = {23,3,3,3,3}
print(num4)

num5: tuple[str,float] = ("s",4)
print(num5)

num6: dict[str] = ["Asds"]

a:str = '''my 
name 
is 
Sudais'''
print(a)

b:str = "Pak zinda bad"
print(b.title())


# FSTRing


fname:str = "Sudais"
age:int = 3
lass:str="piaic"

std_card : str = f""" 
Student detail
Name: {fname}
Age:{age} 
class:{lass}
{3+4+4}
"""
print(std_card)


exec("")

s = "         s          "
print(s.strip()) #Removing spaces


# List Chapter 3
# hetrogenous data type, length is dynamic (positive and negative), 

#                      0        1         2
names : list[str] = ["Sir", "Teacher", "Mentor"]
#                       -3       -2        -1
print(names[2], names[-1]) # positve and negative indexing 

cricketers : list[str] = ["Vk","BA","ABD"]

cricketers.append("KW")
print(cricketers)

names.extend(cricketers)
print(names)

cricketers.append(names)
print(cricketers)


# Slicing(start[include], end[n-1], step[sequence])
# slicing always itrate from left to right 
# step = -1 (left to right direction me chlega)

abc : list[str] = list("abcdefgh")
print(type(abc), abc)
print(abc[1:4], abc[4:1:-1])# -1 is a step means it itrate right to left
print(abc[:4:2])
ls : list[str] = print([i for i in dir(names) if "_" not in i])
strr : list[str] = print([i for i in dir(str) if "_" not in i]) 
print(strr)

nass : int = 'sdfsd'

print(4 \
    + 5 \
    + 5)


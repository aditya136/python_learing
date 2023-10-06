#Learning Python
''' learnt how to commit '''




#Learning about Data Types-
#complex data type
#z = 2j
#print(type(z))

#int type data
#aditya = 136
#print(aditya)
#print(type(aditya))

#floating type data
#aditya = 136.6
#print(aditya)
#print(type(aditya))

#complex type data
#aditya = 23482977j
#print(aditya)
#print(type(aditya))

#text type data/str type data
#MyName = "Aditya Banerjee"
#print(MyName)
#print(type(MyName))





#learning boolean data type
#bool = True
#print(bool)
#print(type(bool))

#z = 10
#x = 8
#print(x < z)





#string formatting
'''num1 = 12
num2 = 20
print(f"This is my super numebr {num1 + num2}")'''

#print(type(f"{10-5}"))







#learning bynary type data

#bytes
''' hablulist = [1,2,3,54,5,41,2,121,255]
b = bytes(hablulist)
print(bytes(hablulist))
print(type(b)) '''
#b[0] = 10   #bite is immutable

#bytearrays
'''hablulist = [1,2,3,54,5,41,2,121,255]
b = bytearray(hablulist)
print(bytes(hablulist))
print(type(b))
b[0] = 10 '''  #bytearray is mutable





#learning none type data
'''x = None
print(x)
print(type(x))'''







#Python operators


#arithmetic operators
#a = 10
#b = 20
#print(a + b)#addition
#print(b - a)#subtraction
#print(a * b)#multiplication
#print(b/a)#division
#print(b % a)#modulus

#exponenetiation
#x = 5
#y = 2
#print(x ** y)#5*5 (works like math to the power)

#floor division
#print(x // y)#floor division





# assignment operators
# d = 5 #5 is assigned in d..
# sum = d + 5  #d + 5 is assigned in the variable called sum
# print(sum) #At present sum's value is 10

# sum += 1
# print(sum)#At present sum's value is 11

# sum -= 1
# print(sum)#At present sum's value is 10

# sum *= 2
# print(sum)#At present sum's value is 20

# I have to comment this↓ befor using the floor division equeal(//=) sing....Other wise it won't work
# sum /= 2
# print(sum)#At present sum's value is 10.0

# sum //= 2
# print(sum)#At present sum's value is 5







#comparison operator
# a = 2
# b = 5
# print(a == b) #equal sing
# print(a != b) #not equal sing
# print(a > b) #greater than sing
# print(a < b) #less than sing
# print(a >= b) #greater than or equal to   *works like or operator
# print(a <= b) #less than or equal to      *works like or operator




#logical operator
#a = 2
#b = 5
#print(a < b and a > b)
#print(a < b or a > b)
#print(not(a < b))





# learning swapping

# swapping
'''c = 50
d = 60
c,d = d,c #swapping
print("This value is now c", c)
print("This value is now d", d)'''





 #learning user input

#name = input("What's your name?: ")
#print( "hello " + name  )

# user_name, password = input("Enter your username: "), input("Enter your password: ")
# print("Hello", user_name + "." + "   " + "Your password is", password)






#learning type casting
# string_type_data = "123"
# print(type(int(string_type_data)))
# print(string_type_data)
# print(type(float(string_type_data)))
# print(float(string_type_data))








#learning python list in depth             *It's a mutable data type


# li = [1, 2, 3]
# #print(type(li))
# li[1] = 10#change list's value      
# print(li)

""" *Wow we can also take variables as a list item"""

#list item add or remove
#li = ["Aditya", 12, 1.2, 12j, True]
#print(li)
# li.append("Adding a new thing")
# print(li)

# li.insert(1, 2.2)
# print(li)


#There is a lot of things to remove item from a list..almost 4 ways..let's try
#li = ["Aditya", 12, 1.2, 12j, True]
#print(li)
#li.remove("Aditya")
#print(li)

#li.pop(3)
#li.pop()  #removes the last item if there is no index number given
#print(li)

#del li[3]
#del li   #as the documentation it should be work but it does not....
#print(li)

#li.clear()
#print(li)




#loop list

#for loop
# looplist = ["Arnob", "Ankan", "Zaiya", "Apurbo", "Ronobir", "Ayesha"]
# for best_friends in looplist:
#    print(best_friends)

# for best_friends in range(len(looplist)):
#    print(best_friends)


#while loop
# looplist = ["Arnob", "Ankan", "Zaiya", "Apurbo", "Ronobir", "Ayesha"]
# y = 0
# while y < len(looplist):
#    print(looplist[y])
#    y = y + 1






#List Comprehension

# newlist = [1, 2, 3, 4, 5]
# for double in newlist:
#    print(double*2)   #comprehension does the same thing but, in 1 line

# Double = [ double*2 for double in newlist] 
# print(Double)








#learning sort list


# example_list = [2, 1, 4, 6, 8, 3, 5, 7]
# print(example_list)
# example_list.sort()
# print(example_list)


#reverse list
# example_list = [1,2,3,4,5,6,7,8,9,10]
# print(example_list)
# example_list.sort(reverse=True)
# print(example_list)



#Copy a list
# num = [1,2,3,4,5,6,7,8,9]
# print(num)
# num2 = num.copy()
# print(num2)




#Join two list
# li1 = [1,2,3]
# li2 = ['a','b','c',]

#With out using any method.
# li3 = li1 + li2
# print(li3)

#With method/with the help of a method called extend
# li1.extend(li2)
# print(li1)





#Basic of Matrix
#my_list = [
#    [1,2,3],
#    [0.1,837j],      #It's called nested list/matrix
#    "adi"
#]
#print(my_list)






#learning Tuple in depth
#my_tuple = (1, 2.3, "adi", 123j, True)    #It's an immutable data type.
#print(type(my_tuple), my_tuple)

#accecing tuple's index
#print(my_tuple[2])
#print(my_tuple[-1])
#print(my_tuple[2:5])



#Update Tuples
# ThisTuple = ("Aditya", "Ayesha", "Ronobir")
# print(ThisTuple)
# a = list(ThisTuple)
# a.append("Faiza")
# ThisTuple = tuple(a)
# print(ThisTuple)



#Unpack Tuples         we can also Unpack Lists

'''mytup = ("apple", "banana", "Aditto", "cherry")
(a, *b, c) = mytup
print(b)'''




#loop tuple

new_tuple = ("Aditya", "Arnob", "Ronobir", "Ayesha", "Ankan", "Zaiyan")

#using for loop, range and len function...
'''for loop in new_tuple:
    print(loop)

for i in range(len(new_tuple)):
    print(i)'''


#using while loop...
'''i = 0
while i < len(new_tuple):
    print(new_tuple[i])
    i += 1'''





#Join tuples
'''num1 = ("a", "b", "c")
num2 = (1,2,3)

num3 = num1 + num2
print(num3)'''


#multiply tuples
'''my_tuple = ("aditto", 29, 13.5, 2008j)
multiply = my_tuple*2
print(multiply)'''




#Tuple methods
'''friends = ("Aditya", "Ayesha", "Ronobir", "Arnab", "Aditya")
indexing = friends.index("Ayesha")
print(indexing)

counting = friends.count("Aditya")
print(counting)'''













#Python Sets         *A set is a collection which is unordered, unchangeable*, and unindexed.


'''my_set = {1, 1.2, 98j, "adi", 1}
print(type(my_set))
print(len(my_set))
print(my_set)'''



#Access Set Items
'''Myset = {1,2,"3",3,6}

for i in Myset:
    print(i)

print("adi" in Myset) #As "adi" is not in the Set so the output will be False
print("3" in Myset) #As "3" is in the Set so the output will be True'''





#Add Sets Items

#add method
'''my_set1 = {"Aditya", "Arnab", "Zaiyan", "Ankan"}
my_set1.add("Apurbo")
print(my_set1)'''

#update method
'''my_set1 = {"Aditya", "Arnab", "Zaiyan", "Ankan"}
my_set2 = {"Apurbo", "Arhan"}
my_set1.update(my_set2)
print(my_set1)'''





#Remove Sets Items

'''#using remove method
myset = {1, 2, 3, 4, 5, 6}
myset.remove(4)
print(myset)

#using discard method
myset.discard(10)
print(myset)

#using pop method
myset.pop() #we don't know which item gots remove
print(myset)

#using clear method
myset.clear()
print(myset)'''




#Loop Sets
'''myset = {1, 2.3, 68j, "adi"}

for loop in myset:
    print(loop)

for loop in range(len(myset)):
    print(loop)'''




#Join Sets
'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

#We can also use update method..And I also prefer UPDATE method
set3 = set1.union(set2)
print(set3)'''















# PYTHON Dictionary..       changeable, ordered and indexed

'''student_info = {
    "Aditya" : {
        "Roll" : 29,
        "Location" : "Rajshahi",
        "Id no" : "2402" 
    },
    "Ayesha" : {
        "Roll" : 46, 
        "Location" : "Rajshahi",
        "Id no" : "2403"
    }
}'''

# student_name = input("Enter the name of the student: ")


# if student_name in student_info:
#     print(student_info[student_name])
# else:
#     print("Sorry! We didn't find the student you are searching for")






#Accessing Items

'''my_dict = {
    "name" : "Aditya",
    "Roll" : 29,
    "School" : "Rajshahi University School",
    "Id" : 136
}

print(my_dict["name"])

print(my_dict.get("Roll"))

print(my_dict.keys())

print(my_dict.values())

print(my_dict.items())'''



#Change dictionary items

'''student_info = {
    "Aditya" : {
        "Roll" : 29,
        "Location" : "Rajshahi",
        "Id no" : "2402" 
    },
    "Ayesha" : {
        "Roll" : 46, 
        "Location" : "Rajshahi",
        "Id no" : "2403"
    }
}


#Using = operator
student_info["Ayesha"]["Location"] = "Dhaka"
print(student_info["Ayesha"]["Location"]) 

#Using update() method
student_info["Aditya"].update({"Location" : "Dhaka"})
print(student_info["Aditya"]["Location"]'''





#Add & remove items

# ADD
'''Aditya = {
    "Name" : "Aditya Banerjee",
    "Roll" : 29,
    "Class" : 7,
    "Section" : "B"
}

Aditya["Id number"] = 2402

Aditya.update({"color": "red"})
print(Aditya)



# REMOVE
Aditya.pop("Id number")

Aditya.popitem()

del Aditya["Section"]

Aditya.clear()
print(Aditya)

#del Aditya #this will cause an error because "thisdict" no longer exists.
#print(Aditya)'''





#Loop dictionary

'''student_info = {
    "Name" : "Aditya Banerjee",
    "Roll" : 29,
    "Ayesha" : {
        "Class" : 7,
        "Section" : "B"
    }
}


for a in student_info:
    print(a)

for b in student_info.values():
    print(b)

for c in student_info.keys():
    print(c)

for d in student_info.items():
    print(d)'''




#Copy dictionary

'''dict1 = {
    "Aditya" : 29,
    "Ayesha" : 48,
    "Arnab"  : 58,
    "Ankan"  : 72
}
print(dict1)

#Using copy method
dict2 = dict1.copy()
print(dict2) 

#Using dict function
dict3 = dict(dict1)
print(dict3)'''











#If else

#conditions & statments

'''a = 80
b = 80
if a > b:
    print("a is greater than b")
elif a == b:
    print("The value of a and b is some")
else:
    print("a is not greater than b")'''






#Python Loop and Break and Continue keywords

'''#While loop
i = 0
while i < 5:
    print(i)
    i += 1

#For loop
fruits = ["apple", "banana", "cherry"]
for n in fruits:
    if n == "cherry":
        break
    print(n)

#Break
for x in range(10):
    if x == 5:
        break
    print(x)

#Continue
for x in range(10):
    if x == 2:
        continue
    print(x)'''










#Python Function

'''def number(a,b):
    sum = a + b
    print(sum)

number(10,10)'''
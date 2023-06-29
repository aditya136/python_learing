# #print('23')
#''' a alkjd '''
#print(24)



#learning input function 
#name = input("What's your name?: ")
#print( "hello " + name  )




#just for fun-
#x = 0
#while x < 100:
#    print(x)



#just for fun-- 
#print("Give the answers of the maths")
#x = input("1st question-  23 + 16?: ")
#if x == 39:
#    print("Your 1st answer is corret")
#else: 
#    print("Your 1st answer is wrong. The correct one is- ", 23 + 16)
#This code doesn't work as I want....I guess I need a bit more knowledge😊








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

#your_name = "I don't know"
#print(MyName + your_name)

#print("My name is" + " " + MyName)







#learning boolean data type
#bool = True
#print(bool)
#print(type(bool))

#z = 10
#x = 8
#print(x < z)






#string formatting
#num1 = 12
#num2 = 20

#print(f"This is my super numebr {num1 + num2}")
#print(type(f"{10-5}"))






#learning bynary type data

#bytes
#hablulist = [1,2,3,54,5,41,2,121,255]
#b = bytes(hablulist)
#print(bytes(hablulist))
#print(type(b))
#b[0] = 10   #bite is immutable

#bytearrays
#hablulist = [1,2,3,54,5,41,2,121,255]
#b = bytearray(hablulist)
#print(bytes(hablulist))
#print(type(b))
#b[0] = 10   #bytearray is mutable




#learning none type data
#x = None
#print(x)
#print(type(x))







#learning the bacises of list, tuple and range type data

#list type data        is mutable
#li = ['Aditya', "Arnob", "Ankan", 'Zaiyan']
#li[0]= "Name-has-changed"
#print(li)
#print(type(li)) 

#tuple type data       is immutable
#tup = ('Aditya', "Arnob", "Ankan", 'Zaiyan')
#print(tup)
#print(type(tup))

#range type data
#ran = range(6)
#print(ran)
#print(type(ran))

#a little bit for loop😁
#for i in ran:
#    print(i)







#Python operators

#arithmetic operators
#a = 10
#b = 20
#print(a + b)#ad dition
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
# sum = d + 5  #d + 5 si assigned in the variable called sum
# print(sum) #At present sum's value is 10

# sum += 1
# print(sum)#At present sum's value is 11

# sum -= 1
# print(sum)#At present sum's value is 10

# sum *= 2
# print(sum)#At present sum's value is 20

# #I have to comment this↓ befor using the floor division equeal(//=) sing....Other wise it won't work
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
# a = 2
# b = 5
# print(a < b and a > b)
# print(a < b or a > b)
# print(not(a < b))





#learning swapping
#int swapping
# c = 50
# d = 60
# c,d = d,c #swapping
# print("This value is now c", c)
# print("This value is now d", d)

#float swapping
# c = 1.2
# d = 2.1
# c,d = d,c
# print("This value is now c", c)
# print("This value is now d", d)

#str swapping
# c = "it's c"
# d = "it's d"
# c,d = d,c
# print("This value is c", c)
# print("This value is d", d)

#complex swapping
# c = 23j
# d = 32j
# c,d = d,c
# print("This value is c", c)
# print("This value is d", d)





 
#learning user input
# user_name, password = input("Enter your username: "), input("Enter your password: ")
# print("Hello", user_name + "." + "   " + "Your password is", password)






#learning type casting
# string_type_data = "123"
# print(type(int(string_type_data)))
# print(string_type_data)
# print(type(float(string_type_data)))
# print(float(string_type_data))












#learning python list in depth 
# li = [1, 2, 3]
# #print(type(li))
# li[1] = 10#change list's value
# print(li)
#Experiments
# li2 = ["Aditya", "Arnob", "Ankan", "jaiyan", "Apurbo"]
# li2[3] = "Zaiyan"
# li2[0] = 29
# li2[1] = 89j #change list item
# li2[2] = 12.3
# li2[4] = True
# print(li2)
# print(type(li2[0]))
# print(type(li2[1])) #print specific index/value
# print(type(li2[2]))
# print(type(li2[3]))
# print(type(li2[4]))

#Wow we can also take variables as a list item
# str_var = "adi"
# int_var = 12
# float_var = 1.2
# complex_var = 12j
# bool_var = False
# all_var = [str_var, int_var, float_var, complex_var, bool_var]
# print(all_var)

#list item add or remove
#li = ["Aditya", 12, 1.2, 12j, True]
#print(li)
# li.append("Adding a new thing")
# li.append(13)
# li.append(12j)
# print(li)

# li.insert(1, 2.2)
# li.insert(0, False)
# print(li)




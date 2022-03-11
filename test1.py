import imp
import this
from tokenize import Double
import random

msg = "hello Opu"

fruits= [10,2,3,4]

print(type(msg))
print(msg)

#####if else condition#####

if(2>5):
    print("5 is greater than 2")
else:
    print("2 is less than 5")

x = str(3)
print(x)
y= int(10)

z= float(4.0)
print(z)


###class type dict###

x= {"name": "Aminul islam", "Age": 24}

print(x)
print(x["name"])
print(x["Age"])


####random number#######

print(random.randrange(1,10))

####casting ########

x= "190"
a= int(222)

y= int(x)
z= float(a)
print(y)
print(z)

####slicing ########

abc= " Hello, World! "

print(abc[-7:-1])
print(abc[2:5])
print(abc[:-1])


### Modify Strings ###

print(abc.upper())
print(abc.lower())
print(abc.replace('W',"S"))
print(abc.strip())
print(abc.split(","))

print(abc+ " : "+ msg)


##### Format - Strings ####

a,b,c= 10,20,30

text1= "opu has {} sweety has {} ayat has {} tk" 
text2= "opu has {1} sweety has {0} ayat has {2} tk" 

print(text1.format(a,b,c))
print(text2.format(a,b,c))


##### List #####

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(thislist))
print(thislist[-1])
print(thislist[2:5])

if "apple"  in thislist:
    print("yes, apple in thislist")

thislist[1]= "blackchart"
print(thislist)

## To add an item to the end of the list, use the append() method:
thislist.append("orange")
print(thislist)

##To insert a list item at a specified index, use the insert() method.

thislist.insert(1,"sweet")
print(thislist)


## To append elements from another list to the current list, use the extend() method.

list2= ["hello","world"]
thislist.extend(list2)
print(thislist)

## Add elements of a tuple to a list:

list3= ("opu", "dipu")
thislist.extend(list3)
print(thislist)


### The remove() method removes the specified item.

thislist.remove("apple")
print(thislist)

thislist.pop(0)
print(thislist)

### Remove the last item:
thislist.pop()
print(thislist)


#######  Loop Through a List ########

for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i =0
while i < len(thislist):
    print(thislist[i])
    i=i+1



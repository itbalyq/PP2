thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print(thislist[-1])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


newlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(newlist[2:5])



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
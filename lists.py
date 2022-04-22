# lists: ordered, mutable, allows duplicates

mylist = [4, True, "apple", "apple"] # no type restriction
item = mylist[0] # access first item in list
# indexerror = mylist[10] # out of range throws an error
negativeitem = mylist[-2] # starts counting from -1

for i in mylist:
    print(i)
# we don't seem to need "end"

if "apple" in mylist:
    print("yes")
else:
    print("no")

len(mylist) # length method
mylist.append("lemon") # append method (like ruby shovel)
apple1 = mylist.pop() # same as other pop methods, removes
mylist.remove(True) # targeted removal, throws error if item not in list
mylist.reverse() # flip-flop the order
mylist.sort() # sort-in-place, changes original
newlist = sorted(mylist) # leaves original unchanged, generates new sorted list
mylist.clear() # yup

listgen = [0] * 5 # to get a list of 5 zeroes
list1 = [1, 2, 3, 4, 5] # could probably automatically generate this with a loop
list2 = listgen + list1 # concats

a = list1[2:5] # slices from index 2 to index 5, right side open [2,5)
b = list1[1:] # goes to the end
c = list1[1::1] # goes to the end by steps (1, in this case)
d = list1[::-1] # same as reverse()

# assignments don't pass references, it identifies them.
# example:
listA = ["foo", "bar"]
listB = listA
# now these are pointing to the same list.
listB = listA.copy() # leaves original as a distinct object
listC = listA[:] # full "slice", makes a copy

numlist1 = [1, 2, 3, 4, 5, 6]
numlist2 = [i*i for i in numlist1] # generates a new list of squares, using "list comprehension" (seems haskellish)
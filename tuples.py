# ordered, immutable, allows duplicates

mytuple = ("Jo Anne", 37, "Juneau")
noparens = "Jo Anne", 37, "Juneau" # don't need parentheses

this_is_a_string = "Doot"
this_is_a_tuple = "Doot",

print(type(this_is_a_tuple)) # yup

indexing = mytuple[0] # starts counting at zero
# as with lists, index error for out of range calls
# other indexing is identical also

mytuple[0] = "Blerp" # throws an error

for i in mytuple:
    print(i)

if "Juneau" in mytuple:
    print("asdfasdfasdf")
else:
    print";lkj;lkj;lkj;lkj"
# pretty usual stuff here

# length, index, slicing, all non-modifying methods work as expected

mylist = list(noparens) # converts a tuple to a list
newtuple = tuple(mylist) # converts a list to a tuple
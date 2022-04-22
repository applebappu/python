# dictionaries are key-value pairs, unordered, mutable
# kind of like an Array in Ruby, or a Table in Lua (if you're using custom keys)

mydict = {
    "name": "Jo Anne",
    "age": 37,
    "city": "Juneau"
    }

newdict = dict(name = "Jo anne", age = 37, city = "Juneau") # with dict(), no quotes needed

value = mydict["name"] # index by the indexes. makes sense
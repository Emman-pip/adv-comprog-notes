# Lists
- lists in python are used to store multiple items in a single value
- since python is **dynamically typed**, a list can hold elements with different data types
- lists are **mutable, allow duplicates, and ordered data** structures
	- ordered means that list items have a defined order
	- mutable means that the items inside can be changed, added, or removed after its been created
```python
# list containing numbers
thisList = [1,2,3,4]

# list containing different data types
anotherList = ["Hello world", 1, 1.232323, 100000, 'a']

# list items can be accessed using indexes
thisList[0] # returns 1
thisList[1] # returns 2

# gets the length of the list
len(thisList) # returns 4

# other list-like data types, such as tuple and sets, can be casted as lists
immutableList = (1,2,3,4)
list(immutableList) # returns immutableList as a list
```

## List methods
- list.append(list-item-here)
	- receives one argument to append to the end of the list
- list.copy(list-here)
	- used to copy the array to another variable (shallow copy)
- list.extend(iterable-here)
	- used to extend an array
- list.insert(index-here, item-here)
	- used to insert items at a specific index
- list.pop()
	- remove and return the last item
- list.reverse
	- sorts the array in a reverse order
- list.clear
	- removes all the items in the array
- list.count(item-here)
	- counts the occurrences of the item specified in the list
- list.index
	- search the index of the first instance of the searched term
- list.remove(item-here)
	- removes the first occurrence of the first matching item in the array
- list.sort()
	- sorts the array in ascending order

# Tuples
- tuple is a collection which is **ordered and immutable.**
- **allows duplicates**
```python
sampleTuple = (1,2,3,4)
```
# Dictionary
- is a collection which is **ordered and changeable**
- **no duplicate keys**
- key-value pairs
```python
sampleDictionary = {1: "first item", 2: "second item", 3:"third item"}
```
# Set
- unordered collection of unique elements
- **no duplicate members**
```python
sampleSet = {1,2,3,4}
```

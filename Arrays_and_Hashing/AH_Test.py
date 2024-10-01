from AH_Function import *

my_hash_set = MyHashSet() # Initialize an empty hashset ("Empty but in fact it is prefilled to size 10")
my_hash_set.add(3.141592652)
my_hash_set.add(3.141592652) # this number is already added
my_hash_set.add(-934)
print(my_hash_set.has(3.141592652)) # returns True
print(my_hash_set.has(2024)) # returns False
my_hash_set.remove(3.141592652)
my_hash_set.remove(2.73) # this number is not in the hashset
print(my_hash_set) # Prints memory address of the hashset
my_hash_set.print() # Prints the hashset

my_dict = MyDict() # Initialize an empty dictionary ("Empty but in fact it is prefilled to size 10")
my_dict.assign(1, 10)
my_dict.assign(2, 20)
my_dict.get(1) # returns 10
my_dict.get(3) # returns -1 (not found)
print(my_dict) # Prints memory address of the dictionary
my_dict.print() # Prints the dictionary
"""
- We will need to use one of python's built-in functions called 'hash()'
- hash() function is used to convert a value into a hash value which is used for quick comparison of dictionary keys during a dictionary lookup.
- The hash() function returns the hash value of the object if it has one.
"""

# Using the hash() function
# print(f"Hash value of 3.141592652: {hash(3.141592652)}")
# print(f"Hash value of 'hello': {hash('hello')}")
# print(f"Hash value of (1, 2, 3): {hash((1, 2, 3))}")
# print(f"Hash value of [1, 2, 3]: {hash([1, 2, 3])}") Note that the hash function does not work on mutable objects like lists, sets, and dictionaries.

# Creating hashset class
class MyHashSet:
    def __init__(self, size=10): # Constructor to initialize the hashset
        self.size = size
        self.buckets = [[] for _ in range(size)] # Creating a list of empty lists to store the elements of the hashset
        # Having a list of lists will allow us to store multiple elements in the same bucket to avoid collisions

    def myhash(self, key):
        # This function will compute a value store a large hash value in a small bucket
        # e.g. hash('apple') = 3297408422841, while the size of the hashset is only 10, so by using the modulo operator, we can store the value in a small bucket
        return hash(key) % self.size

    def has(self, key):
        # This function will check if the key is in the hashset
        index = self.myhash(key) # Call myhash function to get the index
        return key in self.buckets[index]

    def add(self, key):
        index = self.myhash(key)
        # This function will add the key to the hashset
        if key not in self.buckets[index]:
            self.buckets[index].append(key)
        else:
            print(f"{key} already exists in the hashset")

    def remove(self, key):
        # This function will remove the key from the hashset if it exists
        index = self.myhash(key)

        if key in self.buckets[index]:
            self.buckets[index].remove(key)
        else:
            print(f"{key} not found in the hashset")

    def print(self):
        # This function will print the hashset
        for bucket in self.buckets:
            print(bucket) if bucket else None


# Now we will build a dictionary class
class MyDict:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # Initialize buckets

    def myhash(self, key):
        return hash(key) % self.size  # Hash function

    def assign(self, key, value):
        index = self.myhash(key)

        # Check if the key exists in the dictionary
        for pair in self.buckets[index]:
            if pair[0] == key:  # If key exists, update the value
                pair[1] = value
                return  # Exit after updating

        # If key does not exist, append the new key-value pair
        self.buckets[index].append([key, value])

    def get(self, key, default=None):
        index = self.myhash(key)

        # Check if the key exists in the dictionary
        for pair in self.buckets[index]:
            if pair[0] == key:  # If key is found, return its value
                return pair[1]

        # If the key is not found
        print(f"{key} not found in the dictionary")
        if default is not None:
            self.assign(key, default)  # Assign default value if specified
            return default
        else:
            return None  # Return None if not found

    def delete(self, key):
        index = self.myhash(key)

        # Check if the key exists in the dictionary
        for pair in self.buckets[index]:
            if pair[0] == key:  # If key is found, remove it
                self.buckets[index].remove(pair)
                return  # Exit after deletion

        print(f"{key} not found in the dictionary")  # If key is not found

    def has(self, key):
        index = self.myhash(key)

        # Check if the key exists in the bucket
        for pair in self.buckets[index]:
            if pair[0] == key:  # If key is found, return True
                return True
        return False  # Return False if key is not foun


    def print(self):
        # Print the dictionary
        for bucket in self.buckets:
            for pair in bucket:
                print(pair)

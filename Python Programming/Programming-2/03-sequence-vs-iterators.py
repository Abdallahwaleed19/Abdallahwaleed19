
# Sequence vs Iterator in Python
# Both sequences and iterators are fundamental concepts in Python, but they serve different purposes and have distinct behaviors.

# What is a Sequence?
# A sequence in Python is a collection of items arranged in a specific order. Sequences support indexing and slicing,
# allowing access to individual elements or subsets of elements. Common sequence types include lists, tuples, strings, 
# and ranges.

# Characteristics of a Sequence:-

# Indexable: Elements can be accessed using their indices.
my_list = [10, 20, 30]
print(my_list[1])  # Output: 20


# Slicable: You can retrieve subsets of elements using slicing.
print(my_list[0:2])  # Output: [10, 20]

# Common Sequence Types
# List: Mutable, ordered collection of elements.
# Tuple: Immutable, ordered collection.
# String: Immutable, ordered sequence of characters.
# Range: Immutable, ordered sequence of numbers.


# What is an Iterator?
# An iterator in Python is an object that represents a stream of data. It produces elements one at a time and does not 
# necessarily store them in memory. Iterators are often used to handle large data sets or infinite streams.

# Characteristics of an Iterator
# Lazy Evaluation: Iterators compute elements on demand, conserving memory.
# No Indexing: You cannot directly access elements by index.
# One-Time Traversal: Once an iterator is exhausted, it cannot be reused without recreating it.

# How Iterators Work
# Iterators implement the __iter__ method (returns the iterator object) and the __next__ method (returns the next element or 
# raises StopIteration when the iterator is exhausted).

# Example
my_list = [1, 2, 3]
iterator = iter(my_list)  # Create an iterator

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # Raises StopIteration



# Sequence as Iterable
# A sequence is inherently iterable, meaning it implements the __iter__ method. When you iterate over a sequence, 
# Python internally creates an iterator for that sequence.

my_list = [10, 20, 30]

for item in my_list:  # Creates an iterator internally
    print(item)
    


# Iterator Use Cases
# Streaming Data:   
    
def infinite_numbers():
    n = 1
    while True:
        yield n
        n += 1

numbers = infinite_numbers()
print(next(numbers))  # Output: 1
print(next(numbers))  # Output: 2



# Converting Between Sequence and Iterator
# Sequence to Iterator:
# Use the iter() function to convert a sequence into an iterator.

my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # Output: 1


# Iterator to Sequence:
# Use a constructor like list(), tuple(), or set() to convert an iterator into a sequence.

iterator = iter([1, 2, 3])
new_list = list(iterator)
print(new_list)  # Output: [1, 2, 3]
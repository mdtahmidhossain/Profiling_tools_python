### Pure Python Optimizations
List vs Deque
![List](https://github.com/mdtahmidhossain/Profiling_tools_python/raw/main/images/list.png)
![Deque](https://github.com/mdtahmidhossain/Profiling_tools_python/raw/main/images/deque.png)

### bisect module
The **bisect** module in Python is a built-in module that provides support for performing binary searches in sequences such as lists. The bisect module is often used to search for the position of an element in a sorted list or to insert an element into a sorted list in the correct position to maintain the sorted order.

The bisect module provides two main functions: bisect_left and bisect_right. The **bisect_left** function finds the position in a sorted list where an element should be inserted to maintain sorted order, while **bisect_right** returns the index of the first element greater than the search value.

Here's an example of using the bisect module to find the position of an element in a sorted list:
```python
import bisect

numbers = [1, 2, 4, 5, 7, 8, 9]

position = bisect.bisect_left(numbers, 5)

print(position) # Output: 3

```

In this example, the **bisect_left** function returns the position **3**, which is the index of the **5** in the **numbers** list.

Here's an example of using the bisect_right function from the bisect module in Python:
```python
import bisect

numbers = [1, 2, 4, 5, 7, 8, 9]

position = bisect.bisect_right(numbers, 5)

print(position) # Output: 4

```

In this example, the **bisect_right** function returns the position **4**, which is the index of the first element greater than **5** in the **numbers** list (**7**).

Note that if you search for an element that is greater than any element in the list, the bisect_right function will return the length of the list, which is equivalent to appending the new element to the end of the list.

In summary, the bisect module in Python provides support for performing binary searches in sequences such as lists. The bisect module provides two main functions: bisect_left and bisect_right, which can be used to find the position of an element in a sorted list or to insert an element into a sorted list in the correct position to maintain the sorted order.
![Bisect](https://github.com/mdtahmidhossain/Profiling_tools_python/raw/main/images/bisect.png)

### Counter
The **Counter** class in Python is a built-in class that provides an efficient way to count the occurrences of elements in a collection. The Counter class is a subclass of the **dict** class and provides additional functionality for counting elements, such as methods for accessing the count of an element and finding the most common elements in a collection.
```python
from collections import Counter

numbers = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9, 9, 9, 9]

counts = Counter(numbers)

print(counts) # Output: Counter({9: 4, 7: 3, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 8: 1})

print(counts[7]) # Output: 3


```

### inverted index
An inverted index is a way of organizing information about the words (or terms) in a collection of text documents so that you can quickly look up which documents contain a particular word. The term "inverted" refers to the fact that the index is organized with the words as the keys and the documents as the values, which is the opposite of the traditional way of organizing information about documents.

Here's an example implementation of an inverted index in Python 3:
```python
from collections import defaultdict

# A list of documents
docs = [
    "the cat is under the table",
    "the dog is under the table",
    "cats and dogs smell roses",
    "Carla eats an apple"
]

# Create an empty inverted index
inverted_index = defaultdict(list)

# Loop over each document
for doc_id, doc in enumerate(docs):
    # Split the document into words
    words = doc.split()
    # Loop over each word in the document
    for word in words:
        # Add the document ID to the inverted index for the word
        inverted_index[word].append(doc_id)

# Print the inverted index
print(dict(inverted_index))

```
The output of this code will be:
```python
{
    "the": [0, 1],
    "cat": [0],
    "is": [0, 1],
    "under": [0, 1],
    "table": [0, 1],
    "dog": [1],
    "cats": [2],
    "and": [2],
    "dogs": [2],
    "smell": [2],
    "roses": [2],
    "Carla": [3],
    "eats": [3],
    "an": [3],
    "apple": [3]
}

```
In this example, the inverted index is stored as a dictionary where each key is a word (or term) and each value is a list of document IDs that contain that word. You can use the inverted index to quickly find which documents contain a particular word.

You can use this inverted index by searching for a specific word in the dictionary and retrieving the list of document IDs associated with that word. Here's an example:
```python
# Search for the word "table" in the inverted index
if "table" in inverted_index:
    table_docs = inverted_index["table"]
    print("The word 'table' appears in documents:", table_docs)
else:
    print("The word 'table' does not appear in any documents.")

```
The output of this code will be:
```python
#The word 'table' appears in documents: [0, 1]

```
This means that the word "table" appears in documents with IDs 0 and 1. You can then retrieve the actual document text by using the document ID to index the docs list:
```python
print("Document 0:", docs[0])
print("Document 1:", docs[1])

```
### dictionary
A dictionary in Python 3 is an unordered collection of key-value pairs. It allows you to store and access data using a key, which can be any hashable object, instead of an index. Dictionaries are used to store and retrieve values based on a key, and are often used when working with large amounts of data.

### set
A set in Python 3 is a collection of unique elements without any specific order. It is useful for performing operations like union, intersection, and difference.

| Operation | Time Complexity |
|-----------|-----------------|
| Membership test (`x in s`)  | O(1) (sets, dictionaries)<br>O(n) (lists) |
| Adding an element (`s.add(x)`)  | O(1) (sets)<br>O(n) (lists) |
| Removing an element (`s.remove(x)`)  | O(1) (sets)<br>O(n) (lists) |
| Union (`s1 + s2`)  | O(min(len(s1), len(s2))) |
| Intersection (`s1 & s2`)  | O(min(len(s1), len(s2))) |
| Difference (`s1 - s2`)  | O(len(s1)) |

### Here is a more detailed table comparing the differences between sets and dictionaries in Python 3:
| Feature | Set | Dictionary |
|---------|-----|-----------|
| Definition | An unordered collection of unique elements | An unordered collection of key-value pairs |
| Element Insertion | `set.add()` or `{element1, element2, ...}` | `dict[key] = value` or `{key1: value1, key2: value2, ...}` |
| Element Access | `in` operator | Key |
| Element Modification | Cannot modify individual elements | Modify values associated with keys |
| Element Removal | `set.remove()` or `set.discard()` | `del dict[key]` |
| Built-in Functions | `len()`, `min()`, `max()`, `sorted()` | `len()`, `del`, `clear()`, `get()`, `keys()`, `values()`, `items()` |


### Improvement of Inverted index using set:

The use of set operations in the context of building an inverted index, which is a data structure used to efficiently support text search.

The idea is that we start by splitting each document into individual words, and then build a dictionary where each word is associated with a set of document indices that contain that word. The set of indices is represented as a Python set object.

Once we have built the inverted index, we can then use set operations (such as the intersection method) to efficiently answer Boolean queries. For example, we can find all documents that contain both the words "cat" and "table" by intersecting the sets of document indices associated with each word.
```python
index = {}
for i, doc in enumerate(docs):
    for word in doc.split():
        if word not in index:
            index[word] = {i}
        else:
            index[word].add(i)

result = index['cat'].intersection(index['table'])

```

### Heap
A heap is a data structure used in computer science for organizing and storing data efficiently. It is called a "heap" because it resembles a heap of elements, with the largest (or smallest) element at the top and the rest of the elements branching downwards.

Here are a few reasons why we might need a heap:

- Efficient access to the largest (or smallest) element: In a max heap, the largest element is always at the root of the heap, making it easy to access and extract. Similarly, in a min heap, the smallest element is always at the root.
- Priority Queue: Heaps can be used to implement priority queues, where elements with higher priority (or lower value) are given priority over elements with lower priority (or higher value).
- Sorting Algorithm: Heapsort is a comparison-based sorting algorithm that uses a max heap to sort an array of elements.
- Dynamic Programming: Heaps are used in various dynamic programming algorithms such as Dijkstra’s algorithm and Prim’s algorithm.
- Efficient Data Management: Heaps are efficient for inserting and deleting elements, as well as for maintaining the order of elements. This makes them useful for data management in various applications

```python
import heapq

# Create a list of elements
elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Convert the list into a heap
heap = list(elements)
heapq.heapify(heap)

# Print the heap
print("Heap:", heap)

# Use heap operations

# Add an element to the heap
heapq.heappush(heap, 8)
print("After pushing 8:", heap)

# Remove the smallest element from the heap
smallest = heapq.heappop(heap)
print("Smallest element:", smallest)
print("After popping:", heap)

# Get the smallest element without removing it from the heap
smallest = heap[0]
print("Smallest element:", smallest)

```
| Operation | Function |
|-----------|----------|
| Convert list to heap | heapq.heapify(list) |
| Add element to heap | heapq.heappush(heap, element) |
| Remove smallest element from heap | heapq.heappop(heap) |
| Get smallest element in heap | heap[0] |

### What is Tries?

Tries, also known as prefix trees, are a tree-based data structure that is used to store an associative array where the keys are sequences (usually strings). Tries are most commonly used to store a dictionary of words, where each node in the tree represents a single character in a word.
### Why is Tries Needed?

Tries are a very efficient data structure for certain tasks. For example, searching for a word in a trie is much faster than searching for the same word in a large array or list. Tries are also very useful for finding all words that start with a certain prefix, making them useful for tasks such as autocompletion.
### Tries Operations in Python 3

The python **collections** module includes a **defaultdict** class that can be used to implement tries. Here is an example of a basic trie implementation using a defaultdict:
```python
from collections import defaultdict

class Trie:
    def __init__(self):
        self.root = defaultdict()

    def add(self, word):
        current_node = self.root
        for letter in word:
            current_node = current_node.setdefault(letter, {})
        current_node['*'] = True

    def exists(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return '*' in current_node

```
**Input**
```python
trie = Trie()
trie.add('hello')
trie.add('hell')
trie.exists('hello')
trie.exists('hell')
trie.exists('he')

```
**Output**
```python
True
True
False

```
[![IMAGE ALT TEXT](http://img.youtube.com/vi/giiaIofn31A/0.jpg)](http://www.youtube.com/watch?v=giiaIofn31A "Trie Data Structure Implementation (LeetCode)")

### Caching and memoization
**lru_cache** is a decorator provided by the functools module in Python. It is used to cache the results of a function so that they can be reused later. The cache is limited by size, and when it reaches its limit, the least recently used items will be removed to make room for new items. The purpose of the lru_cache is to speed up your program by avoiding the need to recompute the same values over and over again.

Here is an example of how you might use the lru_cache to cache the results of a function that computes the factorial of a number:
```python
import functools

@functools.lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # Output: 120
print(factorial(5)) # Output: 120 (cached result)

```
In this example, the **factorial** function is decorated with the **functools.lru_cache** decorator, which sets the maximum size of the cache to **None**, meaning that the cache has no limit. The first time the function is called with **n=5**, it will compute the factorial and store the result in the cache. The second time the function is called with **n=5**, it will simply return the cached result, avoiding the need to recompute the factorial.

### Joblib
Joblib is a library in Python that is used for running parallel computing tasks. It is designed to be fast and memory-efficient, and it is particularly useful for processing large data sets that take a long time to run.

An example use case for Joblib would be if you have a large data set that you want to process and it takes a long time to run on a single machine. With Joblib, you can break down the data set into smaller chunks and run each chunk on a separate machine or process, allowing you to process the data much more quickly.

Here is a simple example of how you can use Joblib in Python:

```python
from joblib import Parallel, delayed
import numpy as np

def process_data(data):
    return data * 2

def main():
    data = np.arange(1000)
    results = Parallel(n_jobs=-1)(delayed(process_data)(d) for d in data)
    print(results)

if __name__ == '__main__':
    main()

```
In this example, we are using the **Parallel** class from Joblib to run the **process_data** function in parallel on all elements of the **data** array. The **n_jobs** parameter specifies the number of parallel jobs to run, and a value of -1 means to use all available cores. The **delayed** function is used to wrap the **process_data** function so that it can be run in parallel. The resulting **results** array contains the processed data from each parallel job.

Joblib is a library in Python that provides an on-disk cache. This cache can be used to memoize functions, meaning that their results are stored and can persist between runs. This library is particularly useful in scientific and engineering applications, as it provides efficient memoization of functions that operate on numpy arrays.

To use joblib, the module must be installed using the pip install joblib command. Once installed, the Memory class can be used to memoize functions using the Memory.cache decorator. For example, the code below shows how to use joblib to memoize a function that calculates the sum of two numbers:

```python
from joblib import Memory
memory = Memory(cachedir='/path/to/cachedir')

@memory.cache
def sum2(a, b):
    return a + b

```
In this example, the function **sum2** will behave similarly to lru_cache. The results will be stored on-disk in the directory specified by the **cachedir** argument during the Memory initialization, and the cached results will persist over subsequent runs. The **Memory.cache** method also allows limiting recomputation only when certain arguments change. Additionally, the decorated function supports basic functionalities such as clearing and analyzing the cache.
### yield
The **yield** keyword in Python is used to create generator functions, which are functions that can be used to generate an iterable sequence of values. Unlike a normal function, a generator function will pause its execution and return a value whenever it encounters a yield statement. The next time the generator function is called, it will resume execution from where it left off and continue until it reaches the next yield statement or the end of the function. This makes generator functions a more memory-efficient alternative to creating a list of values, as the generator only generates one value at a time, rather than creating a list of all values up front.

Here's a simple example that demonstrates the use of the yield keyword:
```python
def fibonacci_sequence(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

# Use the generator function to generate the first 10 terms of the fibonacci sequence
fib = fibonacci_sequence(10)
for num in fib:
    print(num)

```
This will output the following values:
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    
### Comprehensions and generators
Comprehensions and generators are two different techniques in Python for generating new sequences or collections of data.

Comprehensions are a concise way of creating new lists, dictionaries, and sets by processing an existing iterable (e.g. list, tuple, string, etc.) and applying a set of rules to each element. For example, the following code uses a list comprehension to create a new list that squares each number in an existing list:
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers) # [1, 4, 9, 16, 25]

```
Generators, on the other hand, are a way to generate an iterable sequence by using a function that yields one value at a time. Unlike comprehensions, generators do not generate a complete sequence in memory at once, but instead generate values one by one on-the-fly as they are needed. For example, the following code uses a generator function to generate an iterable sequence of even numbers:
```python
def even_numbers(limit):
    number = 0
    while number < limit:
        yield number
        number += 2

for num in even_numbers(10):
    print(num) # 0, 2, 4, 6, 8

```
```python
def loop():
    res = []
    for i in range(100000):
        res.append(i * i)
    return sum(res)

def comprehension():
    return sum([i * i for i in range(100000)])

def generator():
    return sum(i * i for i in range(100000))

print("loop:", %timeit loop())
print("comprehension:", %timeit comprehension())
print("generator:", %timeit generator())

def loop():
    res = {}
    for i in range(100000):
        res[i] = i
    return res

def comprehension():
    return {i: i for i in range(100000)}

print("loop:", %timeit loop())
print("comprehension:", %timeit comprehension())

def map_comprehension(numbers):
    a = [n * 2 for n in numbers]
    b = [n ** 2 for n in a]
    c = [n ** 0.33 for n in b]
    return max(c)

def map_normal(numbers):
    a = map(lambda n: n * 2, numbers)
    b = map(lambda n: n ** 2, a)
    c = map(lambda n: n ** 0.33, b)
    return max(c)

numbers = range(1000000)
print("map_comprehension peak memory:", %memit map_comprehension(numbers))
print("map_normal peak memory:", %memit map_normal(numbers))

```
In this code, we are exploring the use of comprehensions and generators to speed up and improve the memory usage of Python loops. We start by comparing the speed of a loop, a list comprehension, and a generator expression using the **%timeit** function. Next, we compare the speed and memory usage of a loop and a dict comprehension using **%timeit**. Finally, we compare the memory usage of a list comprehension (**map_comprehension**) and a generator (**map_normal**) using the **%memit** function. The results show that comprehensions and generators can be faster and more memory-efficient than traditional loops in Python.

### generator over comprhension
Generators should be used over comprehensions when memory efficiency is a concern. Comprehensions allocate memory for the entire result set, whereas generators produce values on-the-fly as they are iterated over. Additionally, when the result set is very large, generators can be faster than comprehensions, as they do not need to store all of the results in memory before returning the final result.

Another reason to use generators over comprehensions is if the values of the result set are not required all at once, but rather one at a time, as this allows for better memory management.

However, comprehensions are generally easier to read and write than generators, and are a good choice when memory efficiency is not a concern or when the result set is small.

The memory usage between generators and comprehensions can be evaluated using the memory_profiler extension in an IPython session. For example, consider a scenario where we want to apply a series of operations to a list and take the maximum value.

If we use comprehensions, we will allocate a new list for each comprehension, increasing memory usage:
```python
def map_comprehension(numbers):       
    a = [n * 2 for n in numbers]       
    b = [n ** 2 for n in a]       
    c = [n ** 0.33 for n in b]       
    return max(c)

```
If we use generators instead, we can compute values on the fly, thus saving memory:
```python
def map_normal(numbers):       
    a = map(lambda n: n * 2, numbers)       
    b = map(lambda n: n ** 2, a)       
    c = map(lambda n: n ** 0.33, b)       
    return max(c)

```
We can profile the memory usage of these two solutions using the memory_profiler extension in an IPython session:

```python
%load_ext memory_profiler   
numbers = range(1000000)   
%memit map_comprehension(numbers)   
peak memory: 166.33 MiB, increment: 102.54 MiB   
%memit map_normal(numbers)   
peak memory: 71.04 MiB, increment: 0.00 MiB

```
As seen from the output, the memory used by the comprehension is 102.54 MiB, while the generator uses 0.00 MiB. In scenarios where memory usage is a concern, it's better to use generators instead of comprehensions.

![comprehensions_generators](https://github.com/mdtahmidhossain/Profiling_tools_python/raw/main/images/comprehensions_generators.png)

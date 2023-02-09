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

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
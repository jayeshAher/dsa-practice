# Singly Linked List Implementation

This repository provides a Python implementation of a singly linked list, complete with essential functionalities.

---

## Features

### **Task 1: Basic Linked List Structure**
1. **Node Class**: Represents an individual node in the linked list with:
   - `value`: The value held by the node.
   - `next`: A reference to the next node (default is `None`).
2. **LinkedList Class**:
   - **Constructor**: Initializes an empty list (`head = None`).
   - **Display Method**: Prints the linked list elements in order, e.g., `1 -> 2 -> 3 -> None`.

---

### **Task 2: Essential Linked List Operations**
1. **Append a Node**:
   - Adds a new node to the end of the list.
   - Handles cases where the list is initially empty.
2. **Remove a Node**:
   - Deletes the first occurrence of a node with the specified value.
   - Handles edge cases like an empty list or a missing value.
3. **Search for a Value**:
   - Traverses the list to check if a value exists.
   - Returns a boolean indicating success (`True`) or failure (`False`).

---

### **Task 3: Advanced Operations**
1. **Reverse the Linked List**:
   - Reverses the entire linked list in-place.
   - Adjusts the `next` pointers of all nodes.
2. **Insert a Node at a Specific Position**:
   - Inserts a new node at the given index.
   - Handles edge cases, such as:
     - Negative indices (treated like Python's negative indexing).
     - Insertion at the start or end of the list.
     - Index out of bounds.
3. **Remove All Occurrences of a Value**:
   - Removes all nodes containing a specified value.
   - Efficiently handles multiple consecutive occurrences.

---

### **Advanced Task**
1. **Merge Two Sorted Linked Lists**:
   - Merges two linked lists while preserving sorted order.
   - Returns a new sorted linked list.

---

## Code Structure

### Classes
- **`Node`**: Represents individual elements of the linked list.
- **`LinkedList`**: Contains methods to manipulate and traverse the list.

### Methods
| **Method**                | **Description**                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| `__init__()`              | Initializes the list with an optional `head`.                                                            |
| `display()`               | Displays the linked list in a readable format.                                                           |
| `append(value)`           | Adds a new node with the specified value to the end of the list.                                         |
| `remove(value)`           | Removes the first occurrence of a node with the specified value.                                         |
| `search(value)`           | Checks if a value exists in the list. Returns `True` or `False`.                                         |
| `reverse()`               | Reverses the order of the nodes in the linked list.                                                      |
| `insert(value, pos)`      | Inserts a node at a specific position (supports negative indexing).                                       |
| `remove_all_occurences(value)` | Removes all nodes with the specified value.                                                          |
| `mergeSortedLinked(l1, l2)` | Merges two sorted linked lists into one sorted linked list.                                             |

---

## Example Usage

### Creating and Manipulating a Linked List
```python

# Create a new linked list
ll = LinkedList()

# Append elements
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None

# Insert an element at the start
ll.insert(0, 0)
ll.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

# Remove a specific element
ll.remove(2)
ll.display()  # Output: 0 -> 1 -> 3 -> None

# Reverse the list
ll.reverse()
ll.display()  # Output: 3 -> 1 -> 0 -> None

# Create two sorted linked lists
l1 = LinkedList()
l1.append(1)
l1.append(3)
l1.append(5)

l2 = LinkedList()
l2.append(2)
l2.append(4)
l2.append(6)

# Merge the lists
l3 = mergeSortedLinked(l1, l2)
l3.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
```

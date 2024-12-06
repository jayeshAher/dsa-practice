class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def display(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
        
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        while current:
            if current.value == value:
                prev.next = current.next
                break
            prev = current
            current = current.next
            
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
        
    def reverse(self):
        if not self.head:
            return
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        
    def insert(self, value, pos):
        new_node = Node(value)
        if pos == 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return
        """
        Elegant approach but inefficient
        if pos < 0:
            self.reverse()
            self.insert(value, -pos-1)
            self.reverse()
            return
        """
        if pos < 0:
            size = 0
            current = self.head
            while current:
                size += 1
                current = current.next
            pos = size + pos + 1
            if pos < 0:
                print("Error: Index out of range.")
                return
            
        prev = None
        current = self.head
        for _ in range(pos):
            if not current:
                break
            prev = current
            current = current.next
        new_node.next = current
        if prev:
            prev.next = new_node
        
    def remove_all_occurrences(self, value):
        if not self.head:
            return
        while self.head and self.head.value == value:
            self.head = self.head.next
        prev = None
        current = self.head
        while current:
            if current.value == value:
                prev.next = current.next
            else:
                prev = current
            current = current.next
            
def mergeSortedLinked(l1, l2):
    if not l1.head:
        return l2
    if not l2.head:
        return l1
        
    dummy = Node(0)
    tail = dummy
    p1, p2 = l1.head, l2.head
    
    while p1 and p2:
        if p1.value < p2.value:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next
    
    tail.next = p1 if p1 else p2
    
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list
        
def main():
    l1 = LinkedList()
    l1.append(1)
    l1.append(3)
    l1.append(5)
    l1.append(7)
    l1.append(9)
    l1.display()
    
    l2 = LinkedList()
    l2.append(0)
    l2.append(2)
    l2.append(4)
    l2.append(6)
    l2.display()
    
    l3 = mergeSortedLinked(l1, l2)
    l3.display()

if  __name__ == "__main__":
    main()

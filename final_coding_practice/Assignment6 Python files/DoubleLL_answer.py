class DoubleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
 
        def __init__(self, element, prev, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._prev = prev                     # reference to prev node
            self._next = next                     # reference to next node



    def __init__(self):
        """Create an empty linkedlist."""
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0


    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                             # record deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element                                      # return deleted element

    def first(self):
        """Return (but do not remove) the element at the front of the list.
        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._head._next._element              # front aligned with head of list

    def last(self):
        """Return (but do not remove) the element at the end of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._tail._prev._element


    def delete_first(self):
        """Remove and return the first element of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._delete_node(self._head._next)

    def delete_last(self):
        """Remove and return the last element of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._delete_node(self._head._next)


    def add_first(self, e):
        """Add an element to the front of list."""
        self._insert_between(e, self._head, self._head._next)


    def add_last(self, e):
        """Add an element to the back of list."""
        self._insert_between(e, self._tail._prev, self._tail)


    def __str__(self):
        result = ['head <--> ']
        curNode = self._head._next
        while (curNode._next is not None):
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("tail")
        return "".join(result)


    def sameSame(self, otherlist):
        if len(self) != len(otherlist):
            return False
        else:
            # Loop both linkedlists
            temp1 = self._head._next
            temp2 = otherlist._head._next
            for i in range(len(self)):
                if temp1._element != temp2._element:
                    return False
            return True
        

    def feed(self, otherlist, n):
        if n == 0:
            return
            
        otherlist_temp = otherlist._head
        for i in range(n):              # Find the cut point
            otherlist_temp = otherlist_temp._next
        
        self._head._next._prev = otherlist_temp       # Self.head prev point to cut node
        otherlist_temp._next._prev = otherlist._head       # One after cut node becomes head node
        temp = otherlist._head._next                  # Store this node for swapping
        
        otherlist._head._next = otherlist_temp._next
        otherlist_temp._next._prev = otherlist._head

        otherlist_temp._next = self._head._next       # cut point node next point to self.head
        otherlist_temp._prev = self._head
        self._head._next = temp             # Set up new self.head
        temp._prev = self._head


        self._size += n
        otherlist._size -= n

    def del_anything_occured(self, otherlist):
        temp2 = otherlist._head._next
        for i in range(len(otherlist)):  # Traverse otherlist
            temp = self._head._next           # start from self._head
            while temp is not self._tail:
                if temp._element == temp2._element:     # if found a match, time to delete.
                    if temp is self._head:              # Head case
                        self.delete_first()
                    elif temp is self._tail:            # Tail case
                        self.delete_last()
                    else:                               # Middle case
                        temp._prev._next = temp._next
                        temp._next._prev = temp._prev
                        self._size -= 1
                temp = temp._next
            temp2 = temp2._next





def main():
    print("-------------------Testing sameSame---------------------")
    l1 = DoubleLinkedList()
    l2 = DoubleLinkedList()
    l1.add_first(1)
    l2.add_first(1)
    print(l1.sameSame(l2), "expected: True")

    for i in range(5):
        l1.add_first(i * 2)
    for j in range(5):
        l2.add_first(j * 2)
    print(l1.sameSame(l2), "expected: True")

    l1.add_first("xxx")
    l2.add_first("qqq")
    print(l1.sameSame(l2), "expected: False")


    print("-------------------Testing feed---------------------")
    l1 = DoubleLinkedList()
    l2 = DoubleLinkedList()
    for i in range(5):
        l1.add_first(i * 2)
    for j in range(5):
        l2.add_first(j * 3)
    print(l1) # 8 <--> 6 <--> 4 <--> 2 <--> 0 <--> None
    print(l2) # 12 <--> 9 <--> 6 <--> 3 <--> 0 <--> None
    l1.feed(l2, 5)
    print("Your l1:", l1, "\nExpected: head <--> 12 <--> 9 <--> 6 <--> 8 <--> 6 <--> 4 <--> 2 <--> 0 <--> tail") 
    print("Your l2:", l2, "\nExpected: head <--> 3 <--> 0 <--> tail")


    print("--------------Testing del_anything_occured----------------")
    l1 = DoubleLinkedList()
    l2 = DoubleLinkedList()
    for i in range(10):
        l1.add_first(i * 2)
    for j in range(10):
        l2.add_first(j * 3)
    print(l1)   # 18 <--> 16 <--> 14 <--> 12 <--> 10 <--> 8 <--> 6 <--> 4 <--> 2 <--> 0 <--> None
    print(l2)   # 27 <--> 24 <--> 21 <--> 18 <--> 15 <--> 12 <--> 9 <--> 6 <--> 3 <--> 0 <--> None
    l1.del_anything_occured(l2)
    print("Your l1:", l1, "\nExpected: head <--> 16 <--> 14 <--> 10 <--> 8 <--> 4 <--> 2 <--> tail")
    print("Your l2:", l2, "\nl2 should remain the same.")

 
if __name__ == '__main__':
    main()








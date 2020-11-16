class Empty(BaseException):
    def __init__(self, message):
        self.message = message

class LinkedDeque:
    """Deque implementation using a doubly linked list for storage."""

    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_next', '_prev'         # streamline memory usage

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

            

    #------------------------------- queue methods -------------------------------
    def __init__(self):
        """Create an empty deeue."""
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0                      # number of elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
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
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._head._next._element              # front located at head._next

    def last(self):
        """Return (but do not remove) the element at the end of the queue.

        Raise Empty exception if the deque is empty.
        """
        # Your code
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._tail._prev._element              # front located at tail._prev

    def delete_first(self):
        """Remove and return the first element of the deque.

        Raise Empty exception if the queue is empty.
        """
        # Your code
        if self.is_empty():
            raise Empty
        else:
            ans = self._head._next._element
            new_next = self._head._next._next
            self._head._next = new_next
            new_next._prev = self._head
            self._size -= 1
            return ans

    def delete_last(self):
        """Remove and return the last element of the deque.

        Raise Empty exception if the queue is empty.
        """
        # Your code
        if self.is_empty():
            raise Empty
        else:
            ans = self._tail._prev._element
            new_prev = self._tail._prev._prev
            self._tail._prev = new_prev
            new_prev._next = self._tail
            self._size -= 1
            return ans


    def add_first(self, e):
        """Add element e to the front of deque."""
        # Your code
        newest = self._Node(e,self._head,self._head._next)
        self._head._next._prev = newest
        self._head._next = newest
        self._size += 1
        
        

    def add_last(self, e):
        """Add an element to the back of deque."""
        # Your code
        newest = self._Node(e,self._tail._prev, self._tail)
        self._tail._prev._next = newest
        self._tail._prev = newest
        self._size += 1



    def __str__(self):
        result = ["head <--> "]
        curNode = self._head._next
        while (curNode._next is not None):
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("tail")
        return "".join(result)



def main():
    deque = LinkedDeque()
    for i in range(3):
        deque.add_first(i)
    for j in range(3):
        deque.add_last(j + 4)

    print(deque) # head <--> 2 <--> 1 <--> 0 <--> 4 <--> 5 <--> 6 <--> tail
    print("deleting first: ", deque.delete_first())   # 2
    print("deleting last: ", deque.delete_last())     # 6
    print(deque) # head <--> 1 <--> 0 <--> 4 <--> 5 <--> tail

if __name__ == '__main__':
    main()

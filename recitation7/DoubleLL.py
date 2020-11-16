class Empty(BaseException):
    def __init__(self, message):
        self.message = message

class DoubleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_next', '_prev'         # streamline memory usage

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

    def split_after(self, index):
        """
        :index: Int -- split after this indexed node.
        (index start from zero)

        split self DoubleLinkedList into two separate lists.

        ***head/tail sentinel nodes does not count for indexing.

        :return: A new DoubleLinkedList object that contains the second section.
        """
        ptr = 0
        currNode = self._head._next

        while currNode is not None and ptr<index:
            currNode = currNode._next
            ptr += 1

        #currNode is the breakpoint now
        new_list = DoubleLinkedList()
        #do a loop and add nodes to new list
        to_add = currNode._next
        while to_add._element is not None:
            new_list.add_last(to_add._element)
            to_add = to_add._next
        #cut off connection
        currNode._next = self._tail
        self._tail._prev = currNode
        return new_list







    def merge(self, otherlist):
        """
        :otherlist: DoubleLinkedList -- another DoubleLinkedList to merge.

        For example:
        L1: head<-->1<-->2<-->3-->tail
        L2: head<-->4-->tail
        L1.merge(L2)
        L1: head<-->1-->2-->3<-->4-->tail
        L2: head<-->tail
        :return: Nothing.
        """
        ptr = otherlist._head._next
        while ptr._element is not None:
            next = ptr._next
            self.add_last(otherlist._delete_node(ptr))
            ptr = next





    def switch_first0(self,other):

        head1 = self._head._next
        head2 = other._head._next

        self._head._next = head2
        head1._next._prev = head2

        other._head._next = head1
        head2._next._prev = head1
        #now, we still need to change the two node's reference
        head2._next,head1._next = head1._next, head2._next
        head2._prev,head1._prev = head1._prev,head2._prev

    def switch_first1(self,other):
        head1 = self._head._next
        head2 = other._head._next

        self._head._next = head1._next
        head1._next._prev = self._head
        head1._prev = None
        head1._next = None

        other._head._next = head2._next
        head2._next._prev = other._head
        head2._next = None
        head2._prev = None

        self._head._next._prev = head2
        head2._next = self._head._next
        head2._prev = self._head
        self._head._next = head2

        other._head._next._prev = head1
        head1._next = other._head._next
        head1._prev = other._head
        other._head._next = head1

def main():
    import random
    test_list = DoubleLinkedList()
    for i in range(8):
        test_list.add_first(random.randint(0, 20))
    test_list0 = DoubleLinkedList()
    for i in range(8):
        test_list0.add_first(random.randint(0,20))
    print("Test list length 8, looks like:")
    print(test_list)
    # print("test_list0 looks like: ")
    # print(test_list0)
    print("--------------------------------------------------------")
    # print("after switch_first")
    # test_list.switch_first1(test_list0)
    # print(test_list)
    # print(test_list0)

    print("Split after index 5:")
    new_list = test_list.split_after(5)
    print("Original List:", test_list)
    print("The second part:", new_list)
    print("--------------------------------------------------------")
    print("Merging original list with the second part:")
    #print(test_list._tail._prev._element)
    #print(new_list._size)
    test_list.merge(new_list)
    print("Original List:", test_list)
    print("The second part:", new_list)
    #print(new_list._size)
    print("--------------------------------------------------------")

if __name__ == '__main__':
    main()

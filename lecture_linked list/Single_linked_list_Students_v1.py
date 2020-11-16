class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass

#-------------------------- nested _Node class --------------------------
class Node:
    
  def __init__(self, element, next = None):   # initialize node's fields
    self._element = element               # reference to user's element
    self._next = next                     # reference to next node


class Single_Linked_List:
  #------------------------------- Single Linked List methods -------------------------------
  def __init__(self):
    """Create an empty LinkedList."""
    self._head = None                       # reference to the head node
    self._size = 0                          # number of elements in the list

  def __len__(self):
    """Return the number of elements in the LinkedList."""
    return self._size

  def is_empty(self):
    """Return True if the LinkedList is empty."""
    return self._size == 0

  def insertAtFirst(self, e):
    """Add element e to the start of the LinkedList."""
    # to do
    newNode = Node(e)
    newNode._next = self._head
    self._head = newNode
    self._size += 1


    
  def deleteFirst(self):
    """Remove and return the first element from the LinkedList.

    Raise Empty exception if the Linked list is empty.
    """
    if self.is_empty():
      raise Empty('LinkedList is empty')
    # to do
    else:
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

  def unOrderedSearch(self,target):
    # Search for the target element in the Linked List
    # to do
    currNode = self._head
    while currNode != None and currNode._element != target:
        currNode = currNode._next
    return (currNode!=None)

  def printAll(self):
      # print the contents of the Linked List
      # to do
      result =""
      currNode = self._head
      while currNode is not None:
          result += str(currNode._element)+" "
          currNode = currNode._next
    
      return result[:-1]
  
linkedlist1 = Single_Linked_List()
linkedlist1.insertAtFirst(5)
linkedlist1.insertAtFirst(10)
linkedlist1.insertAtFirst(22)
linkedlist1.insertAtFirst(35)

print("LinkedList contents: "+linkedlist1.printAll())

print(linkedlist1.deleteFirst())
print(linkedlist1.deleteFirst())
print("LinkedList contents: "+linkedlist1.printAll())

print(linkedlist1.unOrderedSearch(20))
print("LinkedList contents: "+linkedlist1.printAll())

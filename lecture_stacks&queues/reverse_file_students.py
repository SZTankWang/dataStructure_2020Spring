class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass


class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data.pop()               # remove last item from list

  def __repr__(self):
      return str(self._data)

def reverse_file(filename):
    
  """Overwrite given file with its contents line-by-line reversed."""

  inputfile = open(filename,'r')
  f = inputfile.readlines()
  print(f)
  record = ArrayStack()
  for i in f:
     record.push(i)
  inputfile.close()
  print(len(record))
  
      
      
      

  # to do


  # now we overwrite with contents in LIFO order
  output = open(filename, 'w')    # reopening file overwrites original
  while len(record) > 0:
      output.write((record.pop()))
  output.close()

  # to do


reverse_file('file.txt')

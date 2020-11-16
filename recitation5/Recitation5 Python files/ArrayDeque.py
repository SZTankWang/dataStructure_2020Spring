from queue import Empty
class ArrayDeque:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == len(self._data)

    def first(self):
        return self._data[self._front]

    def last(self):
        tail = (self._front + self._size -1)%len(self._data)
        return self._data[tail]

    def delete_first(self):
        if self._size == 0:
            raise Empty('Queue is empty')
        memo = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return memo
    def add_first(self, e):
        if self._size == len(self._data):
            raise Empty('Queue is full')
        self._front = (self._front-1) % len(self._data) #make the previous position the first
        self._data[self._front] = e
        self._size += 1

    def delete_last(self):
        if self._size == 0:
            raise Empty('Queue is empty')
        tail = (self._front + self._size-1) %len(self._data)
        to_delete = self._data[tail]
        self._data[tail] = None
        self._size -= 1
        return to_delete
    def add_last(self, e):
        if self._size == len(self._data):
            raise Empty('Queue is full')
        avail = (self._front+self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1
    def __str__(self):
        return str(self._data)

def main():
    # Empty Queue, size 10.
    deque = ArrayDeque()

    # Add 0, 1, 2, 3 following FIFO.
    for i in range(4):
        deque.add_first(i)
    print(deque)  # [None, None, None, None, None, None, 3, 2, 1, 0]

    # Add 4, 5, 6, 7 following LIFO.
    for j in range(4):
        deque.add_last(j + 4)
    print(deque)  # [4, 5, 6, 7, None, None, 3, 2, 1, 0]

    # Remove first one
    print(deque.delete_first()) # 3
    #print(deque)  # [4, 5, 6, 7, None, None, 3, 2, 1, 0]


    # Remove last one
    print(deque.delete_last()) # 7


if __name__ == '__main__':
    main()

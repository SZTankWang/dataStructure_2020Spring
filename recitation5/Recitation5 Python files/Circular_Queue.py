from queue import Empty
class ArrayQueue():

    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        ''' Return the value stored at the front of the queue '''
        return self._data[self._front]

    def dequeue(self):
        ''' Remove and return the value stored at the front of the queue '''
        if self._size == 0:
            raise Empty('Queue is empty')
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
    def enqueue(self, e):
        ''' Insert e at the end of the queue '''
        if self._size == self._data:
            raise Empty('Queue is full')
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    def __str__(self):
        ''' You can simply print self._data '''
        return str(self._data)

def main():
    # Empty Queue, size 10.
    queue = ArrayQueue()

    # Enqueue 0, 1, 2, 3, 4, 5, 6, 7
    for i in range(8):
        queue.enqueue(i)
    print(queue)   # [0, 1, 2, 3, 4, 5, 6, 7, None, None] 

    # Dequeue 5 times.
    for j in range(5):
        queue.dequeue()
    print(queue)  # [None, None, None, None, None, 5, 6, 7, None, None]

    # Enqueue 8, 9, 10, 11, 12
    for k in range(5):
        queue.enqueue(k + 8)
    print(queue)  # [10, 11, 12, None, None, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    main()


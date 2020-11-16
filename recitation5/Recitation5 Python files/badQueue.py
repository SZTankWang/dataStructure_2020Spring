from queue import Empty
class ArrayQueue():

    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        return self._data[0]

    def dequeue(self):
        return self._data.pop(0)

    def enqueue(self, e):
        self._data.append(e)

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
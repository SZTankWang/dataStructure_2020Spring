from queue import Empty # Use this for exception

class LeakyQueue():

    def __init__(self, max_size):
        self._data = [None] * max_size   # Static (fixed) size
        self._size = 0    # Track current number of elements
        self._front = 0  # Use this variable to make the queue circular

    def enqueue(self, e):  # O(1)
        """ enqueue element e into end of the queue, with leaky features. """
        if self._size == len(self._data):
            self.dequeue()
            self.enqueue(e)
        else:
            avail = (self._front + self._size)% len(self._data)
            self._data[avail] = e
            self._size += 1
            
    def dequeue(self):      # O(1)
        """ dequeue and return the value stored at front of the queue. """
        if self._size == 0:
            raise Empty
        else:
            ans = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front+1) % len(self._data)
            self._size -= 1
            return ans

    def __len__(self):  # O(1)
        """ return the current number of elements in the queue. """
        return self._size

    def is_empty(self): # O(1)
        """ return True if the queue is empty. """
        return self._size == 0

    def __str__(self):  # O(n) or O(1) up to you, not graded
        return str(self._data)

##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.'''
def main():
    leakyqueue = LeakyQueue(5)  # Max size = 5 queue.
    leakyqueue.enqueue('a')
    leakyqueue.enqueue('b')
    leakyqueue.enqueue('c')
    print(leakyqueue)   # front of queue --> a b c
    leakyqueue.enqueue('d')
    leakyqueue.enqueue('e')
    print(leakyqueue)  # front of queue --> a b c d e
    leakyqueue.enqueue('f')
    leakyqueue.enqueue('g')
    leakyqueue.enqueue('h')
    print(leakyqueue)   # front of queue --> d e f g h   (a b c are gone because there are old)
    print(leakyqueue.dequeue())  # d dequeued
    print(leakyqueue.dequeue())  # e dequeued
    print(leakyqueue.dequeue())  # f dequeued
    print(leakyqueue)   # front of queue --> g h

if __name__ == '__main__':
    main()
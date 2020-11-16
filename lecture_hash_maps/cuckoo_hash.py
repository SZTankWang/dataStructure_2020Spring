import random

def KeyError(Exception):
    def __init__(self, msg):
        self.msg = msg

class Item():
    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __eq__(self, other):               
        return self._key == other._key   # compare items based on their keys

    def __ne__(self, other):
        return not (self == other)       # opposite of __eq__

    def __lt__(self, other):               
        return self._key < other._key    # compare items based on their keys

class CuckooHashTable():
    def __init__(self):
        self._size = 0
        self._maxsize = 11
        self._array1 = [None] * self._maxsize
        self._array2 = [None] * self._maxsize
        self._random1 = random.random()
        self._random2 = random.random()


    def _hash1(self, key):
        return hash((key, self._random1)) % self._maxsize

    def _hash2(self, key):
        return hash((key, self._random2)) % self._maxsize

    def key_in_array(self,array,k):
        if array == 1:
            item = self._array1[self._hash1(k)]
            if item is None:
                return False
            elif item._key == k:
                return True
            else:
                return False
        if array == 2:
            item = self._array2[self._hash2(k)]
            if item is None:
                return False
            elif item._key == k:
                return True
            else:
                return False

    def __getitem__(self,key):
        ''' given key, return the value associated with key
            use hash1/hash2 to compute the index.
            raise KeyError if not found.
        '''
        # hash1
        if self.key_in_array(1,key):
            return self._array1[self._hash1(key)]._value
        # hash2
        elif self.key_in_array(2,key):
            return self._array2[self._hash2(key)]._value
        else:
            raise KeyError

    def __setitem__(self,k,v, counter = None, next_state = True):
        ''' if key k exists in either array, modify associated value to v.
            if key k does not exist in both arrays, insert (k, v) into table as a new class Item.
            if cycles, resize (rehash) the table.
            terminate the function until we finally find a location for k.
            You may want to define a resize function for cycle 
        '''
        #1
        if self.key_in_array(1,k):
            self._array1[self._hash1(k)]._value = v
        #2
        elif self.key_in_array(2,k):
            self._array2[self._hash2(k)]._value = v
        #3
        elif self._array1[self._hash1(k)] is None:
            self._array1[self._hash1(k)] = Item(k,v)
            self._size += 1
        #4
        elif self._array2[self._hash2(k)] is None:
            self._array2[self._hash2(k)] = Item(k,v)
            self._size += 1

        #5  Switch
        else:
            # Insert to array1
            if next_state == True:
                kickedItem = self._array1[self._hash1(k)]
                self._array1[self._hash1(k)] = Item(k, v)
            # Insert to array2
            elif next_state == False:
                kickedItem = self._array2[self._hash2(k)]
                self._array2[self._hash2(k)] = Item(k, v)

            if counter == None:
                self.__setitem__(kickedItem._key, kickedItem._value, counter = 1, next_state = not next_state)
            else:
                #6 Cycle
                counter += 1
                if counter > len(self) * 2:
                    self._resize()
                    self[kickedItem._key] = kickedItem._value
                    # self.__setitem__(kickedItem._key, kickedItem._value, counter, next_state=not next_state)
                else:
                    self.__setitem__(kickedItem._key, kickedItem._value, counter, next_state = not next_state)


    def __delitem__(self,k):
        ''' given key, set self._array1 or self._array2 corresponding index to None.
            raise KeyError if key not found.
        '''
        if self.key_in_array(1,k):
            self._array1[self._hash1(k)] = None
        # hash2
        elif self.key_in_array(2,k):
            self._array2[self._hash2(k)] = None
        else:
            raise KeyError
        self._size -= 1

    def _resize(self):
        ''' double the size of self._array1, self._array2.
            also self._maxsize
            Remember to rehash all the old (key, value) pairs!
        '''
        items = []
        for item in self.items():
            items.append(item)
        self._size = 0
        self._maxsize *= 2
        self._array1 = [None] * self._maxsize
        self._array2 = [None] * self._maxsize
        self._random1 = random.random()
        self._random2 = random.random()
        for item in items:
            self[item._key] = item._value

    def __len__(self): 
        return self._size

    def __contains__(self,key): 
        ''' return True if key exists in table
            return False otherwise
        '''
        return self.key_in_array(1,key) or self.key_in_array(2,key)

    def __iter__(self):
        ''' same as keys(self) '''
        self.keys()

    def keys(self): 
        ''' yield an generator of keys in table '''
        items = []
        for item in self._array1:
            if item is not None:
                items.append(item)
        for item in self._array2:
            if item is not None:
                items.append(item)
        for item in items:
            yield item._key

    def values(self): 
        ''' yield an generator of values in table '''
        items = []
        for item in self._array1:
            if item is not None:
                items.append(item)
        for item in self._array2:
            if item is not None:
                items.append(item)
        for item in items:
            yield item._value

    def items(self):
        ''' yield an generator of Items in table '''
        items = []
        for item in self._array1:
            if item is not None:
                items.append(item)
        for item in self._array2:
            if item is not None:
                items.append(item)
        for item in items:
            yield  item


# def main():
#     table = CuckooHashTable()
#     for i in range(200):        # Tests __setitem__, insert 0 ~ 199. _resize() also need to work correctly.
#         table[i] = "happy_coding"
    
#     print(len(table))           # Tests __len__, should be 200.

#     for j in range(195):        # Tests __delitem__, delete 0 ~ 194
#         del table[j]

#     print(len(table))           # Tests __len__, should be 5.

#     for j in table.items():     # Tests items()
#         print(j._key)           # 195, 196, 197, 198, 199 left in table

#     print(table[196])           # Tests __getitem__
#                                 # Should print "happy_coding"
#     for i in range(400):
#         table[i] = "w"

#     for i in range(400):
#         table[i] = "w"
#     for j in table.items():     # Tests items()
#         print(j._key)           # 195, 196, 197, 198, 199 left in table

# main()


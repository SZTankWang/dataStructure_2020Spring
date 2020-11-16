import random

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
        self._size=0
        self._maxsize = 11
        self._array1 = [None] * self._maxsize
        self._array2 = [None] * self._maxsize
        self._random1 = random.random()
        self._random2 = random.random()


    def _hash1(self, key):
        return hash((key, self._random1)) % self._maxsize

        return hash((key, self._random2)) % self._maxsize
    def _hash2(self, key):


    def __getitem__(self,key):
        ''' given key, return the value associated with key
            use hash1/hash2 to compute the index.
            raise KeyError if not found.
        '''
        index1 = self._hash1(key)
        index2 = self._hash2(key)
        if self._array1[index1] is not None and self._array1[index1]._key == key:
            return self._array1[index1]._value
        if self._array2[index2] is not None and self._array2[index2]._key == key:
            return self._array2[index2]._value

    def __setitem__(self,k,v): 
        ''' if key k exists in either array, modify associated value to v.
            if key k does not exist in both arrays, insert (k, v) into table as a new class Item.
            remember to modify size.
            if cycles, resize (rehash) the table.
            terminate the function until we finally find a location for k.
            You may want to use the _resize function for cycle 
        '''
        index1 = self._hash1(k)
        index2 = self._hash2(k)
        settle = False #control loop
        loop_count = 0 #determine when to resize
        check_at = 1  #check_at is the number of the array to look at
        if self._array1[index1] is not None and self._array1[index1]._key == k:
            self._array1[index1]._value = v
        elif self._array2[index2] is not None and self._array2[index2]._key == k:
            self._array2[index2]._value = v
            
            
        #else insert, kick and loop
        else:
            #to settle is the item pending
            to_settle = Item(k,v)
            while settle == False:
                if check_at == 1:
                    index = self._hash1(to_settle._key)
                    if self._array1[index] is not None:
                        to_kick = self._array1[index]
                        self._array1[index] = to_settle
                        to_settle = to_kick
                        loop_count += 1
                        check_at = 2
                        if loop_count > 2*self._size:
                            self._resize()
                            loop_count = 0
                    elif self._array1[index] is None:
                        #free, insert directly
                        self._array1[index] = to_settle
                        settle = True
                        self._size += 1
                if check_at == 2:
                    index = self._hash2(to_settle._key)
                    if self._array2[index] is not None:
                        to_kick = self._array2[index]
                        self._array2[index] = to_settle
                        to_settle = to_kick
                        loop_count += 1
                        check_at = 1
                        if loop_count == 2*self._size:
                            self._resize()
                            loop_count = 0
                    elif self._array2[index] is None:
                        #free, insert directly
                        self._array2[index] = to_settle
                        settle = True
                        self._size += 1
                    
                
    def __delitem__(self,k): 
        ''' given key, set self._array1 or self._array2 corresponding index to None.
            remember to modify size.
            raise KeyError if key not found.
        '''
        index1 = self._hash1(k)
        index2 = self._hash2(k)
        if self._array1[index1] is not None and self._array1[index1]._key == k:
            self._array1[index1] = None
            self._size -= 1
            #return
        elif self._array2[index2] is not None and self._array2[index2]._key == k:
            self._array2[index2] = None
            self._size -= 1
            #return
        else: KeyError('Key not found')
            
        
    def _resize(self):
        ''' double the size of self._array1, self._array2.
            also self._maxsize
            Remember to rehash all the old (key, value) pairs!
        '''
        memo1 = self._array1[:]
        memo2 = self._array2[:]
        new_size = 2*self._maxsize - 1
        self._array1 = [None]*new_size
        self._array2 = [None]*new_size
        self._maxsize = new_size
        self._random1 = random.random()
        self._random2 = random.random()
        self._size = 0
        for i in memo1:
            if i is not None:
                key = i._key
                value = i._value
                self[key] = value
        for j in memo2:
            if j is not None:
                key = j._key
                value = j._value
                self[key] = value

    def __len__(self): 
        return self._size

    def __contains__(self,key): 
        ''' return True if key exists in table
            return False otherwise
        '''
        index1 = self._hash1(key)
        index2 = self._hash2(key)
        if self._array1[index1] is not None and self._array1[index1]._key == key:
            return True
        if self._array2[index2] is not None and self._array2[index2]._key == key:
            return True
    def __iter__(self):
        ''' same as keys(self) '''
        for i in self._array1:
            if i is not None:
                yield i._key
        for j in self._array2:
            if j is not None:
                yield j._key 

    def keys(self): 
        ''' yield an generator of keys in table '''
        for i in self._array1:
            if i is not None:
                yield i._key
        for j in self._array2:
            if j is not None:
                yield j._key

    def values(self): 
        ''' yield an generator of values in table '''
        for i in self._array1:
            if i is not None:
                yield i._value
        for j in self._array2:
            if j is not None:
                yield j._value

    def items(self):
        ''' yield an generator of Items in table '''
        for i in self._array1:
            if i is not None:
                yield i
        for j in self._array2:
            if j is not None:
                yield j 


def main():
    table = CuckooHashTable()
    for i in range(200):        # Tests __setitem__, insert 0 ~ 199. _resize() also need to work correctly.
        table[i] = "happy_coding"
    
    print(len(table))           # Tests __len__, should be 200.
    for j in range(195):        # Tests __delitem__, delete 0 ~ 194
        del table[j]

    print(len(table))           # Tests __len__, should be 5.

    for j in table.items():     # Tests items()
        print(j._key)           # 195, 196, 197, 198, 199 left in table

    print(table[196])           # Tests __getitem__
                                # Should print "happy_coding"
    
if __name__ == '__main__':
    main()

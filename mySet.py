class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 5
        self.slots = [None] * self.size
        
    def add(self, key):
        hashIdx = self.hashFunction(key, self.size)
        if self.slots[hashIdx] == None or self.slots[hashIdx]==key:
            self.slots[hashIdx] = key
        else:
            rehashIdx = self.rehashFunction(hashIdx, self.size)
            while self.slots[rehashIdx]!=None and self.slots[rehashIdx]!=key:
                rehashIdx = self.rehashFunction(rehashIdx, self.size)
            self.slots[rehashIdx] = key
        
    def remove(self, key):
        hashIdx = self.hashFunction(key, self.size)
        position = hashIdx
        stop = False
        while self.slots[position]!=None and not stop:
            if self.slots[position]==key:
                self.slots[position] = None
            else:
                position = self.rehashFunction(position, self.size)
                if position == hashIdx:
                    stop = True

        
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        """
        hashIdx = self.hashFunction(key, self.size)
        position = hashIdx
        stop = False
        while self.slots[position]!=None and not stop:
            if self.slots[position] == key:
                return True
            else:
                position = self.rehashFunction(position, self.size)
                if position == hashIdx:
                    stop = True

        return False
        
    def hashFunction(self,key,size):
        return key%size
    
    def rehashFunction(self,oldHash, size):
        return (oldHash+1)%size


# Your MyHashSet object will be instantiated and called as such:
#obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# hashSet = MyHashSet()
# hashSet.add(1)        
# hashSet.add(2)        
# print(hashSet.contains(1))  # returns true
# print(hashSet.contains(3))   # returns false (not found)
# hashSet.add(2)
# hashSet.add(6)  
# hashSet.add(11)
# hashSet.add(16)
# print(hashSet.contains(2)) #returns true
# print(hashSet.contains(6)) #returns true
# print(hashSet.slots)
# # hashSet.remove(6) 
# # print(hashSet.contains(6))  
# print(hashSet.slots)
# print(hashSet.contains(1)) #returns true
# hashSet.remove(2)       
# print(hashSet.contains(2) )   # returns false (already removed)\

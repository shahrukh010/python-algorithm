class Hashtable:

  def __init__(self):
    self.size = 10
    self.key = [None] * self.size
    self.value = [None] * self.size

  def put(self, key, value):
    hash_key = self.hashFunction(key)
    while self.key[hash_key] is not None:

      if self.key[hash_key] == key:
        self.value[hash_key] = value  #update
        return
      hash_key = (hash_key + 1) % self.size
    self.key[hash_key] = key
    self.value[hash_key] = value

  def hashFunction(self, key):
    sum = 0
    for index in range(len(key)):
      sum = sum + ord(key[index])
    return sum % self.size

  def get(self, key):
    index = self.hashFunction(self, key)
    while self.key[index] is not None:
      if self.key[index] == key:
        return self.value[index]
      index = (index + 1) % self.size


ht = Hashtable()
ht.put('apple', 10)
ht.put('barry', 5)
ht.put('pi', 8)
ht.put("chery", 10)
ht.put("date", 5)
ht.put("elderberry", 15)
ht.put('apple', 25)

print(ht.key)
print(ht.value)
print(ht.get('apple'))

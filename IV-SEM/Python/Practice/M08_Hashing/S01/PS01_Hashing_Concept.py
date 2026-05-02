'''
HASHING:
Defiinition: Hashing is a technique that converts a key into an index using a hash function to store and retrieve data quickly in a hash table.
Advantages: 
Fast operations (search, insert, delete ≈ O(1))
Efficient searching
Saves time compared to linear structures
Simple and widely used (databases, caching, passwords)
collision resolution techniques:
1. seperate chaining
2. open addressing
'''
a = 10 
b = 'Nitya'
c = 56.78
print(hash(a))
print(hash(b))
print(hash(c))


size = 7
table = [None]* size
a = [10,20,30]
for key in a:
    index = key % size
    table[index] = key 
print(table)
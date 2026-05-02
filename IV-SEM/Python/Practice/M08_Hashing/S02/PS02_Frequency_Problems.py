'''
1. Count Frequnecy of Elements(Using dict and counter)
2. Count Distinct Elements
3. Find Element with Maximum frequency
4. First non-repeating element
5.Count occurnece of each charecter
6.check if two arrays have same frequency
7.Elements appearng more than n/2 times (majority Element)
'''

#1.
a = [1,2,3,4,1,2,3,4,6]
d = {}
for num in a:
    d[num] = d.get(0,num) + 1
print(d)
from collections import Counter 
a = [1,2,3,4,1,2,3,4,6]
print(Counter(a))

#2.
a = [1,2,1,2,1,4,2,5]
print(len(set(a)))

#3. 
a = [1,2,1,2,1,4,2,5]
freq = {}
for x in a:
    freq[x] = freq.get(x,0)+1
for x in  a:
    max_ele = max(freq, key = freq.get)
print(max_ele)

#First non-repeating element
a = [1,2,1,2,1,4,2,5]
freq = {}
for x in a:
    freq[x] = freq.get(x,0)+1 
for x in a:
    if freq[x] == 1:
        print(x)
        break
#5. Count occurnece of each charecter
a = 'Nitya'
freq = {}
for ch in a:
    freq[ch] = freq.get(ch,0)+1
print(freq)

#6.check if two arrays have same frequency
from collections import Counter
a = [1,2,1,2,1,4,2,5]
b = [10,20,1,4,5,78,9]
print(Counter(a) == Counter(b))

#7.Elements appearng more than n/2 times (majority Element)

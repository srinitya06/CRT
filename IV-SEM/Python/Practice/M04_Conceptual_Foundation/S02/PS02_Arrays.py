'''
Arrays:

#List
#min(), max(), len(), sum(), reversed(), list()
# + ==> concatenation, * ==> Repitition

def Reverse_list(li): 
    res = []
    for ele in li:
        res.insert(0,ele)
    return res
    Solution-1
    res = []
    stop = -1 * (len(li) + 1)
    for i in range(-1,stop,-1):
        res.append(li[i])
    return res

    Solution-2

    
    stop = -1 * (len(li) + 1)
    res = [li[i] for i in range(-1, stop, -1)]
    return res
print(Reverse_list([1,2,3,4])) #[4,3,2,1]

2. check if a array is stored or not
def is_stored(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
           return False
    return True 
print(is_stored([12,23,45,56,78])) #True
print(is_stored([45,20,36,78,1])) #False

'''
#Count Frequency of Elements
'''
input : [1,2,3,2,4,3,1,5]
output : {1:2, 2:2, 3:2, 4:1, 5:1}
'''
li = [1,2,3,2,4,3,2,1,5]
d = {}
for i in li:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d) 
li = [1,2,3,2,4,3,1,5]
d = {}
for i in li:
    d[i] = d.get(i,0)+1
print(d)
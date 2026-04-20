#Digital root
def Digital_root(n):
    if n <= 9:
        return n 
    s = sum([int(i) for i in str(n)])
    return (Digital_root(s))
print(Digital_root(456)) #6

def is_sorted_array(nums):
    pass
print(is_sorted_array([10,20,30,4,50])) #True
print(is_sorted_array([10,2,30,15,50])) #False



#Frequency count 
def frequency_count(st):
    d = {}
    for ch in st:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d

print(frequency_count("abcabc"))  # {'a': 2, 'b': 2, 'c': 2}


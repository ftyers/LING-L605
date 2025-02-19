string = 'abcd'

def permutation(text):
    if len(text) == 0:
        return []
    if len(text) == 1:
        return [text]
        
    l = []
    for i in range(len(text)):
        m = text[i]
        remlist = text[:i] + text[i+1:]
        for p in permutation(remlist):
            l.append(m + p)
    return l

x = permutation(string)
print(x)
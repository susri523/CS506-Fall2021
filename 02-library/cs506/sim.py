def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    '''
        L1 norm is p = 1, so take absolute value of the difference
    '''
    res = 0 
    for i in range(len(x)):
        res += abs(x[i] - y[i]) 
    return res

def jaccard_dist(x, y):
    if len(x) == 0 or len(y)==0:
        return 0
    count_intersect = 0 

    for i in range(len(x)):
        match = x[i] == y[i] 
        count_intersect += match
    jsim = count_intersect / len(x)
    return 1 - jsim 

def cosine_sim(x, y):
    if len(x) == 0 or len(y)==0:
        return 0
    if len(x) != len(y):
        return -1
    res = 0
    for i in range(len(x)):
        res += x[i] * y[i]
    return res

# Feel free to add more

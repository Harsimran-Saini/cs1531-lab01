'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    list = [1, 1]
    if (n > 2):
        for a in range(1, n-1):
            list.append(list[a-1] + list[a])
    elif (n == 0):
        list = []
    elif (n == 1): 
        list = [1]
    else:
        list = [1, 1]
        
    return list
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    # TODO = fill in the code here, and return the correct result using the return keyword

if __name__ == '__main__':
    import doctest
    doctest.testmod()

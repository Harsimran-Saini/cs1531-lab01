'''
make a command line calculator

DIFFICULTY = MEDIUM
TOPICS = strings, variables, lists

your task is to write a command line calculator
this task is easy since we can use the eval function to do most of the legwork
however, we need to parse possible invalid user input. This is your task

return None if invalid input. Otherwise return the result
'''

def calculate(s):

    ans = None;
    k = []
    i = 0
    for character in s:
        if (character >= '0' and character <= '9'):
            k.append(character)
            i = i + 1
        elif (character == '+' or character == '-' or character == '*' or character == '/'):
            k.append(character)
            i = i + 1
        elif (character == '(' or character == ')'):
            k.append(character)
            i = i + 1
        else:
            pass

    final = ''
    for word in k:
        final += word + ' '

    if (i > 0):
        ans = eval(final);
    
    return ans;
        
    '''
    >>> calculate("1+3")
    4
    >>> calculate("1+3*4/3")
    5.0
    >>> calculate("(1+3)*5")
    20
    >>> calculate("-----1")
    -1
    >>> calculate("-+-1")
    1
    >>> calculate(\'print("bad guy coming to hack")\')
    '''
    # TODO = fill in this function
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

#Part 2 Convert script (1) so that it uses functional programming (e.g., list comprehension, map, reduce, and/or lambda), and has no if/while/for statements or recursion.
from itertools import combinations as c

def largestReversi():
    #largestR = [x*y for x,y in list(c(list(range(10,100)),2)) if str(x*y)==''.join(reversed(str(x*y)))][-1]

    x =max(filter(lambda y: str(y[2]) == ''.join(reversed(str(y[2]))),
                    map(lambda x:(x[0] , x[1], x[0]*x[1]),
                        list(c(list(range(100,1000)),2))))
           ,key=lambda item:item[2])

    return (x[0],'x',x[1],'=',x[2])

print(' '.join([str(i) for i in largestReversi()]))





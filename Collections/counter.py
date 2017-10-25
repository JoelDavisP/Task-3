import collections as c

def counter_ex():
    """This is a sample program demonstrating counter module in python. """
    cnt = c.Counter('abcabcabcabc')
    print 'initially: ', cnt
    cnt.update("abc")
    print "After updating with 'abc': ", cnt
    ls = set(cnt.elements())
    print "elements of the list are: ", ls  
    cnt1 = c.Counter("abcabc")
    print 'New counter is: ', cnt1
    print 'Adding first counter with second is: ', cnt + cnt1
    print 'Subtracting first counter from second is: ', cnt - cnt1
    print '\n\n\n\n'
    cnt2 = c.Counter("abdgfvgabfgbdf")
    print 'New counter 1', cnt2
    cnt3 = c.Counter("abhvvvannhvhbhbmncvgdbjd")
    print '\nNew counter 2', cnt3
    print '\nIntersection (taking positive minimums) first counter with second is: ', cnt2 & cnt3   
    print '\nUnion (Taking maximums in the two counters is: ', cnt2 | cnt3
counter_ex()    

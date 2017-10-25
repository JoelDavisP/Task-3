import collections as c

def dqueue():
    """This program demonstrates the working of a double ended queue(called dqueue) in python."""
    d1 = c.deque('abcdefg')
    print "Initially double ended queue is: ", d1
    d1.append('h')
    print "After appending on right, queue will be: ", d1
    d1.appendleft('Z')
    print "After appending on the left, queue will be:", d1
    d1.pop()
    print "After poping from the rightt, queue will be:", d1
    d1.popleft()
    print "After poping from the left, queue will be:", d1
    d1.rotate(2)
    print "After rotating two times from the rightt, queue will be:", d1
    d1.rotate(-2)
    print "After rotating from the right, queue will be:", d1
dqueue()    

import collections as c

def def_dict():
    """This program demonstrates the working of a default_dict object in python."""
    d1 = c.defaultdict(dict)
    print '\nInitially first dictionary is: ', dict(d1)
    l = [('a', 1), ('b', 2), ('a', 27), ('c', 3), ('d', 4), ('c', 29), ('e', 5)]
    for a, b in l:
        d1[a] = b
    print '\nAfter adding elements to the default dictionary, it is: ', dict(d1)
    print '\nItems in the first dictionary is: ', d1.items()
    st = 'malayalam'
    print '\n\nCreating dictionary from the string', st
    d2 = c.defaultdict(int)
    print '\nInitially second dict is:', dict(d2)
    for i in st:
        d2[i] = st.count(i)
    print "After updation, the second dictionary becomes: ", dict(d2)

def_dict()

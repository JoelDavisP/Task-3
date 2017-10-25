import collections as c

def ord_dict():
    """This program demonstrates the working of an ordered_dict object in python."""
    dic1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    d1 = c.OrderedDict(dic1)
    print '\nAdding elements to the dictionary : ', dict(d1) #This may or may not be the same order of d1.
    dic1['f'] = 6
    dic1['g'] = 7
    dic1['h'] = 8
    print '\nAfter inserting three elements (\'g\',\'f\', and \'h\'), resulting dictionary is', dic1 #Insertion preserves the order of dic1
    dic1.pop('c')
    dic1.pop('f')
    print "\nDictionary after deleting two random elements (\'c\' and \'f\') is : ", dic1
    
    dic1['c'] = 46
    print "\nDictionary after inserting the same element(\'c\') with another value once again.", dic1
ord_dict()

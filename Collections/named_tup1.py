import collections as c
 
def area_rect():
    """This is to demonstrate the named couple module in python. It prints the area of a rectangle having length 'l' and breadth 'b'."""
    rect = c.namedtuple('Rectangle', 'l b')
    r1 = rect(5, 10)
    print r1
    area = r1[0] * r1[1]
    print "Area of the rectangle 'r1' is ", area  

area_rect()   

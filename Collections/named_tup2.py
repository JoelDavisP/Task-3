import collections as c
import math 
def hypo_right_tri():
    """This is to demonstrate the named couple module in python. It prints the hypotenus of a right angle triangle having side 'a' and 'b'."""
    right_tri = c.namedtuple('Right_angle_triangle_two_sides', 'a b')
    r1 = right_tri(6, 8)
    print r1
    hypo = math.sqrt(r1[0]**2 +  r1[1]**2)
    print "Hypotenus of the right angle triangle 'r1' is ", hypo  

hypo_right_tri()

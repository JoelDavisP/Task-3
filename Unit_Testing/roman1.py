class OutOfRangeError(ValueError):
    pass


class NotIntegerError(ValueError):
    pass


class InvalidRomanNumeralError(ValueError):
     pass


roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))
import re

def to_roman(n):
    '''convert integer to Roman numeral'''
    if n > 3999 or n <= 0:
        raise OutOfRangeError("Number out of range (Must less than 4000 and greater than zero)")
    if not isinstance(n, int):
        raise NotIntegerError("Non integers cant be converted.")
    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
            #print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))
    return result

def from_roman(s):
    """ Convert roman numeral to integer"""
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    if re.match(pattern, s):
        result = 0
        index = 0
        for numeral, integer in roman_numeral_map:
            while s[index: index + len(numeral)] == numeral:
                result += integer
                index += len(numeral)
            #print('found', numeral, 'of length', len(numeral), ', adding', integer)
    else:
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
    return result


#print from_roman("AGSVGN")
#print from_roman("MMMM")
#print from_roman("CMCM")
#print from_roman("IIMXCC")
#print from_roman("XXI")

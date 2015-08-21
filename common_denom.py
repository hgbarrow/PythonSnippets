def convertFracts(lst):
	""" This function conversts a list of fractions to a list of equivalent
		fractions with common denominators. 
		convertFracts([[1,2], [1,3], [1, 4]]) returns [[6,12], [4,12], [3,12]]
		"""
    out_lst = lst
    denom = lst[0][1]
    for i in range(1, len(lst)):
        denom = lcm(denom, lst[i][1])
    
    for fraction in out_lst:
        fraction[0] = fraction[0] * (denom / fraction[1])
        fraction[1] = denom
    return out_lst
    
def gcd(a, b):
	""" compute the greatest common denominator """
    while b:
        a, b = b, a % b
    return a
    
def lcm(a, b):
	""" compute the least common multiple """
    return a * b / gcd(a, b)
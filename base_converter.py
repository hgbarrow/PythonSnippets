from math import pi

def converter(n, decimals=0, base=pi):
    """takes n in base 10 and returns it in any base (default is pi)
    with optional x decimals"""
    
	# digit can be alphanumermic (max base = 36)
    numeration = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    out_str = ""
    
	# check if number is negative
    if n < 0:
        n = -1 * n
        out_str += '-'
    
	# determine the number of digits needed
    digits = 0
    while base ** (digits + 1) <= n:
        digits += 1
	
	# Build output string
	remainder = n
    for i in range(digits, -1 - decimals, -1):
        digit = int(remainder / (base ** i))
        remainder = remainder - digit * (base ** i)
        if i == -1:
            out_str += '.'
        out_str += numeration[digit]
         
    return out_str
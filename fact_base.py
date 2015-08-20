from math import factorial

def dec2FactString(nb):
  """ This function converts a base 10 number to the factorial number system 
      https://en.wikipedia.org/wiki/Factorial_number_system   """
  num_str = '0'
  if nb <= 0:
      return num_str
  
  # find largest factorial base
  largest_base = 0
  while nb >= factorial(largest_base):
      largest_base += 1
  largest_base -= 1
  
  digit = ['0'] * largest_base
  digit[0] = str(nb / factorial(largest_base))
  remainder = nb % factorial(largest_base)
  for i in range(largest_base - 1, 0, -1):
      digit[largest_base - i] = str(remainder / factorial(i))
      remainder = remainder % factorial(i)
  for i in range(0, len(digit)):
      if int(digit[i]) > 9:
          digit[i] = chr(int(digit[i]) + 55)
  return "".join(digit) + '0
  
def factString2Dec(string):
  """ This function converts a string in the factorial number system back to decimal """
  num_out = long(0)
  string_rev = string[::-1]
  for i in range(0, len(string_rev)):
      if ord(string_rev[i]) - 64 > 0:
          digit = ord(string_rev[i]) - 55
      else:
          digit = int(string_rev[i])
      num_out += factorial(i) * digit
  return num_out

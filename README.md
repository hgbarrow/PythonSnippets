# Henry Barrow's PythonSnippets
This repository contains a variety of small python programs and functions I have written for practice

##Contents:##

File Name | Description
----------|-------------
**base_converter.py** | This script contains the function converter(n, decimals = 0, base = pi). This function takes a number, n in base 10 and returns it in any base (default is pi) with optional x decimals
**common_denom.py** | This script contains the functions convertFracts(lst), gcd(a, b), and lcm(a, b). The function convertFracts(lst) conversts a list of fractions to a list of equivalent fractions with common denominators. convertFracts([[1,2], [1,3], [1, 4]]) returns [[6,12], [4,12], [3,12]]
**fact_base.py** | This script contains two functions: dec2FactString(nb) and factString2Dec(string). These functions are used to convert between the factorial number systerm and base 10 (https://en.wikipedia.org/wiki/Factorial_number_system). 
**human_time.py** | This script contains the function format_duration(seconds). This function takes and arbitrary amount of seconds and returns an easy to read string. i.e. 3 hours, 15 minutes and 4 seconds.
**nested_struct_comp.py** | This program script contains the function same_structure_as(list_a, list_b). This function recursively compares two list to see if they share the same structure. i.e. same_structure_as([1,[1,1]] , [2,[2,2] ]) returns True and same_structure_as([1, [1,1]], [[2,2], 2]) returns False


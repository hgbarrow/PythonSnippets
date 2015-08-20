def same_structure_as(list_a, list_b):
	""" This function recursively compares two list to see if they share the same structure
		i.e. same_structure_as([ 1, [ 1, 1 ] ] , [ 2, [ 2, 2 ] ]) returns True and 
		same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ) returns False"""
    print "{}, {}".format(list_a, list_b)
    if type(list_a) is not type(list_b):
        if type(list_a) is list or type(list_b) is list:
            return False
    if type(list_a) is list:
        if len(list_a) != len(list_b):
            return False
        for i in range(0, len(list_a)):
            if (type(list_a[i]) is not list) and (type(list_b[i]) is not list):
                pass
            elif type(list_a[i]) is not type(list_b[i]):
                return False
            if (type(list_a[i]) is list) and (len(list_a[i]) != len(list_b[i])):
                return False
                
            else:
                out = same_structure_as(list_a[i], list_b[i])
                if not out:
                    return False
    return True
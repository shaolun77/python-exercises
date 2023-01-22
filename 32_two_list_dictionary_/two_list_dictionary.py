def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

   # had to get this from the solution.
   # I read up on enumerate(), which is useful, it gives you back two loop variables:
    # The count of the current iteration
    # The value of the item at the current iteration 

    # so in this case, idx is the index(count) of the key, and val is the value...
    # but the next line I don't understand. 
    # out[val] is putting the value of the key into the dict
    # values[idx] is the information at the same index of values
    # to = them... that puts them into a key:value format? 
    
# example
# ["a", "b"]
# [1]

#as long as the index you're looking at is less than the length of the second list, 
#you know that there will be information there 

#{"a": 1, "b": None}

    out = {}

    for idx, val in enumerate(keys):
        out[val] = values[idx] if idx < len(values) else None

        # if idx < len(values):
        #     out[val] = values[idx]
        # else:
        #     out[val] = None  

    return out


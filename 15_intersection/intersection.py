def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
     set2 = set(l2)
    # make l2 a set to remove any duplicates
    # loop over l1 and if any match, return the val inside a list.
     return [val for val in l1 if val in set2]

# built in method:
# turn both into sets (duplicates removed), return a list of both
# but i don't know how the & operator works here
     return list(set(l1) & set(l2))
def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    # num in nums % 4 == 0 (loop and see what's divisible by 4)
    # can it be just returned as a list? or create a new list first? 

    # then loop through new list and multiply each by 3, and return it. 

    # res = []
    # for num in nums: 
    #     if num % 4 == 0: 
    #         res.append(num*3)
            # return res


    # list comprehension way:

    return [num * 3 for num in nums if num % 4 == 0]





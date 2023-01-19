def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    #make the letter to swap lowercase...
    to_swap = to_swap.lower()
    #make an empty string
    swapped = ""

    #check each letter in the phrase to see if it's the same letter
    #if it's the same letter, then swap the casing
    #then put it in the empty string.
    
    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        swapped += ltr

    return swapped
    
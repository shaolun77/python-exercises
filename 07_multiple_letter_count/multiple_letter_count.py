def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counter = {}
    #use a for loop, iterate over the phrase
    #for each letter, go find the correponding ltr (the key) using '.get', and add 1 to the value.

    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1
    
    return counter

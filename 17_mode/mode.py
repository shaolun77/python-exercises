def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # Make dict with key-value pair num:freq
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # built in method: find the max value in the dict

    max_value = max(counts.values())

    # return the num that equals the max value
    # use .items method to iterate over the key-value pairs of the dictionary, as tuples in a list.

    for (num, freq) in counts.items():
        if freq == max_value:
            return num

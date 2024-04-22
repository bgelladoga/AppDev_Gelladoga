"""
My very own new module
"""

ring_inventory = list(zip([3, 7, 9, 1],
                          ['elven-kings', 'dwarf-lords', 'mortal men', 'Dark Lord']))

def maxmin(num_list):
    """
    Parameter: A list of numbers
    Returns: maximum and minimun values in the list
    """

    largest_so_far = None
    smallest_so_far = None

    for the_num in num_list:
        if (largest_so_far is None) or (the_num > largest_so_far):
            largest_so_far = the_num

        if (smallest_so_far is None) or (the_num < smallest_so_far):
            smallest_so_far = the_num

    return (largest_so_far, smallest_so_far)

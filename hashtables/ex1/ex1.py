def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create empty dict
    sums = {}
    # create empty list to be the return
    results = []
    # using enumerate to have access to the index and the value
    for i, num in enumerate(weights):
        # check to see if the limit - the current num is in sums dict already
        if limit - num in sums:
            # if it is, append the current value and the value that matches
            # it to equal the limit
            results.append(i)
            results.append(sums[limit- num])
            # then end function with a return on the index list
            return results
        # otherwise, we add the value with it's index to the dictionary
        sums[num] = i
get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)
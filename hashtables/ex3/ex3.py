def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create empty dict
    nums_dict = {}
    # create empty list
    result = []
    # going through the first list in our list of lists
    for num in arrays[0]:
        # appending the values from the first list into our 
        # dict with an arbitrary value
        nums_dict[num] = 0
    # afterwards, go through the rest of the lists to check which numbers
    # they share with the first list
    for num in arrays[1:]:
        # going through the items in each list and seeing if it exists
        # in the dict created by the first list
        for item in num:
            if item in nums_dict:
                # checking to see if the item is in the dict and then
                # checking to make sure it isn't already in our results list
                if item not in result:
                    result.append(item)
    # return populated list of common numbers
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

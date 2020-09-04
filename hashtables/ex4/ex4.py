def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create empty dict
    nums_dict = {}
    # create empty list
    result = []
    # going through our numbers list and appending 
    # the negative values to our dict
    for num in a:
        if num < 0:
            nums_dict[num] = 0
    # reiterating through our list for the positive numbers
    # and seeing if their negative counterpart is in the dictionary
    for num in a:
        if num > 0:
            if num * -1 in nums_dict:
                # if it is, then we append the number to the results list
                result.append(num)
    # return our populated list
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

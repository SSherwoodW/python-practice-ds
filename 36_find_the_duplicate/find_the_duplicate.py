def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    new_list = []
    for num in nums:
        if num in new_list:
            return num
        elif not num in new_list:
            new_list.append(num)


    #seen = set()
    #for num in nums:
        #if num in seen:
            #return num
        #seen.add(num)
                    #This better and faster and cleaner
        
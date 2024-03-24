def search(nums: [int], target: int):
    """
    Search for a target value in a list of integers.

    Args:
        nums (List[int]): The list of integers to search in.
        target (int): The target value to search for.

    Returns:
        int: The index of the target value in the list, or -1 if not found.
    """
    if target in nums:
        return nums.index(target)

    return -1

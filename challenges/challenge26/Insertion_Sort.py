def insertion_sort(input):
    """
    Sorts an input list in ascending order using the Insertion Sort algorithm.

    Args:
        input (list): The input list to be sorted.

    Returns:
        list: The sorted list in ascending order.

    Examples:
        >>> arr = [20, 18, 12, 8, 5, -2]
        >>> sorted_arr = insertion_sort(arr)
        >>> print(sorted_arr)
        [-2, 5, 8, 12, 18, 20]
    """
    sorted = []
    if len(input) == 0:
        return sorted

    sorted.append(input[0])

    for i in range(1, len(input)):
        insert(sorted, input[i])

    return sorted

def insert(sorted, value):
    """
    Inserts a value into the sorted list at the appropriate position.

    Args:
        sorted (list): The sorted list to insert the value into.
        value (int): The value to be inserted.

    Returns:
        None

    Examples:
        >>> sorted = [2, 5, 7, 10]
        >>> value = 3
        >>> insert(sorted, value)
        >>> print(sorted)
        [2, 3, 5, 7, 10]
    """
    i = 0

    while i < len(sorted) and value > sorted[i]:
        i += 1

    sorted.append(None)
    j = len(sorted) - 1

    while j > i:
        sorted[j] = sorted[j - 1]
        j -= 1

    sorted[i] = value

# Example usage:
arr = [20,18,12,8,5,-2]
sorted_arr = insertion_sort(arr)
print(sorted_arr)

"""To implement a binary search algorithm."""

def find(search_list, value):
    """Binary search only works when a list has been sorted."""
    left = 0
    right = len(search_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if search_list[middle] == value:
            return middle

        if value < search_list[middle]:
            right = middle - 1
        else:
            left = middle + 1

    raise ValueError("value not in array")

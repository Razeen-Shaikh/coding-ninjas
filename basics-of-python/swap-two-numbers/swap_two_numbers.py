from typing import List

def swap_number(a:List,  b: List) -> None:
    """
    Swaps the contents of two lists.

    Args:
        a (list): The first list.
        b (list): The second list.

    Returns:
        None
    """
    temp = a[:]
    a[:] = b[:]
    b[:] = temp

#!/usr/bin/env python3
"""index_range function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function should return a tuple of size two
    containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters
    """
    return (page_size * (page - 1), page_size * page)

#!/usr/bin/env python3
"""index_range function"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function returns a tuple of size two
    containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters
    """
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return (self.__dataset)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset
        (i.e. the correct list of rows) based on page and page size"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        res = index_range(page, page_size)

        if page > len(self.dataset()) / page_size:
            return []
        else:
            return self.dataset()[res[0]: res[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns page_size, page, data, next_page, prev_page,
        and total_pages"""
        data = self.get_page(page, page_size)
        returned_page_size = len(data)
        total_pages = math.ceil((len(self.dataset()) / page_size))
        next_page = page + 1 if page < total_pages else None
        prev_page = None if page == 1 else page - 1
        result = {
            "page_size": returned_page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

        return (result)

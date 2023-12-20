# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from typing import Type, Union

from bluelily.platform.top import (
    top_repositories,
    top_users
)

from bluelily import (
    Repository,
    User
)

from enums import (
    Sort,
    SortOrder
)


class GitHub:
    @staticmethod
    def top(query_type: Union[Type[Repository], Type[User]], number: int, sort: Sort, sort_order: SortOrder = SortOrder.DESCENDING):
        if type(query_type) is Repository:
            return top_repositories(number, sort, sort_order)

        return top_users(number, sort, sort_order)

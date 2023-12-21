# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from typing import Type

from bluelily.platform.top import (
    top_repositories,
    top_users
)

from bluelily import (
    Repository,
    User,
    Commit
)

from enums import (
    Sort,
    SortOrder,
    Language,
    SpokenLanguage
)


TOP_QUERY_TYPES = Type[Repository | User]
SEARCH_QUERY_TYPES = Type[Repository | User | Commit]  # todo: ad pr's discussions etc. when i implement them


class GitHub:
    @staticmethod
    def top(query_type: TOP_QUERY_TYPES, number: int, sort: Sort, sort_order: SortOrder = SortOrder.DESCENDING):
        response = {
            Repository: lambda: top_repositories(number, sort, sort_order),
            User: lambda: top_users(number, sort, sort_order)
        }

        return response[query_type]()

    @staticmethod
    def search(query_type: SEARCH_QUERY_TYPES, number: int, sort: Sort, sort_range: range, language: Language = Language.ANY, spoken_language: SpokenLanguage = SpokenLanguage.ANY):
        return

    @staticmethod
    def trending():
        return

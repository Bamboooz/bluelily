# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import requests

from bluelily import token

from enums import (
    Sort,
    SortOrder
)

from bluelily.logging import (
    log,
    Level
)


def top_repositories(number: int, sort: Sort, sort_order: SortOrder = SortOrder.DESCENDING):
    """
    Fetches top {number} repositories from GitHub in parameter: stars, watchers and forks at a certain order.
    Selecting ASCENDING order basically gives you {number} random repositories with 0 of your search parameter.
    :param number:
    :param sort:
    :param sort_order:
    """
    if sort == Sort.FOLLOWERS:
        sort = Sort.WATCHERS

    api_call_url = "https://api.github.com/search/repositories"

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    params = {
        "q": f"{sort}:{sort_order.value}0",
        "sort": sort.value,
    }

    if token is not None:
        response = requests.get(api_call_url, params=params, headers=headers)
    else:
        response = requests.get(api_call_url, params=params)

    if response.status_code == 200:
        log(f"Successfully fetched top GitHub repositories, sorted by {sort.value}.", Level.INFO)
        return response.json()["items"][0:number]  # first {number} elements form the api call list
    else:
        log(f"Failed to fetch top GitHub repositories, sorted by {sort.value}. Response code: {response.status_code}.", Level.ERR)
        return None


def top_users(number: int, sort: Sort, sort_order: SortOrder = SortOrder.DESCENDING):
    """
    Fetches top {number} users from GitHub in parameter: stars, watchers and forks at a certain order.
    Selecting ASCENDING order basically gives you {number} random users with 0 of your search parameter.
    :param number:
    :param sort:
    :param sort_order:
    """
    api_url = {
        Sort.FOLLOWERS: f"https://api.github.com/search/users?q=followers:{sort_order.value}0&sort=followers"
    }

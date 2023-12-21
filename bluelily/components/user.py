# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import requests

from bluelily import token

from bluelily.logging import (
    log,
    Level
)


class User:
    def __init__(self, username):
        self.user = username
        self.url = f"https://github.com/{username}"
        self.api_url = f"https://api.github.com/users/{username}"
        self.raw_data = self._fetch_data()
        self.exists = self.raw_data is not None

        log(f"Successfully initiated {self.user} GitHub user.", Level.INFO)

    def _fetch_data(self):
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
        }

        if token is not None:
            response = requests.get(self.api_url, headers=headers)
        else:
            response = requests.get(self.api_url)

        if response.status_code == 200:
            log(f"Successfully fetched {self.user} GitHub user information.", Level.INFO)
            return response.json()
        else:
            log(f"Failed to fetch {self.user} GitHub user information. Response code: {response.status_code}.", Level.ERR)
            return None

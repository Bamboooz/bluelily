# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import requests

from bluelily.logging import (
    log,
    Level
)


class Gist:
    def __init__(self, user: str, gist_id: str):
        self.user = user
        self.gist_id = gist_id
        self.url = f"https://gists.github.com/{user}/{gist_id}"
        self.api_url = f"https://api.github.com/users/{user}/gists/{gist_id}"
        self.raw_data = self._fetch_data()
        self.exists = self.raw_data is not None

        log(f"", Level.INFO)

    def _fetch_data(self):
        response = requests.get(self.api_url)

        if response.status_code == 200:
            log(f"Successfully fetched {self.user}/{self.gist_id} GitHub gist information.", Level.INFO)
            return response.json()
        else:
            log(f"Failed to fetch {self.user}/{self.gist_id} GitHub gist information. Response code: {response.status_code}.", Level.ERR)
            return None

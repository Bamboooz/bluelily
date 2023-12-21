# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bluelily import Branch

import os
import subprocess
import requests

from bluelily.logging import (
    log,
    Level
)


class Repository:
    def __init__(self, user: str, repo: str):
        from bluelily import Branch
        self.user = user
        self.repo = repo
        self.url = f"https://github.com/{user}/{repo}"
        self.api_url = f"https://api.github.com/repos/{user}/{repo}"
        self.main_branch = Branch(self, "master")
        self.raw_data = self._fetch_data()
        self.exists = self.raw_data is not None

        log(f"...", Level.INFO)

    def _fetch_data(self):
        response = requests.get(self.api_url)

        if response.status_code == 200:
            log(f"Successfully fetched {self.user}/{self.repo} GitHub repository information.", Level.INFO)
            return response.json()
        else:
            log(f"Failed to fetch {self.user}/{self.repo} GitHub repository information. Response code: {response.status_code}.", Level.ERR)
            return None

    def clone(self, path: str, branch: Branch = None):
        if not branch:
            branch = self.main_branch

        if branch.parent_repo != self:
            log(f"...", Level.ERR)
            return

        if not os.path.exists(path):
            if branch == self.main_branch:
                log(f"...", Level.ERR)
            else:
                log(f"...", Level.ERR)

            return

        if os.path.exists(os.path.join(path, branch.folder_name)):
            return

        command = ["git", "clone", "-b", branch.branch_name, self.url, branch.folder_name]

        try:
           subprocess.run(command, check=True)
           print(f"...")
        except subprocess.CalledProcessError as e:
           print(f"...: {e}")

        log(f"...", Level.INFO)

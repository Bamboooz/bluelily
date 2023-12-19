# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os

from src.bluelily.logging import (
    log,
    Level
)


class Repository:
    def __init__(self, user: str, repo: str):
        self.user = user
        self.repo = repo
        self.url = f"https://github.com/{user}/{repo}"
        self.api_url = f"https://api.github.com/repos/{user}/{repo}"
        
        log(f"Successfully initialised {user}/{repo} GitHub repository.", Level.INFO)

    def __repr__(self):
        return self.url

    def clone(self, path: str):
        if not os.path.exists(path):
            log(f"Failed to clone {self.user}/{self.repo}, target directory: {path} does not exist.", Level.ERR)
            return
        
        log(f"Cloning {self.url} to {path}.", Level.INFO)

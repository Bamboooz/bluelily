# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from src.bluelily.components.repo import Repository
from src.bluelily.components.changes import Changes

from src.bluelily.logging import (
    log,
    Level
)


class Commit:
    def __init__(self, changes: Changes):
        log("Successfully created a commit with id 5", Level.INFO)

    def push(self, repo: Repository, message: str):
        log("Successfully pushed a commit with id 5 to {repo.user}/{repo.repo}", Level.INFO)

# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bluelily import Repository


class Branch:
    def __init__(self, repo: Repository, branch_name: str):
        self.branch_name = branch_name
        self.parent_repo = repo
        self.folder_name = f"{repo.repo}-{branch_name}"

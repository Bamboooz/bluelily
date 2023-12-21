# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bluelily import Changes

from bluelily.logging import (
    log,
    Level
)


class Commit:
    def __init__(self, changes: Changes):
        log("Successfully created a commit with id 5", Level.INFO)

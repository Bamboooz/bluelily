# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from enum import Enum


class Language:
    ANY = "any"
    PYTHON = "python"


class SpokenLanguage(Enum):
    ANY = "any"


class Sort(Enum):
    FOLLOWERS = "followers"
    STARS = "stars"
    WATCHERS = "watchers"
    FORKS = "forks"


class SortOrder(Enum):
    ASCENDING = "<="
    DESCENDING = ">"

# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import enum

from src.bluelily.bluelily import log_actions


class Level(enum.Enum):
    INFO = 0,
    WARN = 1,
    ERR = 2


def log(msg: str, log_level: Level):
    log = {
        Level.INFO: lambda: print(f"[bluelily: info]: {msg}"),
        Level.WARN: lambda: print(f"[bluelily: warn]: {msg}"),
        Level.ERR: lambda: print(f"[bluelily: err]: {msg}"),
    }

    if log_actions:
        log[log_level]()

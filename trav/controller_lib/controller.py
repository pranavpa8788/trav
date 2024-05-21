from __future__ import annotations

from abc import ABC

import trav.mode_lib.mode_manager as mode_manager


class Controller(ABC):
    def __init__(self):
        self.modeManager: mode_manager.ModeManager

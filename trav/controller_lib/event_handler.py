from functools import partial
from typing import Dict, Callable, Any

from trav.tree_lib.tree import Tree
from trav.controller_lib.key import Key
from trav.utils import Utils


class EventHandler:
    EventMap: Dict[Key, Callable] = {
    }

    @classmethod
    def registerForEvent(cls, key: Key, func: Callable) -> None:
        cls.EventMap[key] = func

    @classmethod
    def handleEvent(cls, key: Key, **kwargs: Any) -> None:
        cls.EventMap[key](**kwargs)


    @classmethod
    def isValidEvent(cls, event: Any) -> bool:
        return event in cls.EventMap.keys()

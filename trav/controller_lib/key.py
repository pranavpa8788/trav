from __future__ import annotations

from typing import Optional


def keyToString(function):
    def wrapper(*args, **kwargs):
        args = list(args)
        args[1] = str(args[1])
        result = function(*args, **kwargs)
        return result

    return wrapper


class Key:
    def __init__(self, primaryValue: str, secondaryValue: str = None) -> None:
        self.primaryValue: str = primaryValue
        self.secondaryValue: str = secondaryValue

    def __hash__(self) -> int:
        return hash((self.primaryValue, self.secondaryValue))

    def __eq__(self, other: Key) -> bool:
        if isinstance(other, Key) and other:
            return self.primaryValue == other.primaryValue and self.secondaryValue == other.secondaryValue
        return False

    def __repr__(self) -> str:
        return f"Key(primaryValue: {self.primaryValue}, secondaryValue: {self.secondaryValue})"

    @staticmethod
    def isValidKey(key: Key):
        for k in vars(KEYS):
            if key == getattr(KEYS, k):
                return True
        return False

    @staticmethod
    def standardizeKey(primaryValue: str, secondaryValue: Optional[str] = None) -> Key:
        if not primaryValue and not secondaryValue:
            return None

        if primaryValue:
            primaryValue = Key.cleanKeyString(primaryValue)

        if secondaryValue:
            secondaryValue = Key.cleanKeyString(secondaryValue)

        standardizedKey: Key = Key(primaryValue, secondaryValue)

        return standardizedKey

    @staticmethod
    def cleanKeyString(keyString: str) -> str:
        if len(keyString) == 3 and not keyString.startswith("Key"):
            keyString = keyString.replace("'", "")
            keyString = f"Key.{keyString}"
        return keyString


class NullKey(Key):
    def __init__(self):
        super().__init__("", None)


class KEYS:
    K_LOWER = Key("Key.k")
    K_UPPER = Key("Key.K")

    J_LOWER = Key("Key.j")
    J_UPPER = Key("Key.J")

    UP_ARROW = Key("Key.up")
    DOWN_ARROW = Key("Key.down")
    LEFT_ARROW = Key("Key.left")
    RIGHT_ARROW = Key("Key.right")

    H_LOWER = Key("Key.h")
    H_UPPER = Key("Key.H")

    L_LOWER = Key("Key.l")
    L_UPPER = Key("Key.L")

    A_UPPER = Key("Key.A")
    A_LOWER = Key("Key.a")

    D_UPPER = Key("Key.D")
    D_LOWER = Key("Key.d")

    Q_UPPER = Key("Key.Q")
    Q_LOWER = Key("Key.q")

    E_UPPER = Key("Key.E")
    E_LOWER = Key("Key.e")

    ENTER = Key("Key.enter")

    ESCAPE = Key("Key.esc")

    GT = Key("Key.g", "Key.t")
    G_LOWER = Key("Key.g")
    T_LOWER = Key("Key.t")

    N_LOWER = Key("Key.n")
    N_UPPER = Key("Key.N")

    FORWARD_SLASH = Key("Key./")

    BACKSPACE = Key("Key.backspace")
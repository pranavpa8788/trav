from trav.mode_lib.mode import Mode
from trav.controller_lib.key import Key, NullKey, keyToString
from trav.controller_lib.event_handler import EventHandler


class TraverseMode(Mode):
    isKeyPressed: bool = False
    currentKey: Key = NullKey()
    previousKey: Key = NullKey()

    @classmethod
    def singleKeyPressed(cls):
        return not cls.isKeyPressed

    @classmethod
    def multipleKeysPressed(cls):
        return cls.isKeyPressed

    @classmethod
    def singleKeyReleased(cls):
        return (cls.previousKey is None) or (cls.currentKey == cls.previousKey)

    @classmethod
    def multipleKeysReleased(cls):
        return not cls.singleKeyPressed()

    @classmethod
    def handleKeyPress(cls, keyValue: str):
        if cls.singleKeyPressed():
            standardizedKey = Key.standardizeKey(keyValue)
            if EventHandler.isValidEvent(standardizedKey) and Key.isValidKey(standardizedKey):
                cls.isKeyPressed = True
                cls.currentKey = Key.standardizeKey(keyValue)
                cls.previousKey = cls.currentKey
        elif cls.multipleKeysPressed():
            primaryValue = cls.previousKey.primaryValue
            secondaryValue = keyValue
            standardizedKey = Key.standardizeKey(primaryValue, secondaryValue)
            if EventHandler.isValidEvent(standardizedKey) and Key.isValidKey(standardizedKey):
                cls.currentKey = Key.standardizeKey(cls.previousKey.primaryValue, keyValue)

    @classmethod
    def handleKeyRelease(cls, keyValue: str):
        if cls.multipleKeysReleased():
            cls.previousKey = None

        if cls.isKeyPressed:
            cls.isKeyPressed = False

            try:
                EventHandler.handleEvent(cls.currentKey)
            except KeyError:
                print(f"Action not found for key: {cls.currentKey}")

            if cls.modeManager.currentMode == TraverseMode:
                cls.modeManager.tree.printVerticalTree()







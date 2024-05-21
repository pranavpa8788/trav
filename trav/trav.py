from pynput import keyboard

from trav.mode_lib.mode_manager import ModeManager
from trav.controller_lib.event_handler import EventHandler
from trav.controller_lib.key import KEYS
from trav.tree_lib.tree_director import TreeDirector
from trav.controller_lib.keyboard_controller import KeyboardController


def runWSLTest(currentNodePath: str):
    treeDirector = TreeDirector(currentNodePath)

    treeDirector.constructTree()

    treeDirector.registerForEvents()

    EventHandler.handleEvent(KEYS.A_LOWER)

    treeDirector.endOperations.writeOutToFile()
    # treeDirector.displayTree()


def run(currentNodePath: str) -> None:

    treeDirector = TreeDirector(currentNodePath)

    treeDirector.constructTree()

    # tree.writeTreeToFile("../tests/sample.tree")
    keyboardController = KeyboardController()

    modeManager = ModeManager(treeDirector.tree, keyboardController)

    keyboardController.modeManager = modeManager

    treeDirector.registerForEvents(modeManager)

    # modeManager.writeOutToFile()
    treeDirector.displayTree()


    with keyboard.Listener(
            on_press=keyboardController.handleKeyPress,
            on_release=keyboardController.handleKeyRelease) as listener:
        modeManager.setListener(listener)
        listener.join()

if __name__ == "__main__":
    run(None)


    # print(headRootNode)
    # print("finished running")
    # Node.printVerticalTree(headRootNode)
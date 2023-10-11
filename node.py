class Node:
    def __init__(self, atr):
        if not isinstance(atr, str):
            raise TypeError(f"Atr needs to be str, not { type(atr) }")
        self.childs = dict()
        self.atrTest = atr

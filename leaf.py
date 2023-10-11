class Leaf:
    def __init__(self, label):
        if not isinstance(label, str):
            raise TypeError(f"label needs to be str not { type(label) }")
        self.label = label

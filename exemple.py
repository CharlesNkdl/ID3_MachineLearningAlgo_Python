class Exemple:
    def __init__(self, atrName, atrValue, label=""):

        if not isinstance(atrName,list) or not isinstance(atrValue, list):
            raise TypeError(f"Needs to be list, not { type(atrName) } and {type(atrValue) }")
        if not isinstance(label, str):
            raise TypeError(f" label needs to be str not { type(label) }")
        if len(atrValue) != len(atrName):
            raise ValueError("atrValue and atrName Needs to be the same length")
        self.label = label
        self.atrDict = dict()
        for i in range(len(atrName)):
            self.atrDict[atrName[i]] = atrValue[i]
    def __str__(self):
        return f"{self.atrDict} {self.label}"
    def __len__(self):
        return len(self.atrDict)

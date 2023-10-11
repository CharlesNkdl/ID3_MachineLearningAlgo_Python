import exemple
from math import log

class Dataset:
    def __init__(self, path=""):
        if not isinstance(path, str):
            raise TypeError(f"Need Str not { type(str) }")
        if path == "":
            self.atr = []
            self.exem = []
        else:
            with open(path, 'r') as ds:
                self.atr = ds.readline().lower().strip().split(' ')
                self.exem = self.exem_inex(ds.read().strip().lower().split('\n'),self.atr)

    def __len__(self):
        return len(self.exem)

    @staticmethod
    def exem_inex(ex, atrName):
        ret = list()
        print(atrName)
        for l in ex:
            atr = l.lower().strip().split(' ')
            label = atr[-1] if len(atr) != len(atrName) else ""
            oui = exemple.Exemple(atrName, atr[:len(atrName)], label)
            ret.append(oui)
        return ret

    def labPoss(self):
        ret = []
        for ex in self.exem:
            if ex.label not in ret:
                ret.append(ex.label)
        return ret

    def ssEnsLabel(self, label):
        ret = Dataset()
        ret.atr = self.atr[:]
        for ex in self.exem:
            if ex == label:
                ret.exem.append(ex)
        return ret

    def ssEnsAtr(self, atrName, value):
        ret = Dataset()
        ret.atr = self.atr[:]
        ret.atr.remove(atrName)
        for ex in self.exem:
            if ex.atrDict[atrName] == value:
                ret.exem.append(ex)
        return ret

    #Entropie de Shannon
    def entropy(self):
        ret = 0
        for label in self.labPoss():
            ssEns = self.ssEnsLabel(label)
            lenSsEns = len(ssEns)
            if lenSsEns != 0:
                ret += lenSsEns * log(lenSsEns, 2)
        return log(len(self),2) - ret/len(self)

    def atrOpti(self):
        max, ret = float("-inf"), ""
        for atr in self.atr:
            gain = self.gainEntro(atr)
            if gain >= max :
                max, ret = gain, atr
        return ret

    def possAtrValue(self, atrName):
        ret = []
        for ex in self.exem:
            if not ex.atrDict[atrName] in ret:
                ret.append(ex.atrDict[atrName])
        return ret

    def gainEntro(self, atrName):
        ret = 0
        for v in self.possAtrValue(atrName):
            ssEns = self.ssEnsAtr(atrName, v)
            ret += len(ssEns) * ssEns.entropy()
        return self.entropy() - ret/len(self)

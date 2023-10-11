from math import log
import dataset
import exemple
import node
import leaf

class ID3:
    def __init__(self, path=""):
        self.ds = dataset.Dataset(path)
        self.tree = None

    def construct(self):
        self.tree = self.__treeConstruct(self.ds)

    def __treeConstruct(self, ds):
        if not isinstance(ds, dataset.Dataset):
            raise TypeError(f"ds needs to be a Dataset, not a { type(ds) }")
        if len(ds) == 0:
            raise ValueError("ds can't be empty")
        if ds.entropy() == 0:
            return leaf.Leaf(ds.exem[0].label)
        if len(ds.atr) == 0:
            max, labelFinal = 0, ""
            for label in ds.labPoss():
                ssEns = ds.ssEnsLabel(label)
                if len(ssEns) > max:
                    max, labelFinal = len(ssEns), label
            return leaf.Leaf(labelFinal)
        atrTester = ds.atrOpti()
        noder = node.Node(atrTester)
        for v in ds.possAtrValue(atrTester):
            ssEns = ds.ssEnsAtr(atrTester, v)
            noder.childs[v] = self.__treeConstruct(ssEns)
        return noder

    def printeur(self):
        self.__printTree(self.tree)

    def __printTree(self, noder, nb_tabs = 0):
        if isinstance(noder, node.Node):
            print('\t' * nb_tabs + ' ' * (nb_tabs ) + noder.atrTest)
            for child in noder.childs:
                print('\t' * (nb_tabs) + ' ' * nb_tabs + '├── ' + str(child))
                self.__printTree(noder.childs[child], nb_tabs + 1)
        elif isinstance(noder,leaf.Leaf):
            print('\t' * nb_tabs + ' ' * nb_tabs + '└── ' + noder.label)
        else:
           raise TypeError(f"Nodes needs to be a Node or a leaf, not a { type(node) }")

    def labelleur(self, ex):
        actualNode = self.tree
        while not isinstance(actualNode, leaf.Leaf):
            val = ex.atrDict[actualNode.atrTest]
            actualNode = actualNode.childs[val]
        ex.label = actualNode.label

def usage(path):
    tree = ID3(path)
    tree.construct()
    tree.printeur()
    ex = exemple.Exemple(["outlook", "temperature", "humidity", "wind"],["sunny", "hot", "normal", "strong"])
    tree.labelleur(ex)
    print("etiquette : '{}'".format(ex.label))

if __name__ == "__main__":
    usage("/home/cnikdel/python/id3algo/example.txt")

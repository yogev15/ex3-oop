class Node:

    def __init__(self, key : int, tag : int = -1, info : str = 'white', pos = None):
        """
        constructor
        :param key:
        :param tag:
        :param color:
        """

        self.key = key
        self.tag = tag
        self.info = 'white'
        self.nodesIn = {} # (key = int , value = weight)
        self.nodesOut = {}# (key = int , value = weight)
        self.pos = pos

    # def __getNodesIn__(self):
    #     return self.nodesIn
    # def __getNodesOut__(self):
    #     return self.nodesOut







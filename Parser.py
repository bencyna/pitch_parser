class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, value):
        self.children.append(TreeNode(value))
        
    

class Parser:
    def __init__(self):
        self.parse_table = self.buildParsetable()
        self.parse_tree = None
    
    def buildParsetable(self):
        pass
      
    
    # returns the head of the parse tree
    def generateParseTree(self, tokens):
        pass
      
      
    def printParseTree(self):
        self.generateParseTree()
        # print it to the console nicely 
        pass
    
    
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, value):
        self.children.append(TreeNode(value))
        
    

class Parser:
    # reads in the tokens 
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.cur_token = tokens[self.position] if tokens else None

    # advances the token 
    def advance(self):
        self.position += 1
        if self.position >= len(self.tokens):
            self.cur_token = None
        else:
            self.cur_token = self.tokens[self.position]


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
    
    
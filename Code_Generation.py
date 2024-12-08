# Develop an algorithm that takes in AST and outouts our bit encodings for the sounds to be made for some other compiler to generate sound
class CodeGeneration:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}
        self.code = []
        
    def parseAssignment(self, node):
        # second child is the note value
        return node.children[1].value
    
    def parseTimes(self, node):
        # first child is the number of times to play
        loops = int(node.children[0].value)
        for i in range(loops):
            if not self.parsePlay(node.children[2]):
                return False    
      
    
    def parsePlay(self, node):
        vals_to_append = self.parseExpression2(node.children[1])
        for val in vals_to_append:
            if not self.generateCode(val):
                print(f"Error: variable {val} not initialised")
                return False
        
        return True
        
    def parseExpression(self, node):
        if len(node.children) == 1:
            return node.children[0].value
        
        self.variables[node.children[0].value] = self.parseAssignment(node.children[1])
      
    def parseExpression2(self, node):
        return_vals = []
        if node.children[0].value == "epsilon":
            return []
        
        return_vals.append(node.children[0].value)
        return_vals.extend(self.parseExpression2(node.children[1]))
        return return_vals
        

    def generateCode(self, variable):
        # algorithim to convert code into bit encodings of sound
        if variable[1] in "abcdefghijklmnopqrstuvwxyz":
            # its a variable name
            if variable not in self.variables:
                return False
            self.code.append(self.variables[variable])
        else:
            # its a sound
            self.code.append(variable)
            
        return True

    
    def parseAST(self, node):
        if node.value == 'S':
            # for each child call dfs
            for child in node.children:
                self.parseAST(child)
                
        elif node.value == "TIMES":
            if not self.parseTimes(node):
                return False
            
        elif node.value == "PLAY":
            if not self.parsePlay(node):
                return False
            
        elif node.value == "EXPRESSION":
            self.parseExpression(node)
            
        elif node.value == "EXPRESSION2":
            self.parseExpression2(node)
            
        return True
        
        
    def printCode(self):
        if not self.parseAST(self.ast):
            return False
        print("Printing code...")
        
        for line in self.code:
            print(line)
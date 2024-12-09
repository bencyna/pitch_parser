# Develop an algorithm that takes in AST and outouts our bit encodings 
# for the sounds to be made for some other compiler to generate sound
class CodeGeneration:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}
        self.code = []
        self.notes = []
        
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
            self.notes.append(self.variables[variable])
            self.code.append(self.convertToBits(self.variables[variable]))
        else:
            # its a sound
            self.notes.append(variable)
            self.code.append(self.convertToBits(variable))
        return True

    def convertToBits(self, note):
        # Convert note to bits
        pitch_map = {'C': '000', 'D': '001', 'E': '010', 'F': '011', 'G': '100', 'A': '101', 'B': '110'}
        duration_map = {'w': '000', 'h': '001', 'q': '010', 'e': '011', 's': '100'}
        octave_map = {'1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}

        pitch = pitch_map[note[0]]
        # convert octave to 3 bit binary 
        octave = octave_map[note[1]]
        duration = duration_map[note[2]]

        return pitch + octave + duration
    
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


    def getOrderedNotes(self):
        return self.notes
from collections import deque

'''
## CFG
S → EXPRESSON S | PLAY | TIMES | $
NOTE → <capital_letter A-H> <num> LENGTH  
LENGTH → w | h | q | e | s 
VAR →  <capital_letter A-Z> LET POSTVAR
LET → <lowercase_letter a-z> | <lowercase_letter a-z> LET
POSTVAR → ε | =NOTE
TIMES → NUMBER times {PLAY} S 
PLAY → play (Expression) S 
EXPRESSiON → NOTE | VAR
'''

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
        self.current_tokens = deque()
        self.head = TreeNode("Head") # 
        self.CFG ={
            'S': [["EXPRESSION", 'S'], ['PLAY'], ['TIMES'], ["$"]],
            'NOTE': [['A-H', 'LENGTH']],
            'LENGTH': [['w'], ['h'], ['q'], ['e'], ['s']],
            'VAR': ['A-Z', 'LET', 'POSTVAR'],
            'LET': [['a-z'], ['a-z', 'LET']],
            'POSTVAR': [['epsilon'], ['=','NOTE']],
            'TIMES': ['NUMBER', 'times', '{', 'PLAY', '}', 'S'],
            'PLAY': ['play', '(', 'EXPRESSION', ')', 'S'],
            'EXPRESSION': [['NOTE'], ['VAR']],
        }
        self.terminals = {'A-H', 'A-Z', 'a-z', '=', '{', '}', '(', ')', 'w', 'h', 'q', 'e', 's', 'play', 'times', 'NUMBER', '$'}
        
        

    # advances the token 
    def advance(self):
        self.position += 1
        if self.position >= len(self.tokens):
            self.cur_token = None
        else:
            self.cur_token = self.tokens[self.position]


    def __init__(self):
        self.parse_tree = self.buildParseTree()

    
    def buildParseTree(self, token_idx=0):
        if not self.current_tokens and not self.cur_token:
            return True
          
        # if the current token is a non-terminal
            # check if the non terminal matches the next chars

          
        # loop through CFG for first token in list
           # select the token and run CFG
      
      
    def printParseTree(self):
        self.generateParseTree()
        # print it to the console nicely 
        pass
    
    


# Example 1
tokens = [
    ('IDENTIFIER', 'Thats'),
    ('OPERATOR', '='),
    ('NOTE', 'G4w'),
    ('IDENTIFIER', 'That'),
    ('OPERATOR', '='),
    ('NOTE', 'G4h'),
    ('IDENTIFIER', 'Me'),
    ('OPERATOR', '='),
    ('NOTE', 'B4h'),
    ('IDENTIFIER', 'Espresso'),
    ('OPERATOR', '='),
    ('NOTE', 'C4q'),
    ('NOTE', 'B4q')
]    
parser = Parser(tokens)
parser.printParseTree()
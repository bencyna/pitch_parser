from collections import deque

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
        self.terminalQueue = deque('S')
        self.head = TreeNode("Head")
        self.CFG ={
            'S': [["EXPRESSION", 'S'], ['PLAY'], ['TIMES'], ["$"]],
            'POSTVAR': [['epsilon'], ['=','NOTE']],
            'TIMES': [['NUM', 'times', '{', 'PLAY', '}', 'S']],
            'PLAY': [['play', '(', 'EXPRESSION', ')', 'S']],
            'EXPRESSION': [['NOTE'], ['VAR', 'POSTVAR']],
        }
        self.terminals = {'$': '$','NOTE': 'NOTE', 'NUM':"INTEGER", 'play':'play', '(':'(', ')':')', 'times':'times', '{':'{', '}':'}', 'epsilon':'epsilon', '=':'=', 'VAR':'IDENTIFIER'}

    
    def buildParseTree(self, production_rule, token_pos):
        if token_pos >= len(self.tokens) and production_rule != '$':
            return False
          
        if production_rule in self.terminals:
            # does the token value or type match the rule
            tokenType, tokenValue = self.tokens[token_pos]
            
            # epsilon case and $ case
            if production_rule == '$' and token_pos >= len(self.tokens):
                print("End of tokens reached")
                return True

            
            if tokenType == self.terminals[production_rule] or tokenValue == self.terminals[production_rule]:
                print("Terminal rule success: ", production_rule, " at token pos: ", token_pos)
                if token_pos == len(self.tokens) - 1:
                    print("End of tokens reached!! Successful parse")
                return True
            
          
        else:
            for production in self.CFG[production_rule]:
                found_sucess = True
                cur_token_pos = token_pos
                for sub_rule in production:
                    if not self.buildParseTree(sub_rule, cur_token_pos):
                        found_sucess = False
                        break
                    else:
                        cur_token_pos += 1
                if found_sucess:
                    print("Production rule success: ", production_rule, " at token pos: ", token_pos)
                    return True
                  
            return False
       
                        
          

      
      
    def printParseTree(self):
        self.generateParseTree()
        # print it to the console nicely 
        pass
    


example =  [('Keyword', 'play'),
    ('Delimiter', '('),
    ('NOTE', 'A4w'),
    ('Delimiter', ')')]
parser = Parser(example)
parser.buildParseTree('S', 0)
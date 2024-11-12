from collections import deque

class TreeNode:
    def __init__(self, value, children = None):
        self.value = value
        self.children = children if children is not None else []

class Parser:
    # reads in the tokens 
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.CFG ={
            'S': [["EXPRESSION", 'S'], ['PLAY', 'S'], ['TIMES', 'S'], ["$"]],
            'POSTVAR': [['=','NOTE'], ['epsilon']],
            'TIMES': [['NUM', 'times', '{', 'PLAY', '}']],
            'PLAY': [['play', '(', 'EXPRESSION2', ')']],
            'EXPRESSION': [['NOTE'], ['VAR', 'POSTVAR']],
            'EXPRESSION2': [['NOTE', 'EXPRESSION2'], ['VAR', 'EXPRESSION2'], ['epsilon']],
        }
        self.terminals = {
            '$': '$',
            'NOTE': 'NOTE', 
            'NUM':"INTEGER", 
            'play':'play', 
            '(':'(', 
            ')':')', 
            'times':'times', 
            '{':'{', '}':'}', 
            'epsilon':'epsilon', 
            '=':'=', 
            'VAR':'IDENTIFIER'
        }
        self.head = self.buildParseTree('S', 0)
    
    def parseTreeTerminal(self, production_rule, token_pos):
        # Does the token value or type match the rule?
          tokenType, tokenValue = self.tokens[token_pos] if token_pos < len(self.tokens) else ('$', '$')
          
          # Handle $ case
          if production_rule == '$':
              # Succeed only if we've reached the end of tokens
              if token_pos >= len(self.tokens):
                  print("End of tokens reached!! Successful parse")
                  terminal_node = TreeNode('$')
                  return terminal_node

              else:
                  return None
          
          # Check if the terminal matches the token at this position
          if tokenType == self.terminals[production_rule] or tokenValue == self.terminals[production_rule]:
              print("Terminal rule success: ", production_rule, " at token pos: ", token_pos)
              # If at the last token, confirm successful parse
              terminal_node = TreeNode(self.terminals[production_rule])
              self.position += 1
              return terminal_node
          else:
              return None
    
    def parseTreeNonTerminal(self, production_rule, token_pos):
        # Try each production rule for the non-terminal
          children = []
          for production in self.CFG[production_rule]:
              children = []
              found_success = True
              for sub_rule in production:
                  if sub_rule == 'epsilon':
                      sub_rule_node = TreeNode(sub_rule)
                      children.append(sub_rule_node)
                      continue
                  # Recursively parse the sub_rule
                  child_node = self.buildParseTree(sub_rule, self.position)
                  if not child_node:
                      found_success = False
                      self.position = token_pos  # Reset the position if this production failed
                      break  # Stop if this production fails
                  else:
                      children.append(child_node)
              # If a production rule succeeded entirely, return success
              if found_success:
                  print("Production rule success: ", production_rule, " at token pos: ", token_pos)
                  production_node = TreeNode(production_rule, children)
                  return production_node
          
          # If no production matched, fail this rule
          return None
        
        
    def buildParseTree(self, production_rule, token_pos):
        print(production_rule, token_pos)
        # If we've gone past the end of the tokens, fail unless we're at the end symbol
        if token_pos >= len(self.tokens) and (production_rule != '$' and production_rule != 'S'):
            return None
        
        if production_rule in self.terminals:
            return self.parseTreeTerminal(production_rule, token_pos)
            
        else:
            return self.parseTreeNonTerminal(production_rule, token_pos)
       
    def printParseTree(self):
        self.generateParseTree()
        # print it to the console nicely 
        pass
      
    def levelOrderTraversal(self, start = None):
        # print the tree in level order
        cur_level = []
        q = deque()
        q.append(self.head if not start else start)
        levelCount = 1
        while q:
            node = q.popleft()
            cur_level.append(node.value)
            for child in node.children:
                q.append(child)
            
            levelCount -= 1
            if levelCount == 0:
                levelCount = len(q)
                print(cur_level)
                cur_level = []
                
    

              
            
            
                
                


# Sample usage
example1 =  [
  ('Keyword', 'play'),
    ('Delimiter', '('),
    ('NOTE', 'A4w'),
    ('NOTE', 'A4w'),
    ('Delimiter', ')')
    ]

example2 =  [
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

example3 =  [
    ('IDENTIFIER', 'Happy'),
    ('OPERATOR', '='),
    ('NOTE', 'A4w'),
    ('IDENTIFIER', 'Birthday'),
    ('OPERATOR', '='),
    ('NOTE', 'A4w'),
    ('NOTE', 'A4h'),
    ('NOTE', 'B4w'),
    ('NOTE', 'A4w'),
    ('NOTE', 'D4h'),
    ('IDENTIFIER', 'To'),
    ('OPERATOR', '='),
    ('NOTE', 'A4w'),
    ('NOTE', 'A4h'),
    ('NOTE', 'B4w'),
    ('NOTE', 'A4w'),
    ('IDENTIFIER', 'You'),
    ('OPERATOR', '='),
    ('NOTE', 'D4w'),
    ('INTEGER', '5'),
    ('Keyword', 'times'),
    ('Delimitter', '{'),
    ('Keyword', 'play'),
    ('Delimiter', '('),
    ('IDENTIFIER', 'Birthday'),
    ('IDENTIFIER', 'To'),
    ('IDENTIFIER', 'You'),
    ('Delimiter', ')'),
    ('Delimiter', '}')
]

example4 = [
  ('IDENTIFIER', 'Thats'),
  ('NOTE', 'G4w')
]

example5 = [
  ('IDENTIFIER', 'Thats'),
  ('OPERATOR', '='),
  ('NOTE', 'G4w'),
  ('NUM', '3')
]

parser = Parser(example4)
if parser.head:
    print("Parsing succeeded!")
    parser.levelOrderTraversal()
else:
    print("Parsing failed.")

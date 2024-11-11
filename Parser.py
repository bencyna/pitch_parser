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
        self.head = TreeNode("Head")
        self.CFG ={
            'S': [["EXPRESSION", 'S'], ['PLAY', 'S'], ['TIMES', 'S'], ["$"]],
            'POSTVAR': [['=','NOTE'], ['epsilon']],
            'TIMES': [['NUM', 'times', '{', 'PLAY', '}']],
            'PLAY': [['play', '(', 'EXPRESSION2', ')']],
            'EXPRESSION': [['NOTE'], ['VAR', 'POSTVAR']],
            'EXPRESSION2': [['NOTE', 'EXPRESSION2'], ['VAR', 'EXPRESSION2'], ['epsilon']],
        }
        self.terminals = {'$': '$','NOTE': 'NOTE', 'NUM':"INTEGER", 'play':'play', '(':'(', ')':')', 'times':'times', '{':'{', '}':'}', 'epsilon':'epsilon', '=':'=', 'VAR':'IDENTIFIER'}
    
    def parseTreeTerminal(self, production_rule, token_pos):
        # Does the token value or type match the rule?
          tokenType, tokenValue = self.tokens[token_pos] if token_pos < len(self.tokens) else ('$', '$')
          
          # Handle $ case
          if production_rule == '$':
              # Succeed only if we've reached the end of tokens
              if token_pos >= len(self.tokens):
                  print("End of tokens reached!! Successful parse")
                  return True
              else:
                  return False
          
          # Check if the terminal matches the token at this position
          if tokenType == self.terminals[production_rule] or tokenValue == self.terminals[production_rule]:
              print("Terminal rule success: ", production_rule, " at token pos: ", token_pos)
              # If at the last token, confirm successful parse
              self.position += 1
              return True
          else:
              return False
    
    def parseTreeNonTerminal(self, production_rule, token_pos):
        # Try each production rule for the non-terminal
          for production in self.CFG[production_rule]:
              found_success = True
              for sub_rule in production:
                  if sub_rule == 'epsilon':
                      continue
                  # Recursively parse the sub_rule
                  if not self.buildParseTree(sub_rule, self.position):
                      found_success = False
                      self.position = token_pos  # Reset the position if this production failed
                      break  # Stop if this production fails
              
              # If a production rule succeeded entirely, return success
              if found_success:
                  print("Production rule success: ", production_rule, " at token pos: ", token_pos)
                  return True
                    # If no production matched, fail this rule
        # If no production matched, fail this rule
          return False
        
        
    def buildParseTree(self, production_rule, token_pos):
        print(production_rule, token_pos)
        # If we've gone past the end of the tokens, fail unless we're at the end symbol
        if token_pos >= len(self.tokens) and (production_rule != '$' and production_rule != 'S'):
            return False
        
        if production_rule in self.terminals:
            return self.parseTreeTerminal(production_rule, token_pos)
            
        else:
            return self.parseTreeNonTerminal(production_rule, token_pos)
       
    def printParseTree(self):
        self.generateParseTree()
        # print it to the console nicely 
        pass
    def error(self, message):
        raise SyntaxError(message)

# Sample usage
example =  [
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

# Missing assignment for 'Thats' variable 
example4 = [
    ('IDENTIFIER', 'Thats'),
    ('NOTE', 'G4w')
]

# extra number 3
example5 = [
    ('IDENTIFIER', 'Thats'),
    ('OPERATOR', '='),
    ('NOTE', 'G4w'),
    ('NUM', '3')
]

# Test cases
examples = [example4]

for i, tokens in enumerate(examples):
  print(f"\nExample {i+1}:")
  parser = Parser(tokens)
  try:
    if parser.buildParseTree('S', 0):
      print("Parsing succeeded!")
    else:
      print("Parsing failed.")
  except SyntaxError as e:
    print(f"Parsing failed with error: {e}")
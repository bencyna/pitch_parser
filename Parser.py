from collections import deque

class TreeNode:
    def __init__(self, value, children = None, failed=False, error_msg=None):
        self.value = value
        self.children = children if children is not None else []
        self.failed = failed  # node failed parsing or not, set to false to begin w/
        self.error_msg = error_msg  # err msg if parse failed 

class Parser:
    # reads in the tokens 
    def __init__(self, tokens):
        self.tokens = tokens
        self.error_log = []
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
                  return TreeNode('$', failed=True, 
                          error_msg=f"Expected end $ input, found {tokenType}({tokenValue})")
          
          # Check if the terminal matches the token at this position
          if tokenType == self.terminals[production_rule] or tokenValue == self.terminals[production_rule]:
              print("Terminal rule success: ", production_rule, " at token pos: ", token_pos)
              # If at the last token, confirm successful parse
              terminal_node = TreeNode(self.terminals[production_rule])
              self.position += 1
              return terminal_node
          else: # doesn't match, make failed node
              return TreeNode(production_rule, failed=True, 
                       error_msg=f"Expected {production_rule}, found {tokenType}({tokenValue})")
    
    def parseTreeNonTerminal(self, production_rule, token_pos):
            best_partial_AST = None
            # Try each production rule for the non-terminal
            for production in self.CFG[production_rule]:
                self.position = token_pos  # Reset position for each attempt
                children = []
                success = True
                
                # Try to match each symbol in the production
                for sub_rule in production:
                    if sub_rule == 'epsilon':
                      sub_rule_node = TreeNode(sub_rule)
                      children.append(sub_rule_node)
                      continue
                    # Recursively parse the sub_rule
                    child_node = self.buildParseTree(sub_rule, self.position)
                    
                    if child_node and not child_node.failed:
                        children.append(child_node)
                    else:
                        success = False
                        if child_node:  # Keep track of partial matches
                            children.append(child_node)
                        break
                
                # If production succeeded completely, return success
                if success:
                    return TreeNode(production_rule, children)
                
                # Keep track of best partial match
                if len(children) > 0 and (not best_partial_AST or len(children) > len(best_partial_AST.children)):
                    best_partial_AST = TreeNode(production_rule, children, failed=True, 
                                        error_msg=f"Partial match for {production_rule}")
            
            # Return best partial match or failed node
            return best_partial_AST or TreeNode(production_rule, failed=True, 
                                        error_msg=f"Failed to match {production_rule}")
            
        
    def buildParseTree(self, production_rule, token_pos):
        print(production_rule, token_pos)
        # If we've gone past the end of the tokens, fail unless we're at the end symbol
        if token_pos >= len(self.tokens) and (production_rule != '$' and production_rule != 'S'):
            return None
        
        if production_rule in self.terminals:
            return self.parseTreeTerminal(production_rule, token_pos)
            
        else:
            return self.parseTreeNonTerminal(production_rule, token_pos)
       
      
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
                
    
    def print_ast(self, node=None, level=0, prefix="", is_last=True):
    
        # Prints the AST
        if node is None:
            # starts at the root(head) of the tree
            node = self.head
            print("\nAbstract Syntax Tree:")
        
        # the branch type (last or not)
        # print('***')

        if is_last:
            branch = "└──"
        else:
            branch = "├──"
        
        # Add error
        if node.failed:
            status = "  X -> " + node.error_msg
        else:
            status = ""
        # Prints the node w/branch
        print(f"{prefix}{branch if level > 0 else ''}─ {node.value}{status}")
            
        # Updates prefix (next level)
        if is_last:
            new_prefix = prefix + "    "
        else:
            new_prefix = prefix + "│   "
        
        # recursively print children, changing level + 1
        for i in range(len(node.children)):
            child = node.children[i]
            is_last_child = (i == len(node.children) - 1)
            self.print_ast(child, level + 1, new_prefix, is_last_child) 

# Examples:
if __name__ == "__main__":
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

    #Parsing fail, extra 5 at the end
    example4 = [
        ('IDENTIFIER', 'Thats'),
        ('NOTE', 'G4w'),
        ('INTEGER', '5'),
        ('Keyword', 'times')
    ]
    # Parsing fail, no brace at the end
    example5 = [
        ('IDENTIFIER', 'Thats'),
        ('OPERATOR', '='),
        ('NOTE', 'G4w'),
        ('INTEGER', '5'),  
        ('Keyword', 'times'),
        ('{', '{'),
        ('Keyword', 'play'),
        ('Delimiter', '('),
        # ('IDENTIFIER', 'Song'),
        # ('Delimiter', ')'),
        ('{', '}'),
    ]

    parser = Parser(example5)
    if parser.head:
        parser.print_ast()
        if any(node.failed for node in parser.head.children):
            print("\nParsing completed with errors (see X markers above)")
        else:
            print("Parsing succeeded!")


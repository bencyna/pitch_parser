from collections import deque

class TreeNode:
    def __init__(self, value, children = None, failed=False, error_msg=None, token_type=None):
        self.value = value
        self.children = children if children is not None else []
        self.failed = failed  # node failed parsing or not, set to false to begin w/
        self.error_msg = error_msg  # err msg if parse failed 
        self.token_type = token_type  # token type for terminals

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
              # terminal_node = TreeNode(self.terminals[production_rule])
              terminal_node = TreeNode(tokenValue, token_type=tokenType)

              self.position += 1
              return terminal_node
          else: # doesn't match, make failed node
              return TreeNode(production_rule, failed=True, 
                       error_msg=f"Expected {production_rule}, found {tokenType}({tokenValue})")
    
    def parseTreeNonTerminal(self, production_rule, token_pos):
            best_partial_AST = None # stores best partial 

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
                        # print("child "+ child_node.value)
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
                
    
    def print_ParseTree(self, node=None, level=0, prefix="", is_last=True):
    
        # Prints the ParseTree
        if node is None:
            # starts at the root(head) of the tree
            node = self.head
        
        # the branch type (last or not)
        # print('***')

        if is_last:
            branch = "└──"
        else:
            branch = "├──"
        
        # Add error and token type if present
        if node.failed:
            status = "  X -> " + node.error_msg
        elif node.token_type:
            status = f"  ({node.token_type})"
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
            self.print_ParseTree(child, level + 1, new_prefix, is_last_child) 


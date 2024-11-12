class LexerDfa:
  def __init__(self, input_str):
    self.input_str = input_str
    self.position = 0
    self.cur_char = input_str[self.position] if input_str else None
    self.tokens = []
    self.errors = [] # List of errors, and their defaults 
    self.prev_char = None  

  def advance(self):
    self.prev_char = self.cur_char
    self.position += 1
    if self.position >= len(self.input_str):
      self.cur_char = None
    else:
      self.cur_char = self.input_str[self.position]
      while self.cur_char == '\n':
          self.position += 1
          if self.position >= len(self.input_str):
              self.cur_char = None
              break
          self.cur_char = self.input_str[self.position]

  def note_token(self):
      # Handles DFA State for recognizing a note Token
      Token = []
      Token.append(self.cur_char)
      self.advance()
      if self.cur_char.isdigit() and int(self.cur_char) in range(1, 9):
          Token.append(self.cur_char)
          self.advance()
          if self.cur_char in "whqes":
              Token.append(self.cur_char)
              self.tokens.append(("NOTE", ''.join(Token)))  # End of Note Token
              self.advance() 
              return True  # Note parsed
          else:
            self.errors.append("Error: Invalid note token, missing duration w, h, q, e, s, default as w.")
            Token.append("w")
            self.tokens.append(("NOTE", ''.join(Token)))
            self.advance() 
            return True  # Note parsed
            # Defaults as whole note if no duration is given
      elif self.cur_char == '9':
          self.errors.append(f"Error: Invalid octave number {self.cur_char}, default as octave 4.")
          Token.append("4")
          self.advance()
          if self.cur_char in "whqes":
              Token.append(self.cur_char)
              self.tokens.append(("NOTE", ''.join(Token)))
              self.advance()
              return True
          else:
              self.errors.append("Error: Invalid note token, missing duration w, h, q, e, s, default as w.")
              Token.append("w")
              self.tokens.append(("NOTE", ''.join(Token)))
              self.advance()
              return True
      
      elif self.cur_char in "abcdefghijklmnopqrstuvwxyz":
        if self.variable_token():
            return True
      elif self.cur_char not in "abcdefghijklmnopqrstuvwxyz":
          Token.append("4")
          self.tokens.append(("NOTE", ''.join(Token)))
          self.errors.append("Error: Invalid note token, missing octave number 1-8, default as octave 4.")
          self.advance() 
          if self.cur_char in "whqes":
              Token.append(self.cur_char)
              self.tokens.append(("NOTE", ''.join(Token)))
              self.advance()
              return True
      return False  # Note not found
    
  def variable_token(self): 
    # Handles DFA State for recognizing a Identity Token
    var_token = [self.prev_char]  # Initialize var_token with the previous character
    # You can have a variable with assignment and variable without assignment 
    while self.cur_char is not None and self.cur_char in "abcdefghijklmnopqrstuvwxyz":
        var_token.append(self.cur_char)
        self.advance()
    self.tokens.append(("IDENTIFIER", ''.join(var_token)))
    if self.cur_char is not None and self.cur_char.isspace():
        self.advance()
    if self.cur_char == "=": # Then its being assigned to a note
        self.tokens.append(("OPERATOR", "="))
        self.advance()
        if self.cur_char is not None and self.cur_char.isspace():
          self.advance()  
          while self.cur_char is not None and self.cur_char in "ABCDEFG ": 
              if self.cur_char is not None and self.cur_char.isspace():
                  self.advance()
                  continue
              elif self.note_token():
                  continue
    else:
        return False

  def play_token(self): 
    # Handles DFA State for recognizing a Play Token
    if self.cur_char == "p":
      self.advance()
      if self.cur_char == "l":
        self.advance()
        if self.cur_char == "a":
          self.advance()
          if self.cur_char == "y":
            self.advance()
            self.tokens.append(("Keyword", "play"))
            if self.parenthesis_token():
              return True
          else:
            self.errors.append("Error: Missing y in play token.")
            self.tokens.append(("Keyword", "play"))
            if self.parenthesis_token():
              return True
    return False
  
  def parenthesis_token(self):
     # Handles DFA State for recognizing a Parenthesis Token
    if self.cur_char == "(":
      # print("parenthesis")
      self.advance()
      self.tokens.append(("DELIMITER", "("))
      # print(self.cur_char)  # it will either be variable starting with ABCDEFG variable with H-Z or a note
      
      if self.note_or_variable():
         if self.cur_char == ")":
            self.tokens.append(("DELIMITER", ")"))
            self.advance()
            # print("parenthesis2")
            return True
         else:
            # print(self.cur_char + "130")
            self.errors.append("Error: Missing ) in play token.")
            return False
    else:   
      self.errors.append("Error: Missing ( in play token.")
      if self.note_or_variable():
         if self.cur_char == ")":
            self.tokens.append(("DELIMITER", ")"))
            self.advance()
            return True
         else:
            # print(self.cur_char + "141")
            self.errors.append("Error: Missing ) in play token.")
            return False
      
    return False
     
  def note_or_variable(self):
    # Handles DFA State for recognizing a Note or Variable Token
    while self.cur_char is not None:
      if self.cur_char is not None and self.cur_char.isspace():
          self.advance()
          continue
      elif self.cur_char in "ABCDEFG":  # Notes or variable starting with A-G
          # print("note or variable")
          if self.note_token():  # Handle note
              continue
          elif self.cur_char in "abcdefghijklmnopqrstuvwxyz":  # Variable 
              # print("variable")
              if self.variable_token():
                  continue
      elif self.cur_char in "HIJKLMNOPQRSTUVWXYZ":  # Variable starting with H-Z
          # print("variable token")
          self.advance()
          if self.variable_token():
              continue
      else:
         # self.advance()
         return True

  def end_bracket(self):
      # Handles DFA state for recognizing the end bracket of a times token
      if self.cur_char == "}":
        self.tokens.append(("DELIMITER", "}")) # 
        self.advance()
        # This is an accept state
      else:
        self.errors.append("Error: Missing } in times token.")
        # This is an error state
     
  # Ignore white space, but remember for variables, they should be on a new line when declared?
  def run(self):
    while self.cur_char is not None:
      if self.cur_char is not None and self.cur_char.isspace():
        self.advance() 
        continue 
      while self.cur_char is not None and self.cur_char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ": # 
        if self.cur_char is not None and self.cur_char.isspace():
            self.advance()
            continue
        elif self.note_token(): # note 
          continue
        else:
          break

      if self.cur_char is not None and self.cur_char in "HIJKLMNOPQRSTUVWXYZ":  
        #This means its a variable token
        self.advance()
        if self.variable_token(): 
          continue
  
      elif self.play_token(): # play token
        continue
      
      elif self.cur_char is not None and self.cur_char.isdigit(): 
        self.tokens.append(("INTEGER", self.cur_char))
        self.advance()
        if self.cur_char == "t":
          self.advance()
          if self.cur_char == "i":
            self.advance()
            if self.cur_char == "m":
              self.advance()
              if self.cur_char == "e":
                self.advance()
                if self.cur_char == "s":
                  self.advance()
                  self.tokens.append(("Keyword", "times"))
                  if self.cur_char is not None and self.cur_char.isspace():
                    self.advance()
                  if self.cur_char == "{":
                    self.advance()
                    self.tokens.append(("Delimiter", "{"))
                    if self.cur_char is not None and self.cur_char.isspace():
                      # print("space")
                      self.advance()
                    elif self.play_token():
                       self.end_bracket()
                  else:
                    self.errors.append("Error: Invalid token, missing { in times token.")
                    self.tokens.append(("KEYWORD", "{"))
                    if self.cur_char is not None and self.cur_char.isspace():
                      self.advance()
                    elif self.play_token():
                      self.end_bracket()
                else:
                    self.errors.append("Error: Invalid token, missing s in times token.")
                    self.advance()
                    self.tokens.append(("KEYWORD", "times"))
                    if self.cur_char is not None and self.cur_char.isspace():
                      self.advance()
                    elif self.cur_char == "{":
                      self.advance()
                      self.tokens.append(("KEYWORD", "{"))
                      if self.cur_char is not None and self.cur_char.isspace():
                        self.advance()
                      elif self.play_token():
                         self.end_bracket()
                    else:
                        self.errors.append("Error: Invalid token, missing { in times token.")
                        self.tokens.append(("KEYWORD", "{"))
                        if self.cur_char is not None and self.cur_char.isspace():
                          self.advance()
                        elif self.play_token(): 
                          self.end_bracket()

      else:
        return
    return

        
  def get_tokens(self):
    return self.tokens
  def get_errors(self):
    return self.errors



# Pitch Parser

See Lexer information here: <br>
https://github.com/gruiiiw/PLT-Music-Compiler

## CFG

S → EXPRESSON S | PLAY S | TIMES S | $ <br>
ASSIGNMENT → =NOTE | ε <br>
TIMES → NUMBER times {PLAY} <br>
NOTE → <capital_letter A-G> <num> LENGTH <br>
LENGTH → w | h | q | e | s <br>
VAR →  <capital_letter A-Z> LET <br>
LET → <lowercase_letter a-z> | <lowercase_letter a-z> LET <br>
PLAY → play (EXPRESSION2) S <br>
EXPRESSION → NOTE |  ASSIGNMENT <br>
EXPRESSION2 → NOTE EXPRESSION2 | VAR EXPRESSION2 | ε <br>

#### Terminal definition: ?
- VAR/IDENTIFIER: Represents variable names or identifiers.
- NOTE: Represents musical notes.
- NUM: Represents numeric values (number or times to play a phrase).
- play: Keyword for playing notes.
- times: Keyword for repeating actions.
- =: Assignment operator.
- {: Opening brace (delimiter, used for times{})
- }: Closing brace. 
- (: Opening parenthesis. (delimiter, used for play())
- ): Closing parenthesis.
- $: End of input marker.

#### Non Terminal Definition ?


## Run Instructions 
Make sure you have python3 installed.   <br>
You can install it from here https://www.python.org/downloads/  <br>
Now make sure to set the permission for the .sh files by running the following command. <br>

``` chmod +x run_full_compiler.sh run_full_tests.sh run_lexer_tests.sh run_parser_tests.sh```
<br>

The provided test cases (see below) are also built into our code. You can run these test cases using the following commands: <br> 

To run the examples in the Lexer, and then have the Lexer tokens run in the Parser, run:
``` ./run_full_tests.sh ``` 

To run the Lexer tests:
``` ./run_lexer_tests.sh ``` 

To run the Parser tests:
``` ./run_parser_tests.sh ``` 

To run the scanner to provide your own inputs:
``` ./run_full_compiler.sh ``` 

## Sample inputs 

### Input 1
```markdown
  ('KEYWORD', 'play'),
  ('DELIMITER', '('),
  ('NOTE', 'A4w'),
  ('NOTE', 'A4w'),
  ('DELIMITER', ')')
```

#### Expected AST
```plaintext
─ S 
   └─── PLAY
        ├─── play  (KEYWORD)
        └─── EXPRESSION2
            ├─── A4w  (NOTE)
            └─── EXPRESSION2
                ├─── A4w  (NOTE)
                └─── EXPRESSION2
                    └─── epsilon
```

### Input 2
```markdown
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
```



#### Expected AST
```plaintext
─ S
    ├─── EXPRESSION
    │   ├─── Thats  (IDENTIFIER)
    │   └─── ASSIGNMENT
    │       ├─── =  (OPERATOR)
    │       └─── G4w  (NOTE)
    ├─── EXPRESSION
    │   ├─── That  (IDENTIFIER)
    │   └─── ASSIGNMENT
    │       ├─── =  (OPERATOR)
    │       └─── G4h  (NOTE)
    ├─── EXPRESSION
    │   ├─── Me  (IDENTIFIER)
    │   └─── ASSIGNMENT
    │       ├─── =  (OPERATOR)
    │       └─── B4h  (NOTE)
    ├─── EXPRESSION
    │   ├─── Espresso  (IDENTIFIER)
    │   └─── ASSIGNMENT
    │       ├─── =  (OPERATOR)
    │       └─── C4q  (NOTE)
    └─── EXPRESSION
        └─── B4q  (NOTE)
```


### Input 3
```markdown
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
    ('KEYWORD', 'times'),
    ('Delimitter', '{'),
    ('KEYWORD', 'play'),
    ('DELIMITER', '('),
    ('IDENTIFIER', 'Birthday'),
    ('IDENTIFIER', 'To'),
    ('IDENTIFIER', 'You'),
    ('DELIMITER', ')'),
    ('DELIMITER', '}')
```

#### Expected AST
```plaintext
─ S
    ├─── EXPRESSION
    │   ├─── Happy  (IDENTIFIER)
    │   └─── ASSIGNMENT
    │       ├─── =  (OPERATOR)
    │       └─── A4w  (NOTE)
    ├─── EXPRESSION
    │   ├─── Birthday  (IDENTIFIER)
    │   └─── ASSIGNMENT
    │       ├─── =  (OPERATOR)
    │       └─── A4w  (NOTE)
    ├─── EXPRESSION
    │   └─── A4h  (NOTE)
    ├─── EXPRESSION
    │   └─── B4w  (NOTE)
    ├─── EXPRESSION
    │   └─── A4w  (NOTE)
    ├─── EXPRESSION
    │   └─── D4h  (NOTE)
    ├─── EXPRESSION
    │   ├─── To  (IDENTIFIER)
    │   └─── ASSIGNMENT
    │       ├─── =  (OPERATOR)
    │       └─── A4w  (NOTE)
    ├─── EXPRESSION
    │   └─── A4h  (NOTE)
    ├─── EXPRESSION
    │   └─── B4w  (NOTE)
    ├─── EXPRESSION
    │   └─── A4w  (NOTE)
    ├─── EXPRESSION
    │   ├─── You  (IDENTIFIER)
    │   └─── ASSIGNMENT
    │       ├─── =  (OPERATOR)
    │       └─── D4w  (NOTE)
    └─── TIMES
        ├─── 5  (INTEGER)
        ├─── times  (KEYWORD)
        └─── PLAY
            ├─── play  (KEYWORD)
            └─── EXPRESSION2
                ├─── Birthday  (IDENTIFIER)
                └─── EXPRESSION2
                    ├─── To  (IDENTIFIER)
                    └─── EXPRESSION2
                        ├─── You  (IDENTIFIER)
                        └─── EXPRESSION2
                            └─── epsilon
```

### Input 4
```markdown
  ('IDENTIFIER', 'Thats'),
  ('OPERATOR', '='),
  ('NOTE', 'A4h'),
  ('NOTE', 'G4w'),
  ('INTEGER', '5'),

```

#### Expected AST with errors (Parsing fail, extra 5 at the end)
```plaintext
─ S  X -> Partial match for S
    ├─── EXPRESSION
    │   ├─── Thats  (IDENTIFIER)
    │   └─── ASSIGNMENT
    │       ├─── =  (OPERATOR)
    │       └─── A4h  (NOTE)
    ├─── EXPRESSION
    │   └─── G4w  (NOTE)
    └─── EXPRESSION  X -> Partial match for EXPRESSION
        └─── NOTE  X -> Expected NOTE, found INTEGER(5)
```


### Input 5
```markdown
    ('OPERATOR', '='),
    ('NOTE', 'G4w'),
    ('INTEGER', '5'),  
    ('KEYWORD', 'times'),
    ('{', '{'),
    ('KEYWORD', 'play'),
    ('DELIMITER', '('),
    ('IDENTIFIER', 'Song'),
    ('DELIMITER', ')'),
    ('DELIMETER', '}'),
```

#### Expected AST with errors, no identifier, but there is an operator = . 
```plaintext
─ S  X -> Partial match for S
    └─── EXPRESSION  X -> Partial match for EXPRESSION
        └─── NOTE  X -> Expected NOTE, found OPERATOR(=)
```

## Teammates 
Benjamin Cyna bc3096 <br>
Grace Dong grd2120 <br>

## Link to demo
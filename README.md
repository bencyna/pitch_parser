# Pitch Parser


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


### Terminal definition:
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
  ('KEYWORD', 'play'),
  ('DELIMITER', '('),
  ('NOTE', 'A4w'),
  ('NOTE', 'A4w'),
  ('DELIMITER', ')')

#### Expected AST ?
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

### Input 2

#### Expected AST

### Input 3

#### Expected AST

### Input 4

#### Expected AST with errors

### Input 5

#### Expected AST with errors 


## Teammates 
Benjamin Cyna bc3096 <br>
Grace Dong grd2120 <br>

## Link to demo
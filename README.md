# Pitch Parser


## CFG

S → EXPRESSON S | PLAY S | TIMES S | $ <br>
POSTVAR → =NOTE | ε <br>
TIMES → NUMBER times {PLAY} <br>
NOTE → <capital_letter A-G> <num> LENGTH <br>
LENGTH → w | h | q | e | s <br>
VAR →  <capital_letter A-Z> LET POSTVAR <br>
LET → <lowercase_letter a-z> | <lowercase_letter a-z> LET <br>
PLAY → play (Expression) S <br>
EXPRESSiON → NOTE | VAR <br>

## Run Instructions 
Make sure you have python3 installed.   <br>
You can install it from here https://www.python.org/downloads/  <br>

### Option 1, Our own test cases
Now make sure to set the permission for the .sh files. <br>
You use these two commands. Run them one after 
the other <br>
``` chmod +x run_full_compiler.sh ```
<br> 

``` chmod +x run_full_tests.sh run_lexer_tests.sh run_parser_tests.sh```
<br>

The provided test cases (see below) are also built into our code. You can run these test cases using the following command. <br> 

To run the lexer, and then have the lexer tokens run in the parser run:
``` ./run_full_tests.sh ``` 

To run the lexer tests:
``` ./run_lexer_tests.sh ``` 

To run the Parser tests:
``` ./run_parser_tests.sh ``` 



## Sample inputs 

### Input 1

#### Expected AST

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
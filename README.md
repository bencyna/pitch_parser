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
Now make sure to set the permission for the .sh files. You use these two commands. Run them one after 
the other <br>
``` chmod +x run_scanner.sh ```
<br> 

``` chmod +x run_tests.sh ```
<br>
The provided test cases (see below) are also built into our code. You can run these test cases using the following command. <br> 

``` ./run_tests.sh ``` 


## Sample inputs 
Provide 5 sample input programs with their expected AST for testing. Write the
input programs such that you can
■ Demonstrate different syntactic structures, such as expressions, control
statements, and nesting.
■ Error handling capabilities of your parser.

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
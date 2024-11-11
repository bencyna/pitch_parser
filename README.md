# Pitch Parser


## CFG

S → EXPRESSON S | PLAY | TIMES | $ <br>
NOTE → <capital_letter A-H> <num> LENGTH <br>
LENGTH → w | h | q | e | s <br>
VAR →  <capital_letter A-Z> LET POSTVAR <br>
LET → <lowercase_letter a-z> | <lowercase_letter a-z> LET <br>
POSTVAR → ε | =NOTE <br>
TIMES → NUMBER times {PLAY} S <br>
PLAY → play (Expression) S <br>
EXPRESSiON → NOTE | VAR <br>

## Run Instructions 
Make sure you have python3 installed.   <br>
You can install it from here https://www.python.org/downloads/  <br>


## Sample inputs 
Provide 5 sample input programs with their expected AST for testing. Write the
input programs such that you can
■ Demonstrate different syntactic structures, such as expressions, control
statements, and nesting.
■ Error handling capabilities of your parser.

### Input 1

### Input 2

### Input 3

### Input 4

### Input 5

## Teammates 
Benjamin Cyna bc3096 <br>
Grace Dong grd2120 <br>

## Link to demo
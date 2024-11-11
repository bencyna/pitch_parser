# Pitch Parser


## CFG

<<<<<<< HEAD
S → EXPRESSON S | PLAY | TIMES | $
NOTE → <capital_letter A-G> <num> LENGTH  
LENGTH → w | h | q | e | s 
VAR →  <capital_letter A-Z> LET POSTVAR
LET → <lowercase_letter a-z> | <lowercase_letter a-z> LET
POSTVAR → ε | =NOTE
TIMES → NUMBER times {PLAY} S 
PLAY → play (EXPRESSION) S 
EXPRESSiON → NOTE | VAR
=======
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
>>>>>>> 566c938356f106df56e7c81e877cb0242c5c1ac4


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
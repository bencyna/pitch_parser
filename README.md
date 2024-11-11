# Pitch Parser


## CFG

S → EXPRESSON S | PLAY | TIMES | $
NOTE → <capital_letter A-G> <num> LENGTH  
LENGTH → w | h | q | e | s 
VAR →  <capital_letter A-Z> LET POSTVAR
LET → <lowercase_letter a-z> | <lowercase_letter a-z> LET
POSTVAR → ε | =NOTE
TIMES → NUMBER times {PLAY} S 
PLAY → play (EXPRESSION) S 
EXPRESSiON → NOTE | VAR


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
# Pitch Parser


## CFG

S → EXPRESSON S | PLAY | TIMES | $
NOTE → <capital_letter A-H> <num> LENGTH  
LENGTH → w | h | q | e | s 
VAR →  <capital_letter A-Z> LET POSTVAR
LET → <lowercase_letter a-z> | <lowercase_letter a-z> LET
POSTVAR → ε | =NOTE
TIMES → NUMBER times {PLAY} S 
PLAY → play (Expression) S 
EXPRESSiON → NOTE | VAR

## Usage 

## Sample inputs 

## Run instructions 

## Teammates 
Benjamin Cyna bc3096 <br>
Grace Dong grd2120 <br>

## Link to demo
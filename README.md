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

## Usage 

## Sample inputs 

## Run instructions 

## Teammates 
Benjamin Cyna bc3096 <br>
Grace Dong grd2120 <br>

## Link to demo
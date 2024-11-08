# Pitch Parser


## CFG

S -> EXPRESSION S | PLAY | TIMES | $
EXPRESSION -> NOTE | IDENTIFIER 
NOTE -> [A-G][0-9][w|h|q|e|s]
IDENTIFIER -> [A-Z] LETTER POSTVAR
LETTER -> [a-z] | [a-z] LETTER
POSTVAR -> ε | = NOTE
TIMES -> int times (PLAY) S
PLAY -> play(EXPRESSION) S

## Usage 

## Sample inputs 

## Run instructions 

## Teammates 
Benjamin Cyna bc3096 <br>
Grace Dong grd2120 <br>

## Link to demo
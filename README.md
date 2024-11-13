# Pitch Parser

See Lexer information here: <br>
https://github.com/gruiiiw/PLT-Music-Compiler

## CFG

S → EXPRESSON S | PLAY S | TIMES S | $ <br>
ASSIGNMENT → =NOTE | ε <br>
TIMES → <integer> times {PLAY} <br>
NOTE → <capital_letter A-G> <1-8> LENGTH <br>
LENGTH → w | h | q | e | s <br>
VAR →  <capital_letter A-Z> LET <br>
LET → <lowercase_letter a-z> | <lowercase_letter a-z> LET <br>
PLAY → play (EXPRESSION2) S <br>
EXPRESSION → NOTE |  ASSIGNMENT <br>
EXPRESSION2 → NOTE EXPRESSION2 | VAR EXPRESSION2 | ε <br>

### Terminal definition:
1. `=`: Assignment (used to assign note to variable)
2. `ε`: Epsilon (empty production)
3. `integer`: # - for number of times something loops, ie 5 times { Id }
4. `times`: Keyword for repeating a loop
5. `{`: Opening brace (used for the times keyword)
6. `}`: Closing brace (used for the times keyword)
7. `<capital_letter A-G>`: Capital letters A to G, used in musical notes
8. `<1-8>`: octave location of the note
9. `w`, `h`, `q`, `e`, `s`: Length of the note (whole, half, quarter, eight, sixteenth)
10. `<capital_letter A-Z>`: Capital letters A to Z 
11. `<lowercase_letter a-z>`: Lowercase letters a to z
12. `play`: Keyword for playing notes, ie play (Note Note )
13. `(`: Opening parenthesis (used for the play keyword)
14. `)`: Closing parenthesis (used for the play keyword)
15. `$`: End of input marker


### Non Terminal Definition 
1. `S` - The start of the program. Can be `EXPRESSION` followed by `S` (start of program), or `PLAY` followed by `S`, or `TIMES` followed by `S`, or the end symbol `$`.
2. `ASSIGNMENT` - assigns a note to a variable. Can be an `=` followed by a `NOTE`, or it can be `ε` (an empty production). (so there would be no assignment in case of `ε`)
3. `TIMES` - Represents a loop. It is a `<integer>` followed by keyword `times`, followed by `{`, followed by `PLAY`, followed by `}`. 
4. `NOTE` - Represents a musical note. It is of a capital letter A-G, followed by a # which is the octave, followed by a `LENGTH` (of the note).
5. `LENGTH` - Represents the length of a note. It can be `w` (whole), `h` (half), `q` (quarter), `e` (eighth), or `s` (sixteenth).
6. `VAR` - Represents a variable. Its made of of a capital letter A-Z, followed by `LET`.
7. `LET` - Represents the letters following the initial capital letter in a variable name. It can be a lowercase letter a-z, or a lowercase letter a-z followed by `LET`. (so basically any # of lower case letters)
8. `PLAY` - Represents the play command. It is the keyword `play` followed by `(`, followed by `EXPRESSION2`, followed by `)`, followed by `S`. 
9. `EXPRESSION` - Represents an expression. It can be a `NOTE`, or an `ASSIGNMENT`.
10. `EXPRESSION2` - Represents a sequence of expressions. It can be a `NOTE` followed by `EXPRESSION2`, or a `VAR` followed by `EXPRESSION2`, or `ε` (an empty production). No assignments can be made in expression2, so in play and times, no assignments can be made within their brackets.



## Run Instructions 
Make sure you have python3 installed.   <br>
You can install it from here https://www.python.org/downloads/  <br>
Now make sure to set the permission for the .sh files by running the following command. <br>

``` chmod +x run_full_compiler.sh run_full_tests.sh run_lexer_tests.sh run_parser_tests.sh```
<br>

The provided test cases (see below) are also built into our code. You can run these test cases using the following commands: <br> 

To run the examples in the Lexer, and then have the Lexer tokens run in the Parser, run: <br>
``` ./run_full_tests.sh ```  

To run the Lexer tests:<br>
``` ./run_lexer_tests.sh ``` 

To run the Parser tests:<br>
``` ./run_parser_tests.sh ``` 

To run the scanner to provide your own inputs:<br>
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
https://youtu.be/nnuGnQhr35c

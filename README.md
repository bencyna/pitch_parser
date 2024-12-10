# Pitch Parser

## Summary 
This is the final iteration of the Pitch Parser, which takes in our made up programming language and generates the bit encodings defined [here](https://www.geognomo.com/geognomo/geotono/). Our code goes through a lexical analysis phase where we tokenize the code. We pass the tokens into our Parser which uses a context free grammar (CFG) we defined to generate an Abstract Syntax Tree (AST) using recursive descent parsing. The AST is fed into the code generation stage which does data analysis while looping through the AST to identify outputs of the program. Optionally, this is run through a pitch parser to generate the sounds defined in the program. Further details explored throughout this README. 

- [Lexical Grammar](#lexical-analysis)
- [Context Free Grammaer](#context-free-grammar)
- [Code Generation](#code-generation)
- [Run Instructions](#run-instructions)
- [Sample Inputs](#sample-inputs)
- [Teammates](#teammates)
- [Link to Demo](#link-to-demo)

## Lexical Analysis
Our program ignores whitespace. 

KEYWORD= ["times", "play"] <br>

Rules: <br>
"times" has to follow an integer. <br> 
"times" has to be followed by an open bracket "{" <br> 
"play" has to be followed by an open parenthesis "(" <br>


<br>
NUMBERS = [0-9] <br>
Rules: <br>
A number can appear before times as first token. <br>
A number can be part of a note. It must follow a letter (note key) [A-G] and precede a length key (w|h|q|e|s) <br>

<br>
IDENTIFIER = ['A-Z']['a-z']* <br>
    Examples: Happy, Birthday, Variable <br>
Rules: <br>
A variable can be defined as a single captial letter [A-Z] followed by any length string of [a-z] chars. <br>
An identifier must precede an '=' sign <br>


<br>
OPERATORS = ["="] <br>
Rules: <br>
An equals sign must follow an identifier and be followed by a NOTE token. 
<br>
<br>

NOTE = [("A-G")(1-8)("w|h|q|e|s")] <br>
Examples: A4w, B3h, G4w, C4w, D4w. <br>
Rules:
A note can be defined after an '=' char <br>
A note can be defined after an open parenthesis '(' <br>
<br>


DELIMITER = ["(", ")", '{', '}'] <br>
Rules: <br>
'(' follows "play" keyword and must have a enclosing '). <br>
'{' follows "times" keyword and must have enclosing '}' <br>


Example Program: <br>
    Variable_name= A4w C2h B43  <br>
    2times {play ( Variable_name )}  <br>

<br>

## Context Free Grammar

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

## Code Generation
To generate the code, the CodeGeneration class takes in the AST generated during the parsing stage. It iterates through the tree, assigning variable values and if matching, produces the output of the sound when played. We conver the notes into their bit form following the insights from [this link](https://www.geognomo.com/geognomo/geotono/). 

### Output
This is the mapping from the note details to bit encodings <br>
pitch_map = {'C': '000', 'D': '001', 'E': '010', 'F': '011', 'G': '100', 'A': '101', 'B': '110'} <br>
duration_map = {'w': '000', 'h': '001', 'q': '010', 'e': '011', 's': '100'} <br>
octave_map = {'1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'} <br> <br>

#### Example
play(A4w) should output 101100000. 

### Error Detection 
Our Code Generation phase also does data analysis which confirms if a variable is alive when called. For example on this output we would get an error. 

``` 
Hello = A4w
play(Holo)
 ```
 Error: variable Holo not initialised. 


## Run Instructions 
Make sure you have python3 installed.   <br>
You can install it from here https://www.python.org/downloads/  <br>
Now make sure to set the permission for the .sh files by running the following command. <br>

``` chmod +x run_full_compiler.sh run_full_tests.sh run_lexer_tests.sh run_parser_tests.sh run_sound_integration.sh```
<br>

The provided test cases (see below) are also built into our code. You can run these test cases using the following commands: <br> 

To run tests through each code generation, run: <br>
``` ./run_full_tests.sh ```  

To run the Lexer tests:<br>
``` ./run_lexer_tests.sh ``` 

To run the Parser tests:<br>
``` ./run_parser_tests.sh ``` 

To run the full program from your own code to bit encoded outputs: <br>
``` ./run_full_compiler.sh ``` 

To run the program from your own code to sound outputs: <br>
``` ./run_sound_integration.sh ``` 

## Sample Inputs 

Example 1 = "play(A4w F5w F5w C4q D4q E4q F4q G4q A4q B4q)" <br>
Expected Output: <br>
``` 
101100000
011101000
011101000
000100010
001100010
010100010
011100010
100100010
101100010
110100000
110100001
```
<br>


Example 2 = "Thats= G4w That= G4h Me= B4h Espresso= C4q 5times{play(Thats That Me  <br>Espresso A4w B3h G4w)}"
Expected Output: <br> 
``` 
100100000
100100001
110100001
000100010
101100000
110011001
100100000
100100000
100100001
110100001
000100010
101100000
110011001
100100000
100100000
100100001
110100001
000100010
101100000
110011001
100100000
100100000
100100001
110100001
000100010
101100000
110011001
100100000
100100000
100100001
110100001
000100010
101100000
110011001
100100000 
```
<br>
<br>


Example 3 = "Happy = A4w Birthday= A4w To = A4w You = D4w 5times {play(Birthday To You)}" <br>
Expected Output: <br>
```
101100000
101100000
001100000
101100000
101100000
001100000
101100000
101100000
001100000
101100000
101100000
001100000
101100000
101100000
001100000
```
<br>
<br>

Example 4 = "White= G4w Lips= A4w Pale = A4w Face = D4w Breathin= D4w In= D4w The= C4q Snowflakes= C4q 3times {play(White Lips Pale Face Breathin In The Snowflakes)}"<br>
```
100100000
101100000
101100000
001100000
001100000
001100000
000100010
000100010
100100000
101100000
101100000
001100000
001100000
001100000
000100010
000100010
100100000
101100000
101100000
001100000
001100000
001100000
000100010
000100010

```
<br>
<br>

Example 5 = "Ben = A4w play(Jack Ben A4w)" <br>
Expected Output: <br>
```
Error: variable Jack not initialised
````
<br>
<br>


## Teammates 
Benjamin Cyna bc3096 <br>
Grace Dong grd2120 <br>

## Link to demo
https://youtu.be/BEa9qIItaZw

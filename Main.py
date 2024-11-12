import sys
from Lexer import LexerDfa
from Parser import Parser

def runFullProgram():
   # Run scanner and then run code
    data = sys.stdin.readlines()
    data_string = "".join(data)
    runParser = LexerDfa(data_string) 
    runParser.run()
    tokens = runParser.get_tokens()
    errors = runParser.get_errors()

    for token in tokens:
        print(token)

    if errors:
        print("Errors encountered in lexical analysis phase. Parser not run")
    else:
        parser = Parser(tokens)
        parser.print_ast()

def runTestsForLexer():
    print("\n Test 1 \n\n")
    # This test shows multiple Identifiers being assigned to notes, and then played 5times in a play token
    # No errors in this first test case
    # Test shows play accepts both variables and notes
    lexer_Dfa1 = LexerDfa("""Thats= G4w That= G4h Me= B4h Espresso= C4q B4q B4w A4q
                            5times{play(Thats That Me Espresso A4w B3h G4w)}""") 
    lexer_Dfa1.run()
    tokens_1 = lexer_Dfa1.get_tokens()
    errors_1 = lexer_Dfa1.get_errors()

    for token in tokens_1:
        print(token)

    if errors_1:
        print("Errors encountered:")
        for error in errors_1:
            print(error)

    # Output: 
    '''
    ('IDENTIFIER', 'Thats')
    ('OPERATOR', '=')
    ('NOTE', 'G4w')
    ('IDENTIFIER', 'That')
    ('OPERATOR', '=')
    ('NOTE', 'G4h')
    ('IDENTIFIER', 'Me')
    ('OPERATOR', '=')
    ('NOTE', 'B4h')
    ('IDENTIFIER', 'Espresso')
    ('OPERATOR', '=')
    ('NOTE', 'C4q')
    ('NOTE', 'B4q')
    ('NOTE', 'B4w')
    ('NOTE', 'A4q')
    ('INTEGER', '5')
    ('Keyword', 'times')
    ('Keyword', '{')
    ('Keyword', 'play')
    ('Delimiter', '(')
    ('IDENTIFIER', 'Thats')
    ('IDENTIFIER', 'That')
    ('IDENTIFIER', 'Me')
    ('IDENTIFIER', 'Espresso')
    ('NOTE', 'A4w')
    ('NOTE', 'B3h')
    ('NOTE', 'G4w')
    ('Delimiter', ')')
    ('Keyword', '}')
    '''

    print("\n\n Test 2 \n\n")
    # Handles assigning multiple Identifiers, in different octaves and durations
    # Handles missing y in play token
    # Handes missing note duration, defaults to whole note (G4)
    # Handles different spacing and new lines
    # Handles missing { in times token
    lexer_DFA2 = LexerDfa("""Is = A4w B3h It = B3h That= B3h G7h 
                              G4 
                              Sweet= A4w B3h C4w 5timespla(Is It That Sweet)}""")
    lexer_DFA2.run()
    tokens_2 = lexer_DFA2.get_tokens()
    errors_2 = lexer_DFA2.get_errors()

    for token in tokens_2:
        print(token)

    if errors_2:
        print("Errors encountered:")
        for error in errors_2:
            print(error)

    # Output:
    '''
    ('IDENTIFIER', 'Is')
    ('OPERATOR', '=')
    ('NOTE', 'A4w')
    ('NOTE', 'B3h')
    ('IDENTIFIER', 'It')
    ('OPERATOR', '=')
    ('NOTE', 'B3h')
    ('IDENTIFIER', 'That')
    ('OPERATOR', '=')
    ('NOTE', 'B3h')
    ('NOTE', 'G7h')
    ('NOTE', 'G4w')
    ('IDENTIFIER', 'Sweet')
    ('OPERATOR', '=')
    ('NOTE', 'A4w')
    ('NOTE', 'B3h')
    ('NOTE', 'C4w')
    ('INTEGER', '5')
    ('Keyword', 'times')
    ('Keyword', '{')
    ('Keyword', 'play')
    ('Delimiter', '(')
    ('IDENTIFIER', 'Is')
    ('IDENTIFIER', 'It')
    ('IDENTIFIER', 'That')
    ('IDENTIFIER', 'Sweet')
    ('Delimiter', ')')
    ('Keyword', '}')
    Errors encountered:
    Error: Invalid note token, missing duration w, h, q, e, s, default as w.
    Error: Invalid token, missing { in times token.
    Error: Missing ( in play token.
    '''

    print("\n\n Test 3 \n\n")
    # Tests 5 notes to a single Identifier
    # Handles octave number error, 9 defaults to octave 4
    # Handles variables in [H-Z] then [A-G] then [H-Z]
    lexer_DFA3 = LexerDfa("Happy= A4w Birthday= A4w A9h B4w A4w D4h To = A4w A4h B4w A4w You = D4w 5times {play(Birthday To You)}")
    lexer_DFA3.run()
    tokens_3 = lexer_DFA3.get_tokens()
    errors_3 = lexer_DFA3.get_errors()

    for token in tokens_3:
        print(token)
    
    if errors_3:
        print("Errors encountered:")
        for error in errors_3:
            print(error)

    # Output:
    '''
    ('IDENTIFIER', 'Happy')
    ('OPERATOR', '=')
    ('NOTE', 'A4w')
    ('IDENTIFIER', 'Birthday')
    ('OPERATOR', '=')
    ('NOTE', 'A4w')
    ('NOTE', 'A4h')
    ('NOTE', 'B4w')
    ('NOTE', 'A4w')
    ('NOTE', 'D4h')
    ('IDENTIFIER', 'To')
    ('OPERATOR', '=')
    ('NOTE', 'A4w')
    ('NOTE', 'A4h')
    ('NOTE', 'B4w')
    ('NOTE', 'A4w')
    ('IDENTIFIER', 'You')
    ('OPERATOR', '=')
    ('NOTE', 'D4w')
    ('INTEGER', '5')
    ('Keyword', 'times')
    ('Keyword', '{')
    ('Keyword', 'play')
    ('Delimiter', '(')
    ('IDENTIFIER', 'Birthday')
    ('IDENTIFIER', 'To')
    ('IDENTIFIER', 'You')
    ('Delimiter', ')')
    ('Keyword', '}')
    Errors encountered:
    Error: Invalid octave number 9, default as octave 4.
    '''

    print("\n\n Test 4 \n\n")
    # Tests playing before and after the Identifier assignment
    # Testing multiple lines of notes
    # Handles missing ( in play token
    lexer_DFA4 = LexerDfa("play(A4w B3h G4w C4w D4w) Someone= D3h To= A4w B3h G4w C4w D4w Love= F3q playSomeone To Love)")
    lexer_DFA4.run()
    tokens_4 = lexer_DFA4.get_tokens()
    errors_4 = lexer_DFA4.get_errors()

    for token in tokens_4:
        print(token)

    if errors_4:
        print("Errors encountered:")
        for error in errors_4:
            print(error)

    # Output:
    '''
    ('Keyword', 'play')
    ('Delimiter', '(')
    ('NOTE', 'A4w')
    ('NOTE', 'B3h')
    ('NOTE', 'G4w')
    ('NOTE', 'C4w')
    ('NOTE', 'D4w')
    ('Delimiter', ')')
    ('IDENTIFIER', 'Someone')
    ('OPERATOR', '=')
    ('NOTE', 'D3h')
    ('IDENTIFIER', 'To')
    ('OPERATOR', '=')
    ('NOTE', 'A4w')
    ('NOTE', 'B3h')
    ('NOTE', 'G4w')
    ('NOTE', 'C4w')
    ('NOTE', 'D4w')
    ('IDENTIFIER', 'Love')
    ('OPERATOR', '=')
    ('NOTE', 'F3q')
    ('Keyword', 'play')
    ('IDENTIFIER', 'Someone')
    ('IDENTIFIER', 'To')
    ('IDENTIFIER', 'Love')
    ('Delimiter', ')')
    Errors encountered:
    Error: Missing ( in play token.
    '''

    print("\n\n Test 5 \n\n")
    # Tests multiple lines of input
    # Tests missing s in times token
    # Missing { in times token
    lexer_DFA5 = LexerDfa("""White= D4h Lips=D4h Pale= A4w Face= B4s
                            Breathin= B4s C3q In= C3q The= D4q Snowflakes= C4q D4q
                            Burnt= E4s F3s Lungs= F3s Sour= G3s Taste= G3s
                            2time play(White Lips Pale Face
                            Breathin In The Snowflakes
                            Burnt Lungs Sour Taste)""")
    lexer_DFA5.run()
    tokens_5 = lexer_DFA5.get_tokens()
    errors_5 = lexer_DFA5.get_errors()

    for token in tokens_5:
        print(token)

    if errors_5:
        print("Errors encountered:")
        for error in errors_5:
            print(error)

    # Output:
    '''
    ('IDENTIFIER', 'White')
    ('OPERATOR', '=')
    ('NOTE', 'D4h')
    ('IDENTIFIER', 'Lips')
    ('OPERATOR', '=')
    ('NOTE', 'D4h')
    ('IDENTIFIER', 'Pale')
    ('OPERATOR', '=')
    ('NOTE', 'A4w')
    ('IDENTIFIER', 'Face')
    ('OPERATOR', '=')
    ('NOTE', 'B4s')
    ('IDENTIFIER', 'Breathin')
    ('OPERATOR', '=')
    ('NOTE', 'B4s')
    ('NOTE', 'C3q')
    ('IDENTIFIER', 'In')
    ('OPERATOR', '=')
    ('NOTE', 'C3q')
    ('IDENTIFIER', 'The')
    ('OPERATOR', '=')
    ('NOTE', 'D4q')
    ('IDENTIFIER', 'Snowflakes')
    ('OPERATOR', '=')
    ('NOTE', 'C4q')
    ('NOTE', 'D4q')
    ('IDENTIFIER', 'Burnt')
    ('OPERATOR', '=')
    ('NOTE', 'E4s')
    ('NOTE', 'F3s')
    ('IDENTIFIER', 'Lungs')
    ('OPERATOR', '=')
    ('NOTE', 'F3s')
    ('IDENTIFIER', 'Sour')
    ('OPERATOR', '=')
    ('NOTE', 'G3s')
    ('IDENTIFIER', 'Taste')
    ('OPERATOR', '=')
    ('NOTE', 'G3s')
    ('INTEGER', '2')
    ('Keyword', 'times')
    ('Keyword', '{')
    ('Keyword', 'play')
    ('Delimiter', '(')
    ('IDENTIFIER', 'White')
    ('IDENTIFIER', 'Lips')
    ('IDENTIFIER', 'Pale')
    ('IDENTIFIER', 'Face')
    ('IDENTIFIER', 'Breathin')
    ('IDENTIFIER', 'In')
    ('IDENTIFIER', 'The')
    ('IDENTIFIER', 'Snowflakes')
    ('IDENTIFIER', 'Burnt')
    ('IDENTIFIER', 'Lungs')
    ('IDENTIFIER', 'Sour')
    ('IDENTIFIER', 'Taste')
    ('Delimiter', ')')
    Errors encountered:
    Error: Invalid token, missing s in times token.
    Error: Invalid token, missing { in times token.
    Error: Missing } in times token.
    '''

def runTestsForParser():
    example1 =  [
        ('Keyword', 'play'),
        ('Delimiter', '('),
        ('NOTE', 'A4w'),
        ('NOTE', 'A4w'),
        ('Delimiter', ')')
    ]
        
    example2 =  [
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
    ]

    example3 =  [
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
        ('Keyword', 'times'),
        ('Delimitter', '{'),
        ('Keyword', 'play'),
        ('Delimiter', '('),
        ('IDENTIFIER', 'Birthday'),
        ('IDENTIFIER', 'To'),
        ('IDENTIFIER', 'You'),
        ('Delimiter', ')'),
        ('Delimiter', '}')
    ]

    # Parsing fail, extra 5 at the end
    example4 = [
        ('IDENTIFIER', 'Thats'),
        ('OPERATOR', '='),
        ('NOTE', 'A4h'),
        ('NOTE', 'G4w'),
        ('INTEGER', '5'),
    ]
    # Parsing fail, no identifier, but there is an operator = 
    example5 = [
        # ('IDENTIFIER', 'Thats'),
        ('OPERATOR', '='),
        ('NOTE', 'G4w'),
        ('INTEGER', '5'),  
        ('Keyword', 'times'),
        ('{', '{'),
        ('Keyword', 'play'),
        ('Delimiter', '('),
        ('IDENTIFIER', 'Song'),
        ('Delimiter', ')'),
        ('{', '}'),
    ]

    
    # examples = [example1, example2, example3, example4, example5]
    examples = [example1]

    for i, tokens in enumerate(examples):
        print(f"\nExample {i+1}:")
        parser = Parser(tokens)
        if parser.head:
            parser.print_ast()
            if any(node.failed for node in parser.head.children):
                print("\nParsing completed with errors (see X -> markers above)\n")
            else:
                print("Parsing succeeded!")
        else:
            print("Parsing failed.")
        
def runTestsFullprogram():
    Example1 = "play(A4w A4w)"
    Example2 = "Thats= G4w That= G4h Me= B4h Espresso= C4q B4q B4w A4q 5times{play(Thats That Me Espresso A4w B3h G4w)}"
    Example3 = "Happy = A4w Birthday= A4w To = A4w You = D4w 5times {play(Birthday To You)}"
    tests = [Example1, Example2, Example3]
    for test in tests:
        print("Running Lexer...")
        run_parser = LexerDfa(test) 
        run_parser.run()
        tokens = run_parser.get_tokens()
        errors = run_parser.get_errors()
        if errors:
            print("Errors encountered in lexical analysis phase. Parser not run")
        else:
            print("Successfully ran lexer, running parser...")
            parser = Parser(tokens)
            parser.print_ast()
  
if len(sys.argv) != 2:
    print("Usage: python3 Main.py <int>\n 0: run tests for lexer. \n 1: run tests for Parser.\n 2 : input your own code in our language and we will run the paerser then lexer on your code.\n 3: Test cases for parser -> scanner" )
    sys.exit(1)
    
type = sys.argv[1]
if type == "2":
    print("Please enter your code below. Press Ctrl +D to finish.")
    runFullProgram()
          
    
elif type == "0":
    print("Running tests for lexer...")
    runTestsForLexer()

    
elif type == "1":
    print("Running tests for parser...")
    runTestsForParser()
    
elif type == "3":
    print("Running tests for parser then scanner...")
    # Test cases for parser -> scanner
    runTestsFullprogram()

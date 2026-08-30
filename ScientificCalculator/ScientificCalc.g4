grammar ScientificCalc;

prog
    : stat+ EOF
    ;

stat
    : expr NEWLINE                                                                                      # printExpr
    | ID '(' ID ')' '=' expr NEWLINE                                                                    # funcDef
    | ID '=' expr NEWLINE                                                                                # assign
    | 'clear' NEWLINE                                                                                    # clear
    | 'vars' NEWLINE                                                                                     # showVars
    | 'plot' '(' funcs+=expr (';' funcs+=expr)* ',' xmin=expr ',' xmax=expr (',' ymin=expr ',' ymax=expr)? ')' NEWLINE   # plotExpr
    | NEWLINE                                                                                             # blank
    ;

expr
    : <assoc=right> expr '^' expr        # power
    | expr op=('*'|'/') expr             # mulDiv
    | expr op=('+'|'-') expr             # addSub
    | function2 '(' expr ',' expr ')'    # functionCall2
    | function '(' expr ')'              # functionCall
    | ID '(' expr ')'                    # userFunctionCall
    | op=('+'|'-') expr                  # unary
    | constant                           # constantExpr
    | NUMBER                             # number
    | ID                                 # id
    | '(' expr ')'                       # parens
    ;

function
    : 'sin'
    | 'cos'
    | 'tan'
    | 'sqrt'
    | 'log'
    | 'ln'
    | 'abs'
    | 'exp'
    | 'asin'
    | 'acos'
    | 'atan'
    | 'floor'
    | 'ceil'
    ;

function2
    : 'pow'
    | 'max'
    | 'min'
    ;

constant
    : 'pi'
    | 'e'
    ;

MUL : '*';
DIV : '/';
ADD : '+';
SUB : '-';

NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

ID
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

NEWLINE
    : '\r'? '\n'
    ;

WS
    : [ \t]+ -> skip
    ;

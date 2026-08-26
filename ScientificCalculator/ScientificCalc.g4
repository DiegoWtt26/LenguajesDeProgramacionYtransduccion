grammar ScientificCalc;

prog
    : stat+ EOF
    ;

stat
    : expr NEWLINE                                          # printExpr
    | ID '=' expr NEWLINE                                   # assign
    | 'clear' NEWLINE                                       # clear
    | 'vars' NEWLINE                                        # showVars
    | 'plot' '(' expr ',' expr ',' expr ')' NEWLINE         # plotExpr
    | NEWLINE                                               # blank
    ;

expr
    : <assoc=right> expr '^' expr   # power
    | expr op=('*'|'/') expr        # mulDiv
    | expr op=('+'|'-') expr        # addSub
    | function '(' expr ')'         # functionCall
    | op=('+'|'-') expr             # unary
    | constant                      # constantExpr
    | NUMBER                        # number
    | ID                            # id
    | '(' expr ')'                  # parens
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

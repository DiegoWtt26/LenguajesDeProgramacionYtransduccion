lexer grammar Expr11LabLexer;

// Tokens (sin literales sueltos: cada simbolo tiene su propio token
// porque lab.antlr.org usa Lexer y Parser por separado).

ID    : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM   : [0-9]+ ;
MAS   : '+' ;
MENOS : '-' ;
POR   : '*' ;
LP    : '(' ;
RP    : ')' ;
WS    : [ \t\r\n]+ -> skip ;

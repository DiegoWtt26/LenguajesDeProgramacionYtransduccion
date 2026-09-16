lexer grammar Expr12LabLexer;

// Tokens para lab.antlr.org (pestana Lexer).
// Diapositiva 12/13: solo '+' y '*' (tal cual la gramatica por niveles).

ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM : [0-9]+ ;
MAS : '+' ;
POR : '*' ;
LP  : '(' ;
RP  : ')' ;
WS  : [ \t\r\n]+ -> skip ;

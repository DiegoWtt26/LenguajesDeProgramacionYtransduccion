lexer grammar ExprAmbLabLexer;

// Tokens para lab.antlr.org (pestana Lexer).
// Diapositiva 15 TAL CUAL: gramatica ambigua E -> E + E | E * E | num.
// Sin parentesis: solo NUM, MAS, POR.

NUM : [0-9]+ ;
MAS : '+' ;
POR : '*' ;
WS  : [ \t\r\n]+ -> skip ;

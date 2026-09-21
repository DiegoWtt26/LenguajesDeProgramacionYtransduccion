// Lexer compartido para lab.antlr.org (pestana Lexer).
// Lo usan los 4 parsers: G1_PrecLeftLabParser, G2_PrecRightLabParser,
// G3_PrecInvLabParser y G4_PrecFlatLabParser (tokenVocab=PrecLabLexer).
// Tokens: + - * / ( ) y NUM. Sin identificadores.

lexer grammar PrecLabLexer;

NUM   : [0-9]+ ;
MAS   : '+' ;
MENOS : '-' ;
POR   : '*' ;
DIV   : '/' ;
LP    : '(' ;
RP    : ')' ;
WS    : [ \t\r\n]+ -> skip ;

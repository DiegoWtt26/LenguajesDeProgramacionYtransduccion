parser grammar ExprAmbInvLabParser;

// Copiar en la pestana Parser de lab.antlr.org (con el MISMO Lexer
// ExprAmbLabLexer). Start rule: prog | Input: 2 + 3 * 4.
// Mismo input, OTRO arbol => demuestra que la gramatica es ambigua.

options { tokenVocab=ExprAmbLabLexer; }

prog : expr EOF ;

expr : expr POR expr # Mult
     | expr MAS expr # Suma
     | NUM           # Num
     ;

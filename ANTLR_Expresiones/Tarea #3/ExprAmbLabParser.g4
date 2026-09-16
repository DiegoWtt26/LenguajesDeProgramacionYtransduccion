parser grammar ExprAmbLabParser;

// Copiar en la pestana Parser de lab.antlr.org.
// Start rule: prog   |   Input de ejemplo: 2 + 3 * 4

options { tokenVocab=ExprAmbLabLexer; }

// Diapositiva 15 AMBIGUA TAL CUAL: E -> E + E | E * E | num.
// La pagina mostrara UN arbol (ANTLR resuelve en silencio por orden);
// para ver el OTRO arbol usa ExprAmbInvLabParser.g4 (orden invertido).

prog : expr EOF ;

expr : expr MAS expr # Suma
     | expr POR expr # Mult
     | NUM           # Num
     ;

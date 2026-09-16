parser grammar Expr12LabParser;

// Copiar en la pestana Parser de lab.antlr.org.
// Start rule: prog   |   Input de ejemplo: 3 + 4 * 5

options { tokenVocab=Expr12LabLexer; }

// Diapositiva 11/12:  E -> E + T | T ;  T -> T * F | F ;  F -> id|num|(E)

prog : e EOF ;

e : e MAS t # Suma
  | t       # A_T
  ;

t : t POR f # Mult
  | f       # A_F
  ;

f : ID      # Id
  | NUM     # Num
  | LP e RP # Parens
  ;

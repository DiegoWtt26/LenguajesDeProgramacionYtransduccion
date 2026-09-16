parser grammar Expr11LabParser;

// Vincula los tokens definidos en la pestana Lexer.
options { tokenVocab=Expr11LabLexer; }

// Diapositiva 11 TAL CUAL:  E -> E + T | T ;  T -> T * F | F ;  F -> id|num|(E)
// Solo '+' y '*'. Sin '-': "2+3-4" debe dar error (RECHAZADA).

prog : e EOF ;

e : e MAS t   # Suma
  | t         # A_T
  ;

t : t POR f   # Mult
  | f         # A_F
  ;

f : ID      # Id
  | NUM     # Num
  | LP e RP # Parens
  ;

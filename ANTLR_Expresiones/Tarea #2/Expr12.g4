// ============================================================
// Tarea #2 - Diapositivas 12 (Parse Tree) y 13 (AST)
// Misma gramatica de expresiones de la diapositiva 11:
//
//   E -> E + T | T
//   T -> T * F | F
//   F -> id | num | ( E )
//
// Ejemplo del PDF:  3 + 4 * 5
//   Parse Tree (diapo 12): conserva TODA la estructura E/T/F.
//   AST (diapo 13): solo operadores y operandos:  + ( 3, * (4, 5) )
// ============================================================
grammar Expr12;

prog : e EOF ;

e : e '+' t   # Suma
  | t         # A_T
  ;

t : t '*' f   # Mult
  | f         # A_F
  ;

f : ID          # Id
  | NUM         # Num
  | '(' e ')'   # Parens
  ;

ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;

// ============================================================
// Tarea #1 - Diapositiva 11: Expresiones aritmeticas TAL CUAL
// Gramatica original del PDF:
//
//   E -> E + T | T
//   T -> T * F | F
//   F -> id | num | ( E )
//
// En ANTLR (las reglas de parser van en minusculas y los
// tokens del lexer en MAYUSCULAS):
//   e : e '+' t | t ;
//   t : t '*' f | f ;
//   f : ID | NUM | '(' e ')' ;
//
// 100% TAL CUAL: solo '+' y '*'. Sin '-'.
// Los ejemplos del PDF con '-' (2+3-4, 2+3*(4-5)) son
// RECHAZADOS por esta gramatica, y eso es lo correcto:
// el .py lo reporta como RECHAZADA + el .txt lo comprueba.
// ============================================================
grammar Expr11;

// Regla inicial (el parser debe terminar en EOF)
prog : e EOF ;

e
    : e '+' t   # Suma
    | t         # A_T     // E -> T
    ;

t
    : t '*' f   # Mult
    | f         # A_F     // T -> F
    ;

f
    : ID            # Id
    | NUM           # Num
    | '(' e ')'     # Parens  // F -> ( E )
    ;

// ---- Lexer ----
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;

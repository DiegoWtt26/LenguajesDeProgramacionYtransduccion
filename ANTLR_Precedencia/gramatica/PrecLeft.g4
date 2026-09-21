// ============================================================
// G1 - Asociatividad IZQUIERDA + precedencia CORRECTA
// Diapos 27-31 del PDF:  E -> E op T  (izquierda)
//                        T -> T op F  (izquierda)
// Precedencia:  *,/  >  +,-   (niveles: E abajo, T arriba)
// 4 - 3 - 2  =>  (4-3)-2 = -1   |   2 + 3*4  =>  2+(3*4) = 14
// Operadores: + - * /  y parentesis. Division real (float).
// ============================================================
grammar PrecLeft;

prog : e EOF ;

e
    : e ('+'|'-') t   # SumaResta
    | t               # A_T
    ;

t
    : t ('*'|'/') f   # MultDiv
    | f               # A_F
    ;

f
    : NUM             # Num
    | '(' e ')'       # Parens
    ;

NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;

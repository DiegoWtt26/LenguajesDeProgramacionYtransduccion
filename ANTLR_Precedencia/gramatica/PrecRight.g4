// ============================================================
// G2 - Asociatividad DERECHA + precedencia CORRECTA
// Diapo 28 del PDF:  E -> T op E  (derecha)
// Misma precedencia que G1:  *,/  >  +,-
// 4 - 3 - 2  =>  4-(3-2) = 3   |   8 / 4 / 2  =>  8/(4/2) = 4
// Comparar con G1 aisla el efecto de la ASOCIATIVIDAD.
// Operadores: + - * /  y parentesis. Division real (float).
// ============================================================
grammar PrecRight;

prog : e EOF ;

e
    : t ('+'|'-') e   # SumaResta
    | t               # A_T
    ;

t
    : f ('*'|'/') t   # MultDiv
    | f               # A_F
    ;

f
    : NUM             # Num
    | '(' e ')'       # Parens
    ;

NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;

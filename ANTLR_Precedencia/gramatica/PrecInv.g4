// ============================================================
// G3 - Asociatividad IZQUIERDA + precedencia INVERTIDA (a proposito)
// Niveles al reves que G1: el nivel superior agrupa *,/ (baja)
// y el nivel inferior agrupa +,- (alta). O sea:  +,-  >  *,/
// 2 + 3 * 4  =>  (2+3)*4 = 20   (en G1 da 14)
// 10 - 2 * 3 =>  (10-2)*3 = 24  (en G1 da 4)
// Demuestra que la precedencia vive en la ESTRUCTURA de niveles
// (diapo 30), no en los simbolos.
// Operadores: + - * /  y parentesis. Division real (float).
// ============================================================
grammar PrecInv;

prog : e EOF ;

e
    : e ('*'|'/') t   # MultDiv
    | t               # A_T
    ;

t
    : t ('+'|'-') f   # SumaResta
    | f               # A_F
    ;

f
    : NUM             # Num
    | '(' e ')'       # Parens
    ;

NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;

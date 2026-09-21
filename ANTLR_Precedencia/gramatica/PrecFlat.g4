// ============================================================
// G4 - SIN niveles de precedencia: un solo nivel, todo a la izquierda
// expr : atom (op atom)*   se pliega siempre por la izquierda,
// o sea evaluacion estrictamente de izquierda a derecha:
// 2 + 3 * 4  =>  (2+3)*4 = 20   (igual que G3 aqui, pero por otra causa)
// 10 - 2 * 3 =>  (10-2)*3 = 24
// 2 + 3*4 - 5/5 => (((2+3)*4)-5)/5 = 3  (en G1/G2 da 13, en G3 da -1)
// Sirve de control: sin niveles no hay precedencia (diapo 30).
// Operadores: + - * /  y parentesis. Division real (float).
// ============================================================
grammar PrecFlat;

prog : expr EOF ;

expr : atom (op atom)* ;

op
    : '+'
    | '-'
    | '*'
    | '/'
    ;

atom
    : NUM
    | '(' expr ')'
    ;

NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;

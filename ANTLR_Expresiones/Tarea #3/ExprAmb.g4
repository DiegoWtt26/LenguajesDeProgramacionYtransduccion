// ============================================================
// Tarea #3 - Diapositiva 15: gramatica AMBIGUA TAL CUAL
// Gramatica original del PDF:
//
//   E -> E + E
//   E -> E * E
//   E -> num
//
// Ejemplo:  2 + 3 * 4  tiene DOS arboles posibles:
//   (2 + 3) * 4 = 20   vs   2 + (3 * 4) = 14
//
// En ANTLR TAL CUAL (sin precedencia declarada, sin parentesis):
// ============================================================
grammar ExprAmb;

prog : expr EOF ;

expr
    : expr '+' expr   # Suma
    | expr '*' expr   # Mult
    | NUM             # Num
    ;

NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;

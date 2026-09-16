// ============================================================
// Tarea #3 (parte B) - Misma gramatica ambigua pero con el
// ORDEN de alternativas invertido:
//
//   E -> E * E   (ahora primero)
//   E -> E + E   (ahora segundo)
//   E -> num
//
// ANTLR asigna precedencia implicita por orden en reglas
// recursivas a izquierda: la alternativa escrita PRIMERO
// agrupa "mas fuerte". Al invertir el orden, el MISMO input
// "2 + 3 * 4" produce el OTRO arbol. Eso DEMUESTRA que la
// gramatica original es ambigua: el resultado depende del
// orden arbitrario de las reglas, no de la entrada.
// ============================================================
grammar ExprAmbInv;

prog : expr EOF ;

expr
    : expr '*' expr   # Mult
    | expr '+' expr   # Suma
    | NUM             # Num
    ;

NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;

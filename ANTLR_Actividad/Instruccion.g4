grammar Instruccion;

programa
    : instruccion+ EOF
    ;

instruccion
    : MOSTRAR ID
    | CARGAR ID
    | GRAFICAR ID
    ;

MOSTRAR
    : 'mostrar'
    ;

CARGAR
    : 'cargar'
    ;

GRAFICAR
    : 'graficar'
    ;

ID
    : [a-zA-Z]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

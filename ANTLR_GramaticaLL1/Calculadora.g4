grammar Calculadora;

// Reglas sintácticas

inicio    : programa EOF ;

programa  : sentencia programa
          |
          ;

sentencia : ID ASIGNAR expr PUNTOYCOMA ;

expr      : term exprP ;

exprP     : MAS term exprP
          | MENOS term exprP
          |
          ;

term      : factor termP ;

termP     : POR factor termP
          | DIV factor termP
          | MOD factor termP
          | PORCENTAJE factor termP
          |
          ;

factor    : MENOS factor
          | primario
          ;

primario  : NUM
          | ID
          | PAR_IZQ expr PAR_DER
          | BARRA expr BARRA
          | func PAR_IZQ expr PAR_DER
          ;

func      : SIN
          | COS
          | TAN
          | ABS
          ;

// Reglas léxicas

SIN        : 'sin' ;
COS        : 'cos' ;
TAN        : 'tan' ;
MOD        : 'mod' ;
ABS        : 'abs' ;

ID         : [a-zA-Z_] [a-zA-Z_0-9]* ;
NUM        : [0-9]+ ('.' [0-9]+)? ;

MAS        : '+' ;
MENOS      : '-' ;
POR        : '*' ;
DIV        : '/' ;
PORCENTAJE : '%' ;
BARRA      : '|' ;
ASIGNAR    : '=' ;
PAR_IZQ    : '(' ;
PAR_DER    : ')' ;
PUNTOYCOMA : ';' ;

COMENTARIO : '#' ~[\r\n]* -> skip ;
ESPACIOS   : [ \t\r\n]+   -> skip ;

# Ejercicio 2

## Enunciado del libro

Make the calculator into a hex calculator that accepts both hex and decimal numbers.
In the scanner add a pattern such as `0x[a-f0-9]+` to match a hex number, and in the
action code use `strtol` to convert the string to a number that you store in `yylval`;
then return a `NUMBER` token. Adjust the output `printf` to print the result in both
decimal and hex.

Se agregan números hexadecimales al scanner y se imprime cada resultado en decimal y
hexadecimal. `strtol` convierte el texto usando base 16 para los números con prefijo
`0x` y base 10 para los números decimales.

## Scanner `ejercicio_2.l`

```lex
%{
#include <stdlib.h>
#include <stdio.h>
#include "ejercicio_2.tab.h"
%}
%%
"//"[^\n]*\n  { }
0[xX][0-9a-fA-F]+ { yylval = (int)strtol(yytext, 0, 16); return NUMBER; }
[0-9]+            { yylval = (int)strtol(yytext, 0, 10); return NUMBER; }
"+"               { return ADD; }
"-"               { return SUB; }
"*"               { return MUL; }
"/"               { return DIV; }
"|"               { return ABS; }
"("               { return OP; }
")"               { return CP; }
\n                { return EOL; }
[ \t]             { }
.                 { fprintf(stderr, "error: Caracter desconocido: %s\n", yytext); }
%%
```

## Parser `ejercicio_2.y`

```bison
%{
#include <stdio.h>
int yylex(void);
void yyerror(const char *message);
%}
%token NUMBER ADD SUB MUL DIV ABS EOL OP CP
%%
calclist:
    /* vacio */
  | calclist exp EOL { printf("= %d (0x%X)\n", $2, (unsigned)$2); }
  ;
exp:
    factor
  | exp ADD factor { $$ = $1 + $3; }
  | exp SUB factor { $$ = $1 - $3; }
  ;
factor:
    term
  | factor MUL term { $$ = $1 * $3; }
  | factor DIV term { $$ = $1 / $3; }
  ;
term:
    NUMBER
  | ABS term { $$ = $2 >= 0 ? $2 : -$2; }
  | OP exp CP { $$ = $2; }
  ;
%%
int main(void) { return yyparse(); }
void yyerror(const char *message) { fprintf(stderr, "error: %s\n", message); }
```

Compilación:

```text
bison -d ejercicio_2.y
flex ejercicio_2.l
cc -o ejercicio_2 ejercicio_2.tab.c lex.yy.c -lfl
```

Por ejemplo, `0x10 + 10` produce `= 26 (0x1A)`.

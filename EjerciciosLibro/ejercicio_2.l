%option noyywrap
%{
#include <stdio.h>
#include <stdlib.h>
#include "ejercicio_2.tab.h"
%}
%%
"//"[^\n]*\n       { }
0[xX][0-9a-fA-F]+ { yylval = (int)strtol(yytext, NULL, 16); return NUMBER; }
[0-9]+            { yylval = (int)strtol(yytext, NULL, 10); return NUMBER; }
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
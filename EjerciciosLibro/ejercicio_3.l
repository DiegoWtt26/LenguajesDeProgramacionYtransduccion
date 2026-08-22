%option noyywrap
%{
#include "ejercicio_3.tab.h"
%}
%%
"//"[^\n]*\n       { }
[0-9]+            { yylval = atoi(yytext); return NUMBER; }
"+"               { return ADD; }
"-"               { return SUB; }
"*"               { return MUL; }
"/"               { return DIV; }
"|"               { return ABS; }
"&"               { return AND; }
"("               { return OP; }
")"               { return CP; }
\n                { return EOL; }
[ \t]             { }
.                 { }
%%
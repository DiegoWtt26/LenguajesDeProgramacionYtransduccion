%{
#include <stdio.h>
int yylex(void);
void yyerror(const char *message);
%}
%define parse.error verbose
%token NUMBER ADD SUB MUL DIV ABS AND EOL OP CP
%%
calclist:
    /* vacio */
  | calclist exp EOL { printf("= %d\n", $2); }
  ;
exp:
    bit_or
  ;
bit_or:
    bit_or ABS bit_and { $$ = $1 | $3; }
  | bit_and
  ;
bit_and:
    bit_and AND sum { $$ = $1 & $3; }
  | sum
  ;
sum:
    sum ADD product { $$ = $1 + $3; }
  | sum SUB product { $$ = $1 - $3; }
  | product
  ;
product:
    product MUL unary { $$ = $1 * $3; }
  | product DIV unary { $$ = $1 / $3; }
  | unary
  ;
unary:
    NUMBER
  | ABS unary { $$ = $2 >= 0 ? $2 : -$2; }
  | OP exp CP { $$ = $2; }
  ;
%%
int main(void) { return yyparse(); }
void yyerror(const char *message) { fprintf(stderr, "error: %s\n", message); }
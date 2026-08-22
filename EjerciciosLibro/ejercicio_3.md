# Ejercicio 3

## Enunciado del libro

(extra credit) Add bit operators such as AND and OR to the calculator. The obvious
operator to use for OR is a vertical bar, but that’s already the unary absolute value
operator. What happens if you also use it as a binary OR operator, for example, `exp
ABS factor`?

El mismo carácter `|` puede representar el operador unario de valor absoluto y el
operador binario OR. El scanner puede devolver el mismo token (`ABS`) en ambos casos;
el parser determina cuál es por la posición del token: al inicio de un `term` es
unario y después de una expresión es binario.

## Cambios del parser

```bison
%token NUMBER ADD SUB MUL DIV ABS AND EOL OP CP
%%
exp:
    factor
  | exp ADD factor { $$ = $1 + $3; }
  | exp SUB factor { $$ = $1 - $3; }
  | exp ABS factor { $$ = $1 | $3; }
  ;
factor:
    term
  | factor MUL term { $$ = $1 * $3; }
  | factor DIV term { $$ = $1 / $3; }
  | factor AND term { $$ = $1 & $3; }
  ;
term:
    NUMBER
  | ABS term { $$ = $2 >= 0 ? $2 : -$2; }
  | OP exp CP { $$ = $2; }
  ;
```

## Cambios del scanner

```lex
"|" { return ABS; }
"&" { return AND; }
```

Con esta gramática no hay confusión entre `|7` (valor absoluto) y `5|2` (OR), porque
solo el primer caso puede aparecer donde se espera un `term`. Si se escribe una regla
ambigua como `exp: exp ABS exp | ABS exp | NUMBER`, Bison informa conflictos de
desplazamiento/reducción y no se debe ignorar ese diagnóstico: hay que separar los
niveles de precedencia como en el código anterior.

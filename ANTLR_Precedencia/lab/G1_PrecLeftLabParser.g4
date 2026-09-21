// ================= G1 : izquierda + precedencia CORRECTA =================
// Para lab.antlr.org (pestana Parser). Start rule: prog.
// Copiar tambien PrecLabLexer.g4 en la pestana Lexer.

parser grammar G1_PrecLeftLabParser;

options { tokenVocab=PrecLabLexer; }

prog : e EOF ;

e : e (MAS|MENOS) t   # SumaResta
  | t                 # A_T
  ;

t : t (POR|DIV) f     # MultDiv
  | f                 # A_F
  ;

f : NUM               # Num
  | LP e RP           # Parens
  ;

// ================= G3 : izquierda + precedencia INVERTIDA =================
// Para lab.antlr.org (pestana Parser). Start rule: prog.
// Copiar tambien PrecLabLexer.g4 en la pestana Lexer.

parser grammar G3_PrecInvLabParser;

options { tokenVocab=PrecLabLexer; }

prog : e EOF ;

e : e (POR|DIV) t     # MultDiv
  | t                 # A_T
  ;

t : t (MAS|MENOS) f   # SumaResta
  | f                 # A_F
  ;

f : NUM               # Num
  | LP e RP           # Parens
  ;

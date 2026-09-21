// ================= G2 : derecha + precedencia CORRECTA =================
// Para lab.antlr.org (pestana Parser). Start rule: prog.
// Copiar tambien PrecLabLexer.g4 en la pestana Lexer.

parser grammar G2_PrecRightLabParser;

options { tokenVocab=PrecLabLexer; }

prog : e EOF ;

e : t (MAS|MENOS) e   # SumaResta
  | t                 # A_T
  ;

t : f (POR|DIV) t     # MultDiv
  | f                 # A_F
  ;

f : NUM               # Num
  | LP e RP           # Parens
  ;

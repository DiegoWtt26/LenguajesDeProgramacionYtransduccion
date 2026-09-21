// ================= G4 : SIN niveles, todo a la izquierda =================
// Para lab.antlr.org (pestana Parser). Start rule: prog.
// Copiar tambien PrecLabLexer.g4 en la pestana Lexer.

parser grammar G4_PrecFlatLabParser;

options { tokenVocab=PrecLabLexer; }

prog : expr EOF ;

expr : atom (op atom)* ;

op : MAS | MENOS | POR | DIV ;

atom : NUM | LP expr RP ;

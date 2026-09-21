# Generated from gramatica/PrecFlat.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PrecFlatParser import PrecFlatParser
else:
    from PrecFlatParser import PrecFlatParser

# This class defines a complete listener for a parse tree produced by PrecFlatParser.
class PrecFlatListener(ParseTreeListener):

    # Enter a parse tree produced by PrecFlatParser#prog.
    def enterProg(self, ctx:PrecFlatParser.ProgContext):
        pass

    # Exit a parse tree produced by PrecFlatParser#prog.
    def exitProg(self, ctx:PrecFlatParser.ProgContext):
        pass


    # Enter a parse tree produced by PrecFlatParser#expr.
    def enterExpr(self, ctx:PrecFlatParser.ExprContext):
        pass

    # Exit a parse tree produced by PrecFlatParser#expr.
    def exitExpr(self, ctx:PrecFlatParser.ExprContext):
        pass


    # Enter a parse tree produced by PrecFlatParser#op.
    def enterOp(self, ctx:PrecFlatParser.OpContext):
        pass

    # Exit a parse tree produced by PrecFlatParser#op.
    def exitOp(self, ctx:PrecFlatParser.OpContext):
        pass


    # Enter a parse tree produced by PrecFlatParser#atom.
    def enterAtom(self, ctx:PrecFlatParser.AtomContext):
        pass

    # Exit a parse tree produced by PrecFlatParser#atom.
    def exitAtom(self, ctx:PrecFlatParser.AtomContext):
        pass



del PrecFlatParser
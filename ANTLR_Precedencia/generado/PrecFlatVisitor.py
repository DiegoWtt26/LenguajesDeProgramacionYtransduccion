# Generated from gramatica/PrecFlat.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PrecFlatParser import PrecFlatParser
else:
    from PrecFlatParser import PrecFlatParser

# This class defines a complete generic visitor for a parse tree produced by PrecFlatParser.

class PrecFlatVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrecFlatParser#prog.
    def visitProg(self, ctx:PrecFlatParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecFlatParser#expr.
    def visitExpr(self, ctx:PrecFlatParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecFlatParser#op.
    def visitOp(self, ctx:PrecFlatParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecFlatParser#atom.
    def visitAtom(self, ctx:PrecFlatParser.AtomContext):
        return self.visitChildren(ctx)



del PrecFlatParser
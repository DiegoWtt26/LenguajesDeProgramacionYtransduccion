# Generated from Expr11.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,2,1,2,1,2,1,2,1,2,1,2,
        5,2,29,8,2,10,2,12,2,32,9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,40,8,3,1,
        3,0,2,2,4,4,0,2,4,6,0,0,41,0,8,1,0,0,0,2,11,1,0,0,0,4,22,1,0,0,0,
        6,39,1,0,0,0,8,9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,6,1,-1,
        0,12,13,3,4,2,0,13,19,1,0,0,0,14,15,10,2,0,0,15,16,5,1,0,0,16,18,
        3,4,2,0,17,14,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,
        20,3,1,0,0,0,21,19,1,0,0,0,22,23,6,2,-1,0,23,24,3,6,3,0,24,30,1,
        0,0,0,25,26,10,2,0,0,26,27,5,2,0,0,27,29,3,6,3,0,28,25,1,0,0,0,29,
        32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,5,1,0,0,0,32,30,1,0,0,
        0,33,40,5,5,0,0,34,40,5,6,0,0,35,36,5,3,0,0,36,37,3,2,1,0,37,38,
        5,4,0,0,38,40,1,0,0,0,39,33,1,0,0,0,39,34,1,0,0,0,39,35,1,0,0,0,
        40,7,1,0,0,0,3,19,30,39
    ]

class Expr11Parser ( Parser ):

    grammarFileName = "Expr11.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUM", "WS" ]

    RULE_prog = 0
    RULE_e = 1
    RULE_t = 2
    RULE_f = 3

    ruleNames =  [ "prog", "e", "t", "f" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    NUM=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def e(self):
            return self.getTypedRuleContext(Expr11Parser.EContext,0)


        def EOF(self):
            return self.getToken(Expr11Parser.EOF, 0)

        def getRuleIndex(self):
            return Expr11Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = Expr11Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.e(0)
            self.state = 9
            self.match(Expr11Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Expr11Parser.RULE_e

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr11Parser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(Expr11Parser.EContext,0)

        def t(self):
            return self.getTypedRuleContext(Expr11Parser.TContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class A_TContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr11Parser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self):
            return self.getTypedRuleContext(Expr11Parser.TContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_T" ):
                listener.enterA_T(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_T" ):
                listener.exitA_T(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_T" ):
                return visitor.visitA_T(self)
            else:
                return visitor.visitChildren(self)



    def e(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Expr11Parser.EContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = Expr11Parser.A_TContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 12
            self.t(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Expr11Parser.SumaContext(self, Expr11Parser.EContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                    self.state = 14
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 15
                    self.match(Expr11Parser.T__0)
                    self.state = 16
                    self.t(0) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Expr11Parser.RULE_t

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr11Parser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self):
            return self.getTypedRuleContext(Expr11Parser.TContext,0)

        def f(self):
            return self.getTypedRuleContext(Expr11Parser.FContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class A_FContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr11Parser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def f(self):
            return self.getTypedRuleContext(Expr11Parser.FContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_F" ):
                listener.enterA_F(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_F" ):
                listener.exitA_F(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_F" ):
                return visitor.visitA_F(self)
            else:
                return visitor.visitChildren(self)



    def t(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Expr11Parser.TContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_t, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = Expr11Parser.A_FContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 23
            self.f()
            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Expr11Parser.MultContext(self, Expr11Parser.TContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_t)
                    self.state = 25
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 26
                    self.match(Expr11Parser.T__1)
                    self.state = 27
                    self.f() 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Expr11Parser.RULE_f

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParensContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr11Parser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(Expr11Parser.EContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr11Parser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(Expr11Parser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr11Parser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(Expr11Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def f(self):

        localctx = Expr11Parser.FContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_f)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = Expr11Parser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(Expr11Parser.ID)
                pass
            elif token in [6]:
                localctx = Expr11Parser.NumContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(Expr11Parser.NUM)
                pass
            elif token in [3]:
                localctx = Expr11Parser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(Expr11Parser.T__2)
                self.state = 36
                self.e(0)
                self.state = 37
                self.match(Expr11Parser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.e_sempred
        self._predicates[2] = self.t_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def e_sempred(self, localctx:EContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def t_sempred(self, localctx:TContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         





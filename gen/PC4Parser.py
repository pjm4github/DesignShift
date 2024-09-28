# Generated from C:/Users/pmora/Documents/Git/GitHub/DesignShift/PC4.g4 by ANTLR 4.13.1
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
        4,1,34,113,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,4,0,37,8,0,11,0,12,0,38,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,1,3,1,4,1,4,1,5,1,5,
        1,6,1,6,1,6,1,6,3,6,77,8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,3,9,91,8,9,1,10,1,10,1,11,1,11,1,12,1,12,5,12,99,8,12,
        10,12,12,12,102,9,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,1,0,8,
        14,1,0,18,26,106,0,36,1,0,0,0,2,42,1,0,0,0,4,47,1,0,0,0,6,57,1,0,
        0,0,8,68,1,0,0,0,10,70,1,0,0,0,12,72,1,0,0,0,14,78,1,0,0,0,16,81,
        1,0,0,0,18,90,1,0,0,0,20,92,1,0,0,0,22,94,1,0,0,0,24,96,1,0,0,0,
        26,103,1,0,0,0,28,105,1,0,0,0,30,110,1,0,0,0,32,37,3,4,2,0,33,37,
        3,6,3,0,34,37,3,2,1,0,35,37,5,32,0,0,36,32,1,0,0,0,36,33,1,0,0,0,
        36,34,1,0,0,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,
        0,0,0,39,40,1,0,0,0,40,41,5,0,0,1,41,1,1,0,0,0,42,43,5,15,0,0,43,
        44,3,30,15,0,44,45,3,24,12,0,45,46,5,32,0,0,46,3,1,0,0,0,47,48,5,
        17,0,0,48,49,3,26,13,0,49,50,3,10,5,0,50,51,3,12,6,0,51,53,3,18,
        9,0,52,54,3,28,14,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,
        56,5,32,0,0,56,5,1,0,0,0,57,58,5,16,0,0,58,59,3,12,6,0,59,60,3,14,
        7,0,60,61,3,16,8,0,61,62,3,20,10,0,62,64,3,22,11,0,63,65,3,28,14,
        0,64,63,1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,67,5,32,0,0,67,7,
        1,0,0,0,68,69,5,33,0,0,69,9,1,0,0,0,70,71,7,0,0,0,71,11,1,0,0,0,
        72,76,5,31,0,0,73,74,5,1,0,0,74,75,5,31,0,0,75,77,5,2,0,0,76,73,
        1,0,0,0,76,77,1,0,0,0,77,13,1,0,0,0,78,79,5,3,0,0,79,80,5,27,0,0,
        80,15,1,0,0,0,81,82,5,4,0,0,82,83,5,27,0,0,83,17,1,0,0,0,84,85,5,
        5,0,0,85,91,5,27,0,0,86,87,5,6,0,0,87,91,5,27,0,0,88,89,5,7,0,0,
        89,91,5,27,0,0,90,84,1,0,0,0,90,86,1,0,0,0,90,88,1,0,0,0,91,19,1,
        0,0,0,92,93,3,18,9,0,93,21,1,0,0,0,94,95,3,18,9,0,95,23,1,0,0,0,
        96,100,5,31,0,0,97,99,5,31,0,0,98,97,1,0,0,0,99,102,1,0,0,0,100,
        98,1,0,0,0,100,101,1,0,0,0,101,25,1,0,0,0,102,100,1,0,0,0,103,104,
        5,31,0,0,104,27,1,0,0,0,105,106,5,27,0,0,106,107,5,27,0,0,107,108,
        5,27,0,0,108,109,5,27,0,0,109,29,1,0,0,0,110,111,7,1,0,0,111,31,
        1,0,0,0,7,36,38,53,64,76,90,100
    ]

class PC4Parser ( Parser ):

    grammarFileName = "PC4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'rel-'", "'id-connector-'", 
                     "'actor-'", "'ext-'", "'app-'", "'[Person]'", "'[User]'", 
                     "'[Actor]'", "'[Role]'", "'[Software System]'", "'[Existing System]'", 
                     "'[Container]'", "'Legend: '", "'Connector:'", "'Element: '", 
                     "'[System Landscape]'", "'[System Context]'", "'[Container View]'", 
                     "'[Component View]'", "'[Code View]'", "'[Image View]'", 
                     "'[Dynamic View]'", "'[Deployment View]'", "'[Filtered View]'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Person", "User", "Actor", "Role", "Software_system", 
                      "Existing_system", "Container", "Legend", "Connector", 
                      "Element", "SystemLandscapeView", "SystemContextView", 
                      "ContainerView", "ComponentView", "CodeView", "ImageView", 
                      "DynamicView", "DeploymentView", "FilteredView", "DIGITS", 
                      "LETTERS", "SPECIALS", "TEXT", "DESCRIPTION", "NEWLINE", 
                      "LineComment", "WS" ]

    RULE_parse = 0
    RULE_legend = 1
    RULE_element = 2
    RULE_connector = 3
    RULE_comment = 4
    RULE_elementKeyword = 5
    RULE_relation = 6
    RULE_catalogRelation = 7
    RULE_uniqueConnectorId = 8
    RULE_uniqueId = 9
    RULE_sourceId = 10
    RULE_targetId = 11
    RULE_sentence = 12
    RULE_name = 13
    RULE_location = 14
    RULE_viewKeyword = 15

    ruleNames =  [ "parse", "legend", "element", "connector", "comment", 
                   "elementKeyword", "relation", "catalogRelation", "uniqueConnectorId", 
                   "uniqueId", "sourceId", "targetId", "sentence", "name", 
                   "location", "viewKeyword" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    Person=8
    User=9
    Actor=10
    Role=11
    Software_system=12
    Existing_system=13
    Container=14
    Legend=15
    Connector=16
    Element=17
    SystemLandscapeView=18
    SystemContextView=19
    ContainerView=20
    ComponentView=21
    CodeView=22
    ImageView=23
    DynamicView=24
    DeploymentView=25
    FilteredView=26
    DIGITS=27
    LETTERS=28
    SPECIALS=29
    TEXT=30
    DESCRIPTION=31
    NEWLINE=32
    LineComment=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PC4Parser.EOF, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PC4Parser.ElementContext)
            else:
                return self.getTypedRuleContext(PC4Parser.ElementContext,i)


        def connector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PC4Parser.ConnectorContext)
            else:
                return self.getTypedRuleContext(PC4Parser.ConnectorContext,i)


        def legend(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PC4Parser.LegendContext)
            else:
                return self.getTypedRuleContext(PC4Parser.LegendContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PC4Parser.NEWLINE)
            else:
                return self.getToken(PC4Parser.NEWLINE, i)

        def getRuleIndex(self):
            return PC4Parser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = PC4Parser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17]:
                    self.state = 32
                    self.element()
                    pass
                elif token in [16]:
                    self.state = 33
                    self.connector()
                    pass
                elif token in [15]:
                    self.state = 34
                    self.legend()
                    pass
                elif token in [32]:
                    self.state = 35
                    self.match(PC4Parser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4295196672) != 0)):
                    break

            self.state = 40
            self.match(PC4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LegendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Legend(self):
            return self.getToken(PC4Parser.Legend, 0)

        def viewKeyword(self):
            return self.getTypedRuleContext(PC4Parser.ViewKeywordContext,0)


        def sentence(self):
            return self.getTypedRuleContext(PC4Parser.SentenceContext,0)


        def NEWLINE(self):
            return self.getToken(PC4Parser.NEWLINE, 0)

        def getRuleIndex(self):
            return PC4Parser.RULE_legend

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLegend" ):
                listener.enterLegend(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLegend" ):
                listener.exitLegend(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLegend" ):
                return visitor.visitLegend(self)
            else:
                return visitor.visitChildren(self)




    def legend(self):

        localctx = PC4Parser.LegendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_legend)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(PC4Parser.Legend)
            self.state = 43
            self.viewKeyword()
            self.state = 44
            self.sentence()
            self.state = 45
            self.match(PC4Parser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Element(self):
            return self.getToken(PC4Parser.Element, 0)

        def name(self):
            return self.getTypedRuleContext(PC4Parser.NameContext,0)


        def elementKeyword(self):
            return self.getTypedRuleContext(PC4Parser.ElementKeywordContext,0)


        def relation(self):
            return self.getTypedRuleContext(PC4Parser.RelationContext,0)


        def uniqueId(self):
            return self.getTypedRuleContext(PC4Parser.UniqueIdContext,0)


        def NEWLINE(self):
            return self.getToken(PC4Parser.NEWLINE, 0)

        def location(self):
            return self.getTypedRuleContext(PC4Parser.LocationContext,0)


        def getRuleIndex(self):
            return PC4Parser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = PC4Parser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(PC4Parser.Element)
            self.state = 48
            self.name()
            self.state = 49
            self.elementKeyword()
            self.state = 50
            self.relation()
            self.state = 51
            self.uniqueId()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 52
                self.location()


            self.state = 55
            self.match(PC4Parser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConnectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Connector(self):
            return self.getToken(PC4Parser.Connector, 0)

        def relation(self):
            return self.getTypedRuleContext(PC4Parser.RelationContext,0)


        def catalogRelation(self):
            return self.getTypedRuleContext(PC4Parser.CatalogRelationContext,0)


        def uniqueConnectorId(self):
            return self.getTypedRuleContext(PC4Parser.UniqueConnectorIdContext,0)


        def sourceId(self):
            return self.getTypedRuleContext(PC4Parser.SourceIdContext,0)


        def targetId(self):
            return self.getTypedRuleContext(PC4Parser.TargetIdContext,0)


        def NEWLINE(self):
            return self.getToken(PC4Parser.NEWLINE, 0)

        def location(self):
            return self.getTypedRuleContext(PC4Parser.LocationContext,0)


        def getRuleIndex(self):
            return PC4Parser.RULE_connector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConnector" ):
                listener.enterConnector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConnector" ):
                listener.exitConnector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConnector" ):
                return visitor.visitConnector(self)
            else:
                return visitor.visitChildren(self)




    def connector(self):

        localctx = PC4Parser.ConnectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_connector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(PC4Parser.Connector)
            self.state = 58
            self.relation()
            self.state = 59
            self.catalogRelation()
            self.state = 60
            self.uniqueConnectorId()
            self.state = 61
            self.sourceId()
            self.state = 62
            self.targetId()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 63
                self.location()


            self.state = 66
            self.match(PC4Parser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LineComment(self):
            return self.getToken(PC4Parser.LineComment, 0)

        def getRuleIndex(self):
            return PC4Parser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = PC4Parser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PC4Parser.LineComment)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Person(self):
            return self.getToken(PC4Parser.Person, 0)

        def User(self):
            return self.getToken(PC4Parser.User, 0)

        def Actor(self):
            return self.getToken(PC4Parser.Actor, 0)

        def Role(self):
            return self.getToken(PC4Parser.Role, 0)

        def Existing_system(self):
            return self.getToken(PC4Parser.Existing_system, 0)

        def Software_system(self):
            return self.getToken(PC4Parser.Software_system, 0)

        def Container(self):
            return self.getToken(PC4Parser.Container, 0)

        def getRuleIndex(self):
            return PC4Parser.RULE_elementKeyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementKeyword" ):
                listener.enterElementKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementKeyword" ):
                listener.exitElementKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementKeyword" ):
                return visitor.visitElementKeyword(self)
            else:
                return visitor.visitChildren(self)




    def elementKeyword(self):

        localctx = PC4Parser.ElementKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elementKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32512) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESCRIPTION(self, i:int=None):
            if i is None:
                return self.getTokens(PC4Parser.DESCRIPTION)
            else:
                return self.getToken(PC4Parser.DESCRIPTION, i)

        def getRuleIndex(self):
            return PC4Parser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = PC4Parser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(PC4Parser.DESCRIPTION)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 73
                self.match(PC4Parser.T__0)
                self.state = 74
                self.match(PC4Parser.DESCRIPTION)
                self.state = 75
                self.match(PC4Parser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatalogRelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self):
            return self.getToken(PC4Parser.DIGITS, 0)

        def getRuleIndex(self):
            return PC4Parser.RULE_catalogRelation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatalogRelation" ):
                listener.enterCatalogRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatalogRelation" ):
                listener.exitCatalogRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatalogRelation" ):
                return visitor.visitCatalogRelation(self)
            else:
                return visitor.visitChildren(self)




    def catalogRelation(self):

        localctx = PC4Parser.CatalogRelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_catalogRelation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(PC4Parser.T__2)
            self.state = 79
            self.match(PC4Parser.DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UniqueConnectorIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self):
            return self.getToken(PC4Parser.DIGITS, 0)

        def getRuleIndex(self):
            return PC4Parser.RULE_uniqueConnectorId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniqueConnectorId" ):
                listener.enterUniqueConnectorId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniqueConnectorId" ):
                listener.exitUniqueConnectorId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniqueConnectorId" ):
                return visitor.visitUniqueConnectorId(self)
            else:
                return visitor.visitChildren(self)




    def uniqueConnectorId(self):

        localctx = PC4Parser.UniqueConnectorIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_uniqueConnectorId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(PC4Parser.T__3)
            self.state = 82
            self.match(PC4Parser.DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UniqueIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self):
            return self.getToken(PC4Parser.DIGITS, 0)

        def getRuleIndex(self):
            return PC4Parser.RULE_uniqueId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniqueId" ):
                listener.enterUniqueId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniqueId" ):
                listener.exitUniqueId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniqueId" ):
                return visitor.visitUniqueId(self)
            else:
                return visitor.visitChildren(self)




    def uniqueId(self):

        localctx = PC4Parser.UniqueIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_uniqueId)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(PC4Parser.T__4)
                self.state = 85
                self.match(PC4Parser.DIGITS)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(PC4Parser.T__5)
                self.state = 87
                self.match(PC4Parser.DIGITS)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(PC4Parser.T__6)
                self.state = 89
                self.match(PC4Parser.DIGITS)
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


    class SourceIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uniqueId(self):
            return self.getTypedRuleContext(PC4Parser.UniqueIdContext,0)


        def getRuleIndex(self):
            return PC4Parser.RULE_sourceId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceId" ):
                listener.enterSourceId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceId" ):
                listener.exitSourceId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSourceId" ):
                return visitor.visitSourceId(self)
            else:
                return visitor.visitChildren(self)




    def sourceId(self):

        localctx = PC4Parser.SourceIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sourceId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.uniqueId()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TargetIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uniqueId(self):
            return self.getTypedRuleContext(PC4Parser.UniqueIdContext,0)


        def getRuleIndex(self):
            return PC4Parser.RULE_targetId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTargetId" ):
                listener.enterTargetId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTargetId" ):
                listener.exitTargetId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTargetId" ):
                return visitor.visitTargetId(self)
            else:
                return visitor.visitChildren(self)




    def targetId(self):

        localctx = PC4Parser.TargetIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_targetId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.uniqueId()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESCRIPTION(self, i:int=None):
            if i is None:
                return self.getTokens(PC4Parser.DESCRIPTION)
            else:
                return self.getToken(PC4Parser.DESCRIPTION, i)

        def getRuleIndex(self):
            return PC4Parser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence" ):
                return visitor.visitSentence(self)
            else:
                return visitor.visitChildren(self)




    def sentence(self):

        localctx = PC4Parser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(PC4Parser.DESCRIPTION)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 97
                self.match(PC4Parser.DESCRIPTION)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESCRIPTION(self):
            return self.getToken(PC4Parser.DESCRIPTION, 0)

        def getRuleIndex(self):
            return PC4Parser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = PC4Parser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(PC4Parser.DESCRIPTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(PC4Parser.DIGITS)
            else:
                return self.getToken(PC4Parser.DIGITS, i)

        def getRuleIndex(self):
            return PC4Parser.RULE_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocation" ):
                listener.enterLocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocation" ):
                listener.exitLocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocation" ):
                return visitor.visitLocation(self)
            else:
                return visitor.visitChildren(self)




    def location(self):

        localctx = PC4Parser.LocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(PC4Parser.DIGITS)
            self.state = 106
            self.match(PC4Parser.DIGITS)
            self.state = 107
            self.match(PC4Parser.DIGITS)
            self.state = 108
            self.match(PC4Parser.DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ViewKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SystemLandscapeView(self):
            return self.getToken(PC4Parser.SystemLandscapeView, 0)

        def SystemContextView(self):
            return self.getToken(PC4Parser.SystemContextView, 0)

        def ContainerView(self):
            return self.getToken(PC4Parser.ContainerView, 0)

        def ComponentView(self):
            return self.getToken(PC4Parser.ComponentView, 0)

        def CodeView(self):
            return self.getToken(PC4Parser.CodeView, 0)

        def ImageView(self):
            return self.getToken(PC4Parser.ImageView, 0)

        def DynamicView(self):
            return self.getToken(PC4Parser.DynamicView, 0)

        def DeploymentView(self):
            return self.getToken(PC4Parser.DeploymentView, 0)

        def FilteredView(self):
            return self.getToken(PC4Parser.FilteredView, 0)

        def getRuleIndex(self):
            return PC4Parser.RULE_viewKeyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterViewKeyword" ):
                listener.enterViewKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitViewKeyword" ):
                listener.exitViewKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitViewKeyword" ):
                return visitor.visitViewKeyword(self)
            else:
                return visitor.visitChildren(self)




    def viewKeyword(self):

        localctx = PC4Parser.ViewKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_viewKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 133955584) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






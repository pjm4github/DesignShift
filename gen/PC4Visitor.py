# Generated from C:/Users/pmora/Documents/Git/GitHub/DesignShift/PC4.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PC4Parser import PC4Parser
else:
    from PC4Parser import PC4Parser

# This class defines a complete generic visitor for a parse tree produced by PC4Parser.

class PC4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by PC4Parser#parse.
    def visitParse(self, ctx:PC4Parser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#legend.
    def visitLegend(self, ctx:PC4Parser.LegendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#element.
    def visitElement(self, ctx:PC4Parser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#connector.
    def visitConnector(self, ctx:PC4Parser.ConnectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#comment.
    def visitComment(self, ctx:PC4Parser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#elementKeyword.
    def visitElementKeyword(self, ctx:PC4Parser.ElementKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#relation.
    def visitRelation(self, ctx:PC4Parser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#catalogRelation.
    def visitCatalogRelation(self, ctx:PC4Parser.CatalogRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#uniqueConnectorId.
    def visitUniqueConnectorId(self, ctx:PC4Parser.UniqueConnectorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#uniqueId.
    def visitUniqueId(self, ctx:PC4Parser.UniqueIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#sourceId.
    def visitSourceId(self, ctx:PC4Parser.SourceIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#targetId.
    def visitTargetId(self, ctx:PC4Parser.TargetIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#sentence.
    def visitSentence(self, ctx:PC4Parser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#name.
    def visitName(self, ctx:PC4Parser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#location.
    def visitLocation(self, ctx:PC4Parser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PC4Parser#viewKeyword.
    def visitViewKeyword(self, ctx:PC4Parser.ViewKeywordContext):
        return self.visitChildren(ctx)



del PC4Parser
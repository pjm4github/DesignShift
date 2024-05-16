from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream, tree

import json

from ShiftJson import parse_tree_to_json, clean_json_tree, remove_backslashes
from gen.StructurizrLexer import StructurizrLexer
from gen.StructurizrListener import StructurizrListener
from gen.StructurizrParser import StructurizrParser


from pathlib import Path
DOWNLOADS_PATH = str(Path.home()/"Downloads")
OUTPUT_PATH = str("./scratch")

import logging
logger = logging.getLogger(__name__)


class DesignShiftListener(StructurizrListener):
    def __init__(self):
        super().__init__()
        self.running_dict = {}
        # The list of all subcomponents that are collected across the walker.
        # Every exit module should collect the items below it and set the body_list to and empty list
        self.body_list = []

    def exitWorkspace(self, ctx:StructurizrParser.WorkspaceContext):
        # Example usage:
        json_tree = parse_tree_to_json(ctx)
        cleaned_json_tree = clean_json_tree(json_tree)
        super_clean_json = remove_backslashes(cleaned_json_tree)
        print(json.dumps(cleaned_json_tree, indent=2))
        with open(f"{OUTPUT_PATH}/super_clean_json.json", "w") as json_file:
            json.dump(super_clean_json, json_file, indent=2)

    #
    # def exitNamespace(self, ctx):
    #     self.running_dict['name'] = ctx.getText()
    #
    # def exitDescription(self, ctx):
    #     self.running_dict['description'] = ctx.getText()
    #
    # def exitLocation(self, ctx:StructurizrParser.LocationContext):
    #     self.running_dict['location'] = ctx.getText()
    #
    # def exitTags(self, ctx:StructurizrParser.TagsContext):
    #     self.running_dict['tags'] = ctx.getText()
    #
    # def exitElements(self, ctx:StructurizrParser):
    #     self.running_dict['elementView'] = {'id': "", 'x': 0, 'y': 0}
    #
    # def exitComponent_body(self, ctx:StructurizrParser.Component_bodyContext):
    #     accum_dict = {}
    #     count = len(ctx.children)
    #     for i, child in enumerate(ctx.children):
    #         print(child.getText())
    #
    #     self.running_dict['component_body'] = accum_dict
    #
    # def exitInfrastructureNode_body(self, ctx):
    #
    #     count = len(ctx.children)
    #     for i, child in enumerate(ctx.children):
    #         print(child.getText())
    #     self.running_dict['infrastructureNode_body'] = {'description': self.running_dict.get('description'),
    #                                                     'tags': self.running_dict.get('tags')}
    #     self.running_dict.pop('description', None)
    #     self.running_dict.pop('tags', None)
    #     print(json.dumps(self.running_dict, indent=4))
    #
    # def exitInfrastructureNode(self, ctx ):
    #     key = 'infrastructureNode'
    #     id = ''
    #     name = ''
    #     for c in ctx.children:
    #         print(type(c))
    #         if type(c) == StructurizrParser.IdentifierContext:
    #             id = c.children[0].getText()
    #         elif type(c) == tree.Tree.TerminalNodeImpl:
    #             if key != c.getText():
    #                 print("wrong key detected")
    #         elif type(c) == StructurizrParser.NameContext:
    #             name = c.getText()
    #
    #     self.running_dict['infrastructureNode'] = {'id': id,
    #                                                'name': name,
    #                                                'technology': '',
    #                                                "url": "",
    #                                                "properties": {},
    #                                                "perspectives": [],
    #                                                "relationships": [],
    #                                                }
    #     for k in self.running_dict.get('infrastructureNode_body', {}).keys():
    #         self.running_dict['infrastructureNode'][k] = self.running_dict['infrastructureNode_body'][k]
    #     print(json.dumps(self.running_dict, indent=4))
    #
    # # Exit a parse tree produced by StructurizrParser#container_body.
    # def exitContainer_body(self, ctx:StructurizrParser.Container_bodyContext):
    #     print("Exiting DesignShiftListener:exitContainer_body")
    #     pass
    # def exitModel(self, ctx:StructurizrParser.ModelContext):
    #     print("Exiting DesignShiftListener:")
    #     print(f"    grammar rule: {StructurizrParser.ruleNames[ctx.getRuleIndex()]}")
    #     json_tree = parse_tree_to_json(ctx)
    #     json.dumps(json_tree)
    #
    #     count = len(ctx.children)
    #     for i, child in enumerate(ctx.children):
    #         try:
    #             print(f"        grammar rule name {i}/{count} {StructurizrParser.ruleNames[child.getSymbol().tokenIndex]}")
    #             rule_index = child.getRuleIndex()
    #             if rule_index:
    #                 rule_name = StructurizrParser.ruleNames[rule_index]
    #                 print(f"        grammar rule {i}/{count}: {rule_name}")
    #         except AttributeError:
    #             print(f"        grammar rule {i}/{count}: None")
    #         try:
    #             left_child = child.getChild(0)
    #             if left_child:
    #                 rule_index = left_child.getRuleIndex()
    #                 rule_name = StructurizrParser.ruleNames[rule_index]
    #                 print(f"            <<< left_child: {rule_name}")
    #         except AttributeError:
    #             print(f"            <<< child has no left rule_index")
    #         try:
    #             right_child = child.getChild(1)
    #             if right_child:
    #                 rule_index = right_child.getRuleIndex()
    #                 rule_name = StructurizrParser.ruleNames[rule_index]
    #                 print(f"            >>> right_child: {rule_name}")
    #         except AttributeError:
    #             print(f"            >>> child has no right rule_index")

def parse_structurizr(filename):
    with open(filename, "r") as file:
        # Create an InputStream object using the file
        # Read the entire file into a string
        input_text = file.read()
        input_stream = InputStream(input_text)

        lexer = StructurizrLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = StructurizrParser(stream)
        tree = parser.workspace()

        listener = DesignShiftListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)


logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    logger.debug("Testing Structurizr")
    structurizer_file = './dsl/amazon.dsl'
    parse_structurizr(structurizer_file)

    logger.setLevel(logging.DEBUG)


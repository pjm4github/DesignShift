import os

from ShiftArchi import build_archi_xml

import pandas as pd

import json

def dump_csv(jf, csv_file_name):
    if type(jf) == str:
        if os.path.exists(jf):
            # Read JSON into DataFrame
            with open(jf) as f:
                json_file = json.load(f)
                df = pd.json_normalize(json_file)
                df.to_csv(csv_file_name, index=False)
    elif type(jf) == dict or type(jf) == list:
        df = pd.json_normalize(jf)
        # Write DataFrame to CSV
        df.to_csv(csv_file_name, index=False)

def convert_json_to_standard_form(key, json_dict):
    """
    Cleans the json file and converts it to the structurizer template form. Each of these forms is processed in
    the order they are defined in this code. This allows the nested, hierarchical structure to be properly formed.
    :param key: The key name of the section to process. For example key="Branding" will cause the branding
                 section to be normallized.
    :param json_dict:
    :return: The standard form dictionary of the form to
    """
    pass
    # Branding
    # Branding = {
    #     "logo": "A Base64 data URI representation of a PNG/JPG/GIF file.",
    #     "font": {
    #       "name": "Times New Roman",
    #       "url": "https://archive.ics.uci.edu/ml",
    #     }
    # }

    if key == "Branding":
        print("process branding")
    # ElementStyle
    # User
    # HttHealthCheck
    # Perspective
    # Dimension
    # AutomaticLayout
    # FilteredView
    # ImageView
    # ElementView
    # Vertex
    # RelationshipView
    # DocumentationSection
    # Decision
    # Image
    # Terminology
    # Relationship
    # AnimationStep
    # SystemLandscapeView
    # SystemContextView
    # ContainerView
    # ComponentView
    # DynamicView
    # DeploymentView
    # Configuration
    # Views
    # WorkspaceConfiguration
    # Documentation
    # APIResponse
    # Component
    # Container
    # Person
    # InfrastructureNode
    # SoftwareSystemInstance
    # ContainerInstance
    # DeploymentNode
    # SoftwareSystem
    # Model
    # Workspace


def remove_backslashes(d):
    if isinstance(d, list):
        new_list = []
        for item in d:
            new_item = remove_backslashes(item)
            new_list.append(new_item)
        return new_list
    elif isinstance(d, str):
        d = d.replace('\\"', '"')
        return d
    elif isinstance(d, dict):
        for key, value in d.items():
            if isinstance(value, str):
                if value[0] == '"':
                    value = value[1:]
                if value[-1] == '"':
                    value = value[:-1]
                d[key] = value
            else:
                d[key] = remove_backslashes(value)
    return d

def parse_tree_to_json(ctx):
    if ctx.getChildCount() == 0:
        # Leaf node, return token text
        return ctx.getText()
    else:
        # Non-leaf node, construct JSON object
        key = ctx.__class__.__name__.replace('Context', '')
        key = f"{key[0].lower()}{key[1:]}"
        node = {
            key: []
        }
        for i in range(ctx.getChildCount()):
            child_ctx = ctx.getChild(i)
            return_dict = parse_tree_to_json(child_ctx)
            # if type(return_dict) == dict:
            #     key_name = list(return_dict.keys())[0]
            # else:
            #     key_name = f"child_{i}"
            # node[ctx.__class__.__name__][key_name] = return_dict
            if return_dict == "\n":
                print("skipping a newline")
            elif return_dict == key:
                # Skip the value thats the same as the keyword that is
                continue
            elif return_dict == "->":
                # Skip the RIGHTARROW lexical that is part of the relation
                continue
            else:
                if type(return_dict) == dict:
                    key_name = list(return_dict.keys())[0]
                    if key_name == "identifier":
                        return_dict = {
                            key_name: return_dict[key_name][0]  # Pull out the string which will be the ID
                        }
                    elif key_name in ["closeCurly", "openCurly"]:
                        # Skip these grammar items
                        continue
                    if not return_dict[key_name]:
                        # Get rid of all list items that are empty
                        continue
                node[key].append(return_dict)
        if len(node[key])==1:
            node[key] = node[key][0]
        return node

def clean_json_tree(json_item):
    if type(json_item) == list:
        temp = []
        for item in json_item:
            new_temp = clean_json_tree(item)
            temp.append(new_temp)
        json_item = temp
        return json_item
    elif type(json_item) == dict:
        new_key = list(json_item.keys())[0]
        if new_key.find("_body") > 0:
            new_json_item = json_item.pop(new_key)
            recurse_json_item = clean_json_tree(new_json_item)
            return recurse_json_item
        else:
            json_item[new_key] = clean_json_tree(json_item[new_key])
            return json_item
    else:
        return json_item

import yaml
import json
# This generates an example file of the standard json file that should be produced if the
# structurizer file is parsed.
# This standard file is modified slightly to differentiate the body contents of the grammar from the
# properties grammar keyword.
def yaml_to_json_schema(yaml_file):
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    schema = {}

    def process_node(node, schema_node):
        if isinstance(node, dict):
            for key, value in node.items():
                schema_node[key] = {}
                process_node(value, schema_node[key])
        elif isinstance(node, list) and len(node) > 0:
            schema_node['type'] = 'array'
            schema_node['items'] = {}
            process_node(node[0], schema_node['items'])
        else:
            schema_node['type'] = 'string'

    process_node(yaml_data, schema)
    return schema

def generate_example_json(yaml_file):
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    return yaml_data

def main():
    yaml_file = 'Structurizr.yaml'
    json_schema = yaml_to_json_schema(yaml_file)

    with open('structurizr_schema.json', 'w') as file:
        yaml.safe_dump(json_schema, file, default_flow_style=False)

    # Generate example JSON
    example_json = generate_example_json(yaml_file)
    with open('structurizr_example.json', 'w') as file:
        json.dump(example_json, file, indent=2)

    print("JSON schema generated successfully.")

if __name__ == "__main__":
    main()
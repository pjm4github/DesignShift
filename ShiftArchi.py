

def build_archi_xml(fid, mname, elems, rels, orgs, view_iname, view_comps, vname):
    """
    :param fid: Model identifier name, example: 'id-1234'
    :param mname: Model name, example: 'The Architecture Context Diagram'
    :param elems: Dictionary of elements used for this model, example:
                elems = [{'type': "BusinessActor",
                         'identifier': "actor-1",
                         'name': "Customer",
                         'documentation': "Any person who purchases books from the Online Bookstore."}, ...]

    :param rels:  Dictionary of relations used for this model, example:
                 rels = [{'type': "Association",
                          'identifier': "rel-1",
                          'source': "app-1",
                          'target': "actor-1",
                          'documentation': "Allows customers to browse, search, and buy books."}, ...]

    :param orgs: Dictionary of organizations used for this model , example:
                 orgs = [{'label': 'Application'
                          'identifier': ["app-1", "ext-1"]}, ...]

    :param view_iname: A string, exmaple:  "view-1"
    :param view_comps: Dictionary of view components used for this model, example:
                 view_comps = [  {'type': 'element',
                                  'id': "id-instance2"
                                  'ref': "actor-1"
                                  'box': {'x': 312, 'y': 216, 'w': 120, 'h': 55}, ...

                                {'type': 'relationship',
                                 'id': "id-connector1"
                                 'ref': "rel-2"
                                 'source': "id-instance1"
                                 'target': id-instance3"} ]
    :param vname: A string, example "Context"
    :return: A serialized xml string of the xml file.
    """
    xml_header_line = [f'<?xml version="1.0" encoding="UTF-8"?>']
    xml_model_lines1 = [f'<model xmlns="http://www.opengroup.org/xsd/archimate/3.0/"',
                        f'    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
                        f'    xsi:schemaLocation="http://www.opengroup.org/xsd/archimate/3.0/ http://www.opengroup.org/xsd/archimate/3.0/archimate3_Diagram.xsd"',
                        f'    identifier="{fid}">',
                        f'  <name xml:lang="en">{mname}</name>']

    xml_elements_lines = ['  <elements>']

    for element in elems:
        xml_elements_lines.append(f"    <element xsi:type=\"{element['type']}\" identifier=\"{element['identifier']}\">")
        xml_elements_lines.append(f"      <name>{element['name']}</name>")
        xml_elements_lines.append(f"      <documentation>{element['documentation']}</documentation>")
        xml_elements_lines.append(f"     </element>")

    xml_elements_lines.append(f"  </elements>")

    # <elements>
    #   <element xsi:type="BusinessActor" identifier="actor-1">
    #   <name>Customer</name>
    #            <documentation>Any person who purchases books from the Online Bookstore.</documentation>
    #   </element>
    #   <element xsi:type="BusinessActor" identifier="actor-2">
    #     <name>Admin</name>
    #     <documentation>Administrator who manages the Online Bookstore application.</documentation>
    #   </element>
    #
    #   <element xsi:type="ApplicationComponent identifier="app-1">
    #      <name>Online Bookstore</name>
    #      <documentation>A web application allowing users to buy books and manage their purchases.</documentation>
    #    </element>
    #
    #    <element xsi:type="ApplicationComponent" identifier="ext-1">
    #      <name>Payment Gateway</name>
    #      <documentation>Third-party service that processes payments.</documentation>
    #    </element>
    # </elements>
    xml_relationships_lines = ['  <!-- Relationships -->']
    if len(rels) > 0:
        xml_relationships_lines = ['  <relationships>']

        for relationship in rels:
            xml_relationships_lines.append(f"    <relationship xsi:type=\"{relationship['type']}\" "
                                           f"identifier=\"{relationship['identifier']}\" "
                                           f"source=\"{relationship['source']}\" target=\"{relationship['target']}\">")
            # xml_relationships_lines.append(f"    <name>{relationship['name']}</name>")
            xml_relationships_lines.append(f"        <documentation>{relationship['documentation']}</documentation>")
            xml_relationships_lines.append(f"    </relationship>")
        xml_relationships_lines.append('  </relationships>')

    # <relationships>
    #   <relationship xsi:type="Association" identifier="rel-1" source="app-1" target="actor-1">
    #     <documentation>Allows customers to browse, search, and buy books.</documentation>
    #   </relationship>
    #   <relationship xsi:type="Association" identifier="rel-2" source="app-1" target="actor-2">
    #     <documentation>Provides system management and report generation capabilities.</documentation>
    #   </relationship>
    #   <relationship xsi:type="Association" identifier="rel-3" source="app-1" target="ext-1">
    #     <documentation>Handles all payment transactions securely.</documentation>
    #   </relationship>
    # </relationships>


    xml_organizations_lines = ["  <organizations>"]

    for org_item in orgs:
        xml_organizations_lines.append("    <item>")
        # <organizations>
        # <item>

        xml_organizations_lines.append(f"      <label xml:lang=\"en\">{org_item['label']}</label>")
        # <label xml:lang="en">Business</label>
        for item_id in org_item['identifier']:
            xml_organizations_lines.append(f"      <item identifierRef=\"{item_id}\" />")

            # <item identifierRef="actor-1" />
            # <item identifierRef="actor-2" />
        xml_organizations_lines.append("    </item>")
        #
        # </item>
        # <item>
        #     <label xml:lang="en">Application</label>
        #     <item identifierRef="app-1" />
        #     <item identifierRef="ext-1" />
        # </item>
        # <item>
        #     <label xml:lang="en">Relations</label>
        #     <item identifierRef="rel-2" />
        #     <item identifierRef="rel-1" />
        #     <item identifier Ref="rel-3" />
        # </item>
        # <item>

    xml_organizations_lines.append("  </organizations>")
    # </organizations>
    xml_views_lines1 = ['  <views>']

    xml_diagram_lines = ['    <diagrams>',
                         f"      <view xsi:type=\"Diagram\" identifier=\"{view_iname}\">",
                         f"        <name>{vname}</name>"]
    # <diagrams>

    for component in view_comps:
        if component['type'] == 'element':
            xml_diagram_lines.append(f"        <node identifier=\"{component['id']}\" "
                                     f"elementRef=\"{component['ref']}\" xsi:type=\"Element\" "
                                     f"x=\"{component['box']['x']}\" y=\"{component['box']['y']}\" "
                                     f"w=\"{component['box']['w']}\" h=\"{component['box']['h']}\"></node>")
        elif component['type'] == 'relationship':
            xml_diagram_lines.append(f"        <connection identifier=\"{component ['id']}\" "
                                     f"relationshipRef=\"{component['ref']}\" xsi:type=\"Relationship\" "
                                     f"source=\"{component['source']}\" target=\"{component['target']}\"></connection>")
            # <node identifier="id-instance2" element Ref="actor-1" xsi:type="Element" x="312" y="216" w="120" h="55"></node>
            # <node identifier="id-instance3" elementRef="actor-2" xsi:type="Element" x="516" y="72" w="120" h="55"></node>
            # <node identifier="id-instance4" elementRef="ext-1" xsi:type="Element" x="132" y="270" w="120" h="55"></node>
            # <connection identifier="id-connector1" relationship Ref="rel-2" xsi:type="Relationship" source="id-instance1" target="id-instance3"></connection>
            # <connection identifier="id-connector2" relationship Ref="rel-1" xsi:type="Relationship" source="id-instance1" target="id-instance2"></connection> # <connection identifier="id-connector 3" relationship Ref="rel-3" xsi:type="Relationship" source="id-instance1" target="id-instance4"></connection>
        else:
            print(f"Unhandled component type: {component ['type']}")

    xml_diagram_lines.append('      </view>')
    xml_diagram_lines.append('    </diagrams>')
    xml_views_lines2 = ['  </views>']
    xml_model_lines2 = ['</model>']

    # Put it all together
    xml_lines = xml_header_line
    xml_lines.extend(xml_model_lines1)
    xml_lines.extend(xml_elements_lines)
    xml_lines.extend(xml_relationships_lines)
    xml_lines.extend(xml_organizations_lines)
    xml_lines.extend(xml_views_lines1)
    xml_lines.extend(xml_diagram_lines)
    xml_lines.extend(xml_views_lines2)
    xml_lines.extend(xml_model_lines2)
    xml_string = '\n'.join(xml_lines)
    return xml_string


if __name__ == "__main__":
    file_id = 'id-1234'
    model_name = 'Online Bookstore Context Diagram'
    elements = [{'type': "BusinessActor", 'identifier': "actor-1", 'name': 'Customer',
                 'documentation': 'Any person who purchases books from the Online Bookstore.'},
                {'type': "BusinessActor", 'identifier': "actor-2", 'name': 'Admin',
                 'documentation': 'Administrator who manages the Online Bookstore application. '},
                {'type': "ApplicationComponent", 'identifier': "app-1", 'name': 'Online Bookstore',
                 'documentation': 'A web application allowing users to buy books and manage their purchases.'},
                {'type': "ApplicationComponent", 'identifier': "ext-1", 'name': 'Payment Gateway',
                 'documentation': 'Third-party service that processes payments. '},
                ]
    relationships = [{'type': "Association", 'identifier': "rel-1", 'source': "app-1", 'target': "actor-1",
                      'documentation': 'Allows customers to browse, search, and buy books. '},
                     {'type': "Association", 'identifier': "rel-2", 'source': "app-1", 'target': "actor-2",
                      'documentation': 'Provides system management and report generation capabilities. '},
                     {'type': "Association", 'identifier': "rel-3", 'source': "app-1", 'target': "ext-1",
                      'documentation': 'Handles all payment transactions securely.'},
                     ]


    organizations = [
        {'label': 'Business', 'identifier': ["actor-1", "actor-2"]},
        {'label': 'Application', 'identifier': ["app-1", "ext-1"]},
        {'label': 'Relations', 'identifier': ["rel-1", "rel-2", "rel-3"]},
        {'label': 'Views', 'identifier': ["view-1"]}
    ]
    view_instance_name = "view-1"

    diagram_view_components = [{'type': 'element', 'id': 'id-instance1', 'ref': 'app-1',
                                'box': {'x': 72, 'y': 60, 'w': 120, 'h': 55}},
                               {'type': 'element', 'id': 'id-instance2', 'ref': 'actor-1',
                                'box': {'x': 312, 'y': 216, 'w': 120, 'h': 55}},
                               {'type': 'element', 'id': 'id-instance3', 'ref': 'actor-2',
                                'box': {'x': 516, 'y': 72, 'w': 120, 'h': 55}},
                               {'type': 'element', 'id': 'id-instance4', 'ref': 'ext-1',
                                'box': {'x': 132, 'y': 270, 'w': 120, 'h': 55}},
                               {'type': 'relationship', 'id': 'id-connector1', 'ref': 'rel-2',
                                'source': 'id-instance1', 'target': 'id-instance3'},
                               {'type': 'relationship', 'id': 'id-connector2', 'ref': 'rel-1',
                                'source': 'id-instance1', 'target': 'id-instance2'},
                               {'type': 'relationship', 'id': 'id-connector3', 'ref': 'rel-3',
                                'source': 'id-instance1', 'target': 'id-instance4'}, ]


    view_name = "Context View"


    s = build_archi_xml(file_id, model_name, elements, relationships, organizations, view_instance_name, diagram_view_components, view_name)
    print(s)
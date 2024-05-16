// converted from the YAML file
// https://raw.githubusercontent.com/structurizr/json/master/structurizr.yaml
// openapi: 3.0.0
// info:
//  version: 1.29.0
//  title: Structurizr
//  description: The web API for Structurizr.

// Look here for the DSL definition
// https://docs.structurizr.com/dsl

// Here is apointer to teh swagger docs
// https://editor.swagger.io/?url=https://raw.githubusercontent.com/structurizr/json/master/structurizr.yaml

// Parser rules
grammar Structurizr;

//structurizr: workspace| named_workspace| workspace_extension;


// Workspace
// https://docs.structurizr.com/dsl/
// Represents a Structurizr workspace, which is a wrapper for a software architecture model, views, and documentation.
workspace: (bangs | NEWLINE)* WORKSPACE ('extends' URLTEXT |name description?)? openCurly workspace_body* closeCurly NEWLINE*;
//workspace_body: configuration | model | views | bangs | properties | NEWLINE;
workspace_body: properties |
                bangs |
//                bang_docs |
//                bang_adrs |
//                bang_identifiers |
//                bang_plugin |
                NAMENAME name NEWLINE |
                DESCRIPTION description NEWLINE |
                model |
                views |
                configuration |
//                thumbnail | // swagger docs show a thumbnail child here
//                documentation | // swagger docs show a properties child here
                NEWLINE;

// workspace is the entry point for the grammar
// https://docs.structurizr.com/dsl/
//named_workspace: 'workspace' name description? '{' (properties | identifier | docs | adrs
//                                                                              | model | views | configuration)+ '}';
//workspace_extension: 'workspace' 'extends' (file | uri) '{' (properties | identifier | docs | adrs
//                                                                              | model | views | configuration)+ '}';

// Model
// https://docs.structurizr.com/dsl/language#model
model: MODEL (name description?)? openCurly model_body* closeCurly NEWLINE;
//model_body: person | softwareSystem | relationship | group | deploymentEnvironment | properties | customElement | NEWLINE;
model_body: bang_identifiers |
            bang_ref |
            properties |
            group |
            person |
            softwareSystem |
            deploymentEnvironment |
            customElement |
            relationship |  // the specification says this should be RIGHTARROW relationship
            NEWLINE;

// Person
// A person who uses a software system.
// https://docs.structurizr.com/dsl/language#person
person : identifier? PERSON name (description tags?)? (openCurly person_body* closeCurly)? NEWLINE;
person_body: DESCRIPTION description NEWLINE |
             TAGS tags NEWLINE |
             url NEWLINE |
//             location | //swagger docs
//             group | //swagger docs
             properties |
             perspectives |
             relationship |
             NEWLINE;
// URLTEXT NEWLINE | location NEWLINE | group | properties | perspectives | relationships NEWLINE | NEWLINE;

// SoftwareSystem
// Software system may contain containers
// https://docs.structurizr.com/dsl/language#softwaresystem
softwareSystem:  identifier? SOFTWARESYSTEM name (description tags?)? (openCurly softwareSystem_body* closeCurly)? NEWLINE;
softwareSystem_body: bang_docs |
                     bang_adrs |
                     bang_ref |
                     bang_extend |
                     group |
                     container |
//                     documentation | // swagger docs
                     DESCRIPTION description NEWLINE |
//                     location | // swagger
                     TAGS tags NEWLINE |
                     url NEWLINE |
                     properties |
                     perspectives |
                     relationship |
                     NEWLINE;

// Container
// Containers may contain components
// A container (something that can execute code or host data).
// https://docs.structurizr.com/dsl/language#container
container: identifier? CONTAINER name (description (technology tags?)?)? (openCurly container_body* closeCurly)? NEWLINE;
container_body: bang_docs |
                bang_adrs |
                group |
                component |
                DESCRIPTION description NEWLINE |
                technology NEWLINE |
                TAGS tags NEWLINE |
                url NEWLINE |
                properties |
                perspectives |
                relationship |
                NEWLINE;

// Component
// A component (a grouping of related functionality behind an interface that runs inside a container).
// https://docs.structurizr.com/dsl/language#component
component: identifier? COMPONENT name (description (technology tags?)?)? (openCurly component_body* closeCurly)? NEWLINE;
component_body: bang_docs NEWLINE |
                bang_adrs NEWLINE |
                DESCRIPTION description NEWLINE |
                technology NEWLINE |
                TAGS tags NEWLINE |
                url NEWLINE |
                properties |
                perspectives |
                relationship |
                NEWLINE;

// DeploymentNode
// https://docs.structurizr.com/dsl/language#deploymentnode
deploymentNode: identifier? DEPLOYMENTNODE name (description (technology (tags (POSITIVE_INT | INSTANCES)?)?)?)? (openCurly deploymentNode_body* closeCurly)? NEWLINE;
deploymentNode_body: group |
                     deploymentNode |
                     infrastructureNode |
                     softwareSystemInstance |
                     containerInstance |
                     relationship |
                     DESCRIPTION description NEWLINE |
                     technology NEWLINE |
                     instances NEWLINE |
                     TAGS tags NEWLINE |
                     url NEWLINE |
                     properties |
                     perspectives |
                     NEWLINE;

// InfrastructureNode
// https://docs.structurizr.com/dsl/language#infrastructurenode
infrastructureNode: identifier? INFRASTRUCTURENODE name (description (technology tags?)?)? (openCurly infrastructureNode_body* closeCurly)? NEWLINE;
infrastructureNode_body: relationship |
                         DESCRIPTION description NEWLINE |
                         technology NEWLINE |
                         environment NEWLINE |  // "live" or "development" etc.
                         TAGS tags NEWLINE |
                         url NEWLINE |
                         properties |
                         perspectives |
                         NEWLINE;

// SoftwareSystemInstance
// https://docs.structurizr.com/dsl/language#softwaresysteminstance
softwareSystemInstance: SOFTWARESYSTEMINSTANCE name (deploymentGroups tags?)? (openCurly softwareSystemInstance_body* closeCurly)? NEWLINE;
softwareSystemInstance_body: DESCRIPTION description NEWLINE |
                             TAGS tags NEWLINE |
                             relationship |
                             url NEWLINE |
                             properties |
                             perspectives |
                             healthCheck |
//                             softwareSystemId |
//                             instanceId |
                             environment NEWLINE |
                             NEWLINE;
// https://docs.structurizr.com/dsl/language#deploymentgroup
deploymentGroups: name (',' name)*;
deploymentGroup: identifier? DEPLOYMENTGROUP name NEWLINE;

// ContainerInstance
// https://docs.structurizr.com/dsl/language#containerinstance
containerInstance: identifier? CONTAINERINSTANCE name (deploymentGroups tags?)? (openCurly container_inst_body* closeCurly)? NEWLINE;
container_inst_body: DESCRIPTION description NEWLINE |
                     TAGS tags NEWLINE |
                     relationship |
                     url NEWLINE |
                     properties |
                     perspectives |
                     healthCheck |
//                     containerId |
//                     instanceId |
                     environment NEWLINE |
                     NEWLINE;

// HealthCheck
// https://docs.structurizr.com/dsl/language#healthcheck
healthCheck: 'healthCheck' name URLTEXT (interval timeout?)? NEWLINE;
interval: POSITIVE_INT;
timeout: POSITIVE_INT;

// Relationship
// https://docs.structurizr.com/dsl/language#relationship
// when the first name is missing, the source is implied by the scope.
relationship: name? RIGHTARROW name (description (technology tags?)?)? (openCurly relationship_body* closeCurly)? NEWLINE; //
relationship_body: TAGS tags NEWLINE |
                   url NEWLINE |
                   properties |
                   perspectives |
//                   containerId |
//                   instanceId |
                   environment NEWLINE |
                   NEWLINE;

// Perspective
// Structurizr supports the addition of arbitrary “perspectives” to elements and
// relationships in the software architecture model. The concept is an implementation
// of the perspectives you’ll see described in approaches such as Viewpoints and
// Perspectives (Eoin Woods and Nick Rozanski).
// https://docs.structurizr.com/dsl/language#perspectives
//perspectives{
//    <name> <description> [value]
//    ...
//}
perspectives: PERSPECTIVES openCurly perspectives_body* closeCurly NEWLINE;
perspectives_body: name description value? NEWLINE;

///////////////////////////////  VIEWS /////////////////////////////////
// Views
// https://docs.structurizr.com/dsl/language#views
views: VIEWS openCurly views_body* closeCurly NEWLINE;
views_body: systemLandscapeView |
            systemContextView |
            containerView |
            componentView |
            filteredView |
            relationshipView |
            elementView |
            dynamicView |
            deploymentView  |
            customView |
            imageView |
            styles |
            theme |
            themes |
            branding |
            terminology |
            properties |
            NEWLINE;

// SystemLandscapeView
// https://docs.structurizr.com/dsl/language#systemlandscape-view
systemLandscapeView: identifier? SYSTEMLANDSCAPE key? description? openCurly view_body* closeCurly NEWLINE;

view_body: include NEWLINE |
           exclude NEWLINE
           'order' value NEWLINE |
           title NEWLINE |
           properties |
           paperSize NEWLINE |
           DESCRIPTION description NEWLINE |
           dimensions NEWLINE |  // swagger
           automaticLayout NEWLINE |
           default NEWLINE |
           relationship |
           animation |
           theme |
           themes |
           NEWLINE;

paperSize: 'A6_Landscape' |
            'A5_Portrait' |
            'A5_Landscape' |
            'A4_Portrait' |
            'A4_Landscape' |
            'A3_Portrait' |
            'A3_Landscape' |
            'A2_Portrait' |
            'A2_Landscape' |
            'A1_Portrait' |
            'A1_Landscape' |
            'A0_Portrait' |
            'A0_Landscape' |
            'Letter_Portrait' |
            'Letter_Landscape' |
            'Legal_Portrait' |
            'Legal_Landscape' |
            'Slide_4_3' |
            'Slide_16_9' |
            'Slide_16_10';

// SystemContextView
// https://docs.structurizr.com/dsl/language#systemcontext-view
systemContextView: identifier? SYSTEMCONTEXT name (key description?)? openCurly view_body* closeCurly NEWLINE;
//systemContext_view_body: title NEWLINE | automaticLayout NEWLINE | properties | relationships NEWLINE | include NEWLINE |
//                         exclude NEWLINE | DESCRIPTION description NEWLINE | default NEWLINE | animation | NEWLINE;

// AutomaticLayout
automaticLayout: AUTOLAYOUT  ('tb'|'bt'|'lr'|'rl')? (rankSeparation nodeSeparation)?;
rankSeparation: POSITIVE_INT;
nodeSeparation: POSITIVE_INT;

default: 'default';
include: 'include' (IDENTIFIER | URLTEXT | '*')+; // TODO: This needs checking
exclude: 'exclude' IDENTIFIER+;


// ContainerView
//https://docs.structurizr.com/dsl/language#container-view
containerView: identifier? CONTAINER name? key? description? openCurly view_body* closeCurly NEWLINE;

// ComponentView
//https://docs.structurizr.com/dsl/language#component-view
componentView: identifier? COMPONENT name? key? description? openCurly view_body* closeCurly NEWLINE;

// FilteredView
// https://docs.structurizr.com/dsl/language#filtered-view
filteredView: 'filtered' key (include|exclude) tags (key description?)? openCurly filtered_body* closeCurly NEWLINE;
filtered_body: default NEWLINE |
               title NEWLINE |
               DESCRIPTION description NEWLINE |
               properties |
               NEWLINE;

// DynamicView
// https://docs.structurizr.com/dsl/language#dynamic-view
dynamicView: 'dynamic' ('*' | IDENTIFIER)? (key description?)? openCurly dynamicView_body* closeCurly NEWLINE;
dynamicView_body: relationship |
                  name |
                  DESCRIPTION description NEWLINE |
                  NEWLINE;

// DeploymentEnvironment
// https://docs.structurizr.com/dsl/language#deploymentenvironment
deploymentEnvironment: identifier? DEPLOYMENTENVIRONMENT name (key description?)? (openCurly dep_env_body* closeCurly)? NEWLINE;
dep_env_body: TAGS tags NEWLINE |
              deploymentNode |
              deploymentGroup |
              infrastructureNode |
              relationship |
              NEWLINE;

// DeploymentView
// https://docs.structurizr.com/dsl/language#deployment-view
deploymentView: identifier? DEPLOYMENT ('*' | IDENTIFIER) environment (key description?)? (openCurly deployment_view_body* closeCurly)? NEWLINE;
deployment_view_body: TAGS tags NEWLINE |
                      deploymentNode |
                      infrastructureNode |
                      relationship |
                      DESCRIPTION description NEWLINE |
                      include NEWLINE |
                      automaticLayout NEWLINE |
                      animation |
                      NEWLINE;

environment: name;

// ImageView
// https://docs.structurizr.com/dsl/language#image-view
// The public PlantUML (https://plantuml.com/plantuml),
// Mermaid (https://mermaid.ink), and Kroki (https://kroki.io) URLs may work,
// but (1) please be aware that you are sending information to a third-party service and
// (2) these public services may not correctly set the CORS headers
// required for image views to work (see the notes at Image views).
imageView: IMAGE ('*' | name) key? (openCurly imageView_body* closeCurly)? NEWLINE;
imageView_body: 'plantuml' URLTEXT NEWLINE |
                'mermaid' URLTEXT NEWLINE |
                'kroki' value URLTEXT NEWLINE | // (the format identifier included in the URL path; e.g. https://kroki.io/{format}/...)
                IMAGE URLTEXT NEWLINE |
                default NEWLINE |
                title NEWLINE |
                DESCRIPTION description NEWLINE |
                properties |
                NEWLINE;

// customElement
// https://docs.structurizr.com/dsl/language#element
customElement: ELEMENT name (description tags?)? openCurly custom_element_body* closeCurly NEWLINE;
custom_element_body: DESCRIPTION description NEWLINE | tags NEWLINE | properties | perspectives | relationship | NEWLINE;

// ElementView
// An instance of a model element (Person, Software System, Container or Component) in a View.
elementView: ELEMENTVIEW name (metadata (description tags?)?)? openCurly elementView_body* closeCurly NEWLINE;
elementView_body: include NEWLINE |
                  'id' IDENTIFIER NEWLINE |  // tag of the element thats affected by this view
                  'x' POSITIVE_INT NEWLINE | // The horizontal position of the element when rendered.
                  'y' POSITIVE_INT NEWLINE | // The vertical position of the element when rendered.
                  NEWLINE;

metadata: BOOLEAN;

// RelationshipView
relationshipView: RELATIONSHIP name (description tags?)? openCurly relationshipView_body* closeCurly NEWLINE;
relationshipView_body: 'target' tags NEWLINE |  // tag of the relationship thats affected by this view
                       DESCRIPTION description NEWLINE |
                       'response' BOOLEAN |
                       'order' POSITIVE_INT NEWLINE |
                       'verticies' array NEWLINE |
                       'routing' routingType NEWLINE |
                       'sourceConnector' POSITIVE_INT NEWLINE| // the "connector id" on the source element
                       'targetConnector' POSITIVE_INT NEWLINE| // the "connector id" on the target element
                       NEWLINE;

// Manual layout:
// https://docs.structurizr.com/ui/diagrams/manual-layout
// Convert the yaml file to json, then create a json schema file, then create a json schema checker


// Vertex
// The X, Y coordinate of a bend in a line.

//vertex: LBRACKET pair RBRACKET NEWLINE;
pair: POSITIVE_INT COMMA POSITIVE_INT ;

//array: '[' vertex ']' |  '[' vertex (';' vertex)* ']';

array : LBRACKET pair (SEMICOLON pair)* RBRACKET;

// AnimationStep
//more items to include: animations | order | softwareSystemId | paperSize | dimensions | automaticLayout | enterpriseBoundaryVisible | elements |

animation: 'animation' openCurly animation_body* closeCurly NEWLINE;
animation_body: IDENTIFIER+ NEWLINE;

// Dimensions
dimensions: 'dimensions' NUMBER NUMBER;

// WorkspaceConfiguration or Configuration
// https://docs.structurizr.com/dsl/language#configuration
configuration: CONFIGURATION openCurly configuration_body* closeCurly NEWLINE;
configuration_body: scope | visibility | users | properties | NEWLINE;

// Styles
// https://docs.structurizr.com/dsl/language#styles
styles: STYLES openCurly style_body* closeCurly NEWLINE;
style_body: elementStyle | relationshipStyle | NEWLINE;

// CustomView
customView: 'custom' (key (title description?)?)? openCurly custom_body* closeCurly NEWLINE;
custom_body: include NEWLINE |
             exclude NEWLINE |
             automaticLayout NEWLINE |
             default NEWLINE |
             animation |
             title NEWLINE |
             DESCRIPTION description NEWLINE |
             properties |
             NEWLINE;

// ElementStyle
elementStyle: ELEMENT tag openCurly element_style_body* closeCurly NEWLINE;
element_style_body: 'opacity' POSITIVE_INT NEWLINE |
                    'shape' shapetype NEWLINE |
                    'dashed' BOOLEAN NEWLINE |
                    'icon' URLTEXT NEWLINE |
                    'width' POSITIVE_INT NEWLINE |
                    'height' POSITIVE_INT NEWLINE |
                    'background' value NEWLINE | // <#rrggbb|color name>
                    'color' value NEWLINE | // <#rrggbb|color name>
                    'colour' value NEWLINE | // <#rrggbb|color name>
                    'stroke' value NEWLINE | // <#rrggbb|color name>
                    'strokeWidth' POSITIVE_INT NEWLINE | //: 1-10>
                    'fontSize' POSITIVE_INT NEWLINE |
                    'border' styleType NEWLINE |
                    'opacity' POSITIVE_INT NEWLINE | //: 0-100>
                    'metadata' BOOLEAN NEWLINE |
                    DESCRIPTION BOOLEAN NEWLINE |
                    properties |
                    NEWLINE;

shapetype:  ('Box' | 'box' | 'BOX')? |
            ('RoundedBox' |'roundedbox' |'ROUNDEDBOX')? |
            COMPONENT |
            ('Circle' |'circle' |'CIRCLE')? |
            ('Ellipse' |'ellipse' |'ELLIPSE')? |
            ('Hexagon' |'hexagon' |'HEXAGON')? |
            ('Diamond' |'diamond' |'DIAMOND')? |
            ('Folder' |'folder' |'FOLDER')? |
            ('Cylinder' |'cylinder' |'CYLINDER')? |
            ('Pipe' |'pipe' |'PIPE')? |
            ('WebBrowser' |'webbrowser' |'WEBBROWSER')? |
            ('Window' |'window' |'WINDOW')? |
            ('MobileDevicePortrait' |'mobiledeviceportrait' |'MOBILEDEVICEPORTRAIT')? |
            ('MobileDeviceLandscape' |'mobiledevicelandscape' 'MOBILEDEVICELANDSCAPE')? |
            PERSON|
            ('Robot'|'robot'|'ROBOT')?;

// RelationshipStyle
relationshipStyle: RELATIONSHIP tag openCurly rel_style_body* closeCurly NEWLINE;
rel_style_body: 'thickness' POSITIVE_INT NEWLINE |
                'color' value NEWLINE | // <#rrggbb|color name>
                'colour' value NEWLINE | // <#rrggbb|color name>
                //    'stroke' value NEWLINE | // <#rrggbb|color name>
                //    'strokeWidth' POSITIVE_INT NEWLINE | //: 1-10>
                'dashed' BOOLEAN NEWLINE |
                'style' styleType NEWLINE |
                'routing' routingType NEWLINE |
                'fontSize' POSITIVE_INT NEWLINE |
                'width' POSITIVE_INT NEWLINE |
                'position' POSITIVE_INT NEWLINE |
                'opacity' POSITIVE_INT NEWLINE |
                properties |
                // 'dashed' BOOLEAN NEWLINE |
                NEWLINE;

routingType: 'Direct' | 'Curved' | 'Orthogonal';

styleType: 'solid' | 'dashed' | 'dotted';

// Documentation
//      type: object
//      description: A wrapper for documentation.
//      properties:
//        sections:
//          type: array
//          items:
//            $ref: '#/components/schemas/DocumentationSection'
//        decisions:
//          type: array
//          items:
//            $ref: '#/components/schemas/Decision'
//        images:
//          type: array
//          items:
//            $ref: '#/components/schemas/Image'

// Markdown TODO: not impolemented yet
//// markdown
//elem
//@init {System.err.println(_input.LT(1));} //With predicates, it seems debugging the grammar helps where is normally does not.
//	:	header
//	|	para
//	|	quote
//	|	list
//	|	'\n'
//	;
//
//header : '#'+ ~'\n'* '\n' ;
//
//file:	'\n'* elem+ EOF ;
//
//para:	'\n'* paraContent '\n' (NEWLINE|EOF) ; // if \n\n, exists loop. if \n not \n, stays in loop.
//
//paraContent : (TEXT|bold|italics|link|astericks|underscore|{_input.LA(2)!='\n'&&_input.LA(2)!=Token.EOF}? '\n')+ ;
//
//bold:	'*' ~('\n'|' ') TEXT'*' ;
//
//astericks : {_input.LT(1).getCharPositionInLine()!=0}? WS '*' WS ;
//
//underscore : WS '_' WS ;
//
//italics : '_' ~('\n'|' ') TEXT '_' ;
//
//link : '[' TEXT ']' '(' ~')'* ')' ;
//
//quote : quoteElem+ NEWLINE ;
//
//quoteElem : {_input.LT(1).getCharPositionInLine()==0}? '>' ~'\n'* '\n' ;
//
//list:	listElem+ NEWLINE NEWLINE ;
//
//listElem : {_input.LT(1).getCharPositionInLine()==0}? (' ' (' ' ' '?)?)? '*' WS paraContent ;
//
////text:	~('#'|'*'|'>'|'['|']'|'_'|'\n')+ ;



// https://docs.structurizr.com/dsl/language#docs
// The !docs keyword can be used to attach
// Markdown/AsciiDoc documentation to the parent context (either the workspace, a software system, or a container).
// The path must be a relative path, located within the same directory as the parent file, or a subdirectory of it.
// For example:  !docs subdirectory
bang_docs: BANGDOCS path name? NEWLINE;

// Architecture Decision Records
// https://docs.structurizr.com/dsl/adrs.html#architecture-decision-records-adrs
// The !adrs keyword can be used to attach Markdown/AsciiDoc ADRs to the parent context
// (either the workspace, a software system, or a container).
// Because diagrams alone can’t express the decisions that led to a solution,
// Structurizr allows you to supplement your software architecture model with a decision log,
// captured as a collection of lightweight Architecture Decision Records (ADRs) as described by Michael Nygard,
// and featured on the ThoughtWorks Technology Radar. Structurizr allows you to publish your ADRs to allow team
// members get an “at a glance” view of the current set of ADRs, along with facilities to make navigating them easier.
bang_adrs: BANGADRS path name? NEWLINE;

// The !identifiers keyword can be used to modify the scope of identifiers.
// https://docs.structurizr.com/dsl/language#identifiers
bang_identifiers: BANGIDENTIFIERS ('hierarchical'| 'flat') NEWLINE;

// The !extend keyword provides a way to extend a previously defined element/relationship, and is designed to be used
// with the workspace extends or !include features. It can be used in a couple of ways.
// The first usage scenario is to extend an existing element/relationship that has been defined via the DSL.
// This allows you to extend the element referenced by the given identifier.
bang_extend: identifier? BANGEXTEND name (openCurly (model_body | softwareSystem_body)* closeCurly)? NEWLINE;
bang_impliedRelationships: BANGIMPLIEDRELATIONSHIPS BOOLEAN NEWLINE;

// The !ref keyword does the same as !extend, and may provide better readability when you
// just want to reference an element (e.g. when extending a JSON workspace) rather than extend it.
bang_ref: identifier? BANGREF name (openCurly  group_body* closeCurly)? NEWLINE;

bang_script: BANGSCRIPT (URLTEXT | name (openCurly bang_script_body* closeCurly)?) NEWLINE;
bang_script_body: name_value_pair | URLTEXT| STRING | NEWLINE; // TODO needs more work

bang_var: BANGVAR IDENTIFIER value NEWLINE;
bang_const: BANGCONST IDENTIFIER value NEWLINE;
bang_include: BANGINCLUDE (IDENTIFIER | URLTEXT) NEWLINE;
bang_plugin: BANGPLUGIN (URLTEXT | name) (openCurly bang_plugin_body* closeCurly)? NEWLINE;
bang_plugin_body: STRING STRING NEWLINE |
                  NEWLINE;

bangs: bang_docs |
       bang_adrs |
       bang_identifiers |
       bang_extend |
       bang_ref |
       bang_script |
       bang_const |
       bang_impliedRelationships |
       bang_var |
       bang_plugin |
       bang_include;

// DocumentationSection
//       type: object
//      description: A documentation section.
//      properties:
//        content:
//          type: string
//          description: The Markdown or AsciiDoc content of the section.
//        format:
//          type: string
//          description: The content format type.
//          enum:
//            - Markdown
//            - AsciiDoc
//        order:
//          type: number
//          format: integer
//          description: The order (index) of the section in the document.

// Decision
//     type: object
//      description: A decision record (e.g. architecture decision record).
//      properties:
//        id:
//          type: string
//          description: The ID of the decision.
//        date:
//          type: string
//          description: The date that the decision was made (ISO 8601 format).
//        status:
//          type: string
//          description: The status of the decision.
//          enum:
//            - Proposed
//            - Accepted
//            - Superseded
//            - Deprecated
//            - Rejected
//        title:
//          type: string
//          description: The title of the decision.
//        content:
//          type: string
//          description: The Markdown or AsciiDoc content of the section.
//        format:
//          type: string
//          description: The content format type.
//          enum:
//            - Markdown
//            - AsciiDoc
//        elementId:
//          type: string
//          description: The ID of the element (in the model) that this decision applies to (optional).


// Expressions  TODO: Not implemented yet
// https://docs.structurizr.com/dsl/expressions#expressions
// expression: '->' (identifier| expression); // others below

//-><identifier|expression>: the specified element(s) plus afferent couplings
//<identifier|expression>->: the specified element(s) plus efferent couplings
//-><identifier|expression>->: the specified element(s) plus afferent and efferent couplings
//element.type==<type>: elements of the specified type (Person, SoftwareSystem, Container, Component, DeploymentNode, InfrastructureNode, SoftwareSystemInstance, ContainerInstance, Custom)
//element.parent==<identifier>: elements with the specified parent
//element.tag==<tag>[,tag]: all elements that have all of the specified tags
//element.tag!=<tag>[,tag]: all elements that do not have all of the specified tags
//element==-><identifier>: the specified element plus afferent couplings
//element==<identifier>->: the specified element plus efferent couplings
//element==-><identifier>->: the specified element plus afferent and efferent couplings
//Relationship expressions
//*->*: all relationships
//<identifier>->*: all relationships with the specified source element
//*-><identifier>: all relationships with the specified destination element
//relationship==*: all relationships
//relationship==*->*: all relationships
//relationship.tag==<tag>[,tag]: all relationships that have all of the specified tags
//relationship.tag!=<tag>[,tag]: all relationships that do not have all of the specified tags
//relationship.source==<identifier>: all relationships with the specified source element
//relationship.destination==<identifier>: all relationships with the specified destination element
//relationship==<identifier>->*: all relationships with the specified source element
//relationship==*-><identifier>: all relationships with the specified destination element
//relationship==<identifier>-><identifier>: all relationships between the two specified elements

// URI TODO: Not implemented yet
//uri: scheme '://' login? host (':' port)? ('/' path?)? query? frag? WS? ;
//scheme: string ;
//host: '/'? hostname;
//hostname
//    : string         # DomainNameOrIPv4Host
//    | '[' v6host ']' # IPv6Host
//    ;
//v6host: '::'? (string | DIGITS) ((':' | '::') (string | DIGITS))*;
//port: DIGITS;
//path: string ('/' string)* '/'?;
//user: string;
//login: user (':' password)? '@';
//password: string;
//frag: '#' (string | DIGITS);
//query: '?' search;
//search: searchparameter ('&' searchparameter)*;
//searchparameter: string ('=' (string | DIGITS | hex))?;
//string: STRING;
//hexDigits : HEX_DIGIT+ ;   // One or more hexadecimal digits.
//hex : HEX_PREFIX hexDigits ;



// Terminology
// https://docs.structurizr.com/dsl/language#terminology
terminology: 'terminology' openCurly terminology_body* closeCurly NEWLINE;
terminology_body: keywords IDENTIFIER NEWLINE;

// User
users: USERS openCurly users_body* closeCurly NEWLINE;
users_body: URLTEXT ('read'|'write') NEWLINE;

// APIResponse
//  type: object
//      description: An API response.
//      properties:
//        success:
//          type: boolean
//          description: 'true if the API call was successful, false otherwise.'
//        message:
//          type: string
//          description: 'A human readable response message.'
//        revision:
//          type: integer
//          description: 'The internal revision number.'

// The scope keyword can be used to set the workspace scope.
// https://docs.structurizr.com/dsl/language#scope
scope: 'scope' ('landscape' | SOFTWARESYSTEM | 'none') NEWLINE;
visibility: 'visibility' ('private' | 'public') NEWLINE;

// Themes
// https://docs.structurizr.com/dsl/language#themes
themes: 'themes' URLTEXT URLTEXT* NEWLINE;

theme: 'theme' ('default' | URLTEXT) NEWLINE;
// default is short for https://static.structurizr.com/themes/default/theme.json

// Branding
// https://docs.structurizr.com/dsl/language#branding
// branding {
//    logo <file|url>
//    font <name> [url]
//   }
branding: 'branding' openCurly branding_body* closeCurly NEWLINE;
branding_body: 'logo' (name | URLTEXT) NEWLINE |
               'font' name URLTEXT NEWLINE |
               NEWLINE;


openCurly: '{' NEWLINE;
closeCurly: '}'; // NEWLINE+;

instances: 'instances' INSTANCE_STRING;

path: name;

name: IDENTIFIER | STRING | keywords| URLTEXT;

value: STRING | NUMBER | BOOLEAN | HEXNUMBER| IDENTIFIER | object | array;


object: '{' (STRING ':' value ';')* '}'; // A simplified version of an object

properties: 'properties' openCurly name_value_pair+ closeCurly NEWLINE;
name_value_pair: name value NEWLINE;

// See https://docs.structurizr.com/dsl/identifiers#identifier-scope
identifier: (IDENTIFIER | keywords) '=';

technology: IDENTIFIER | STRING;

tag: IDENTIFIER | STRING;

key: IDENTIFIER | STRING ;

description: IDENTIFIER | STRING ; // STRING | NAME;

// https://docs.structurizr.com/dsl/language#tags
// TODO: The second form of this tags grammar needs to be added and tested.
tags: STRING (','? STRING)*; // '"' IDENTIFIER (',' IDENTIFIER)* '"';

//description : 'description:' STRING ';';

title: 'title' STRING;

url : 'url' URLTEXT;
location : LOCATION_TYPE;
group : identifier? GROUP name (description tags?)? (openCurly group_body* closeCurly)? NEWLINE;
group_body: person | softwareSystem | container | NEWLINE;

//relationships : 'relationships' LBRACKET relationshipList? RBRACKET;

perspective : STRING;  // Simplified, assuming a reference to a perspective defined elsewhere

//relationshipList : relationship (',' relationship)*;

keywords: AUTOLAYOUT |
            COMPONENT |
            CONFIGURATION |
            CONTAINER |
            CONTAINERINSTANCE |
            DEPLOYMENT |
            DEPLOYMENTENVIRONMENT |
            DEPLOYMENTGROUP |
            DEPLOYMENTNODE |
            DESCRIPTION |
            ELEMENTVIEW |
            ELEMENT |
            GROUP |
            INFRASTRUCTURENODE |
            IMAGE |
            MODEL |
            PERSON |
            PERSPECTIVES |
            //RELATIONSHIPVIEW |
            RELATIONSHIP |
            SOFTWARESYSTEM |
            SOFTWARESYSTEMINSTANCE |
            STYLES |
            SYSTEMCONTEXT |
            SYSTEMLANDSCAPE |
            TAGS |
            USERS |
            VIEWS |
            WORKSPACE;

///////////////////////////////////////////////////////////////////////
// Lexer rules
///////////////////////////////////////////////////////////////////////
HEXNUMBER : '0x' [0-9a-fA-F]+ | '0X' [0-9a-fA-F]+ | '#' [0-9a-fA-F]+; // Match numbers prefixed with 0x or 0X or #

// Case insentitive keywords
//s = 'DEPLOYMENTENVIRONMENT';w = [f'[{x.upper()}{x.lower()}]' for x in s];print(f"{s.upper()}: {''.join(w)};")
BANGDOCS: '!'[Dd][Oo][Cc][Ss];
BANGADRS: '!'[Aa][Dd][Rr][Ss];
BANGIDENTIFIERS: '!'[Ii][Dd][Ee][Nn][Tt][Ii][Ff][Ii][Ee][Rr][Ss];
BANGEXTEND: '!'[Ee][Xx][Tt][Ee][Nn][Dd];
BANGREF: '!'[Rr][Ee][Ff];
BANGSCRIPT: '!'[Ss][Cc][Rr][Ii][Pp][Tt];
BANGCONST: '!'[Cc][Oo][Nn][Ss][Tt];
BANGINCLUDE: '!'[Ii][Nn][Cc][Ll][Uu][Dd][Ee];
BANGIMPLIEDRELATIONSHIPS: '!'[Ii][Mm][Pp][Ll][Ii][Ee][Dd][Rr][Ee][Ll][Aa][Tt][Ii][Oo][Nn][Ss][Hh][Ii][Pp][Ss];
BANGVAR: '!'[Vv][Aa][Rr];
BANGPLUGIN: '!'[Pp][Ll][Uu][Gg][Ii][Nn];

// Order of the LEXER items is important. Put the longer matches first
AUTOLAYOUT: [Aa][Uu][Tt][Oo][Ll][Aa][Yy][Oo][Uu][Tt];
COMPONENT: [Cc][Oo][Mm][Pp][Oo][Nn][Ee][Nn][Tt];
CONFIGURATION: [Cc][Oo][Nn][Ff][Ii][Gg][Uu][Rr][Aa][Tt][Ii][Oo][Nn];
CONTAINERINSTANCE: [Cc][Oo][Nn][Tt][Aa][Ii][Nn][Ee][Rr][Ii][Nn][Ss][Tt][Aa][Nn][Cc][Ee];
CONTAINER: [Cc][Oo][Nn][Tt][Aa][Ii][Nn][Ee][Rr];
DEPLOYMENTENVIRONMENT: [Dd][Ee][Pp][Ll][Oo][Yy][Mm][Ee][Nn][Tt][Ee][Nn][Vv][Ii][Rr][Oo][Nn][Mm][Ee][Nn][Tt];
DEPLOYMENTGROUP: [Dd][Ee][Pp][Ll][Oo][Yy][Mm][Ee][Nn][Tt][Gg][Rr][Oo][Uu][Pp];
DEPLOYMENTNODE: [Dd][Ee][Pp][Ll][Oo][Yy][Mm][Ee][Nn][Tt][Nn][Oo][Dd][Ee];
DEPLOYMENT: [Dd][Ee][Pp][Ll][Oo][Yy][Mm][Ee][Nn][Tt];
DESCRIPTION: [Dd][Ee][Ss][Cc][Rr][Ii][Pp][Tt][Ii][Oo][Nn];
ELEMENTVIEW: [Ee][Ll][Ee][Mm][Ee][Nn][Tt][Vv][Ii][Ee][Ww];
ELEMENT: [Ee][Ll][Ee][Mm][Ee][Nn][Tt];
GROUP: [Gg][Rr][Oo][Uu][Pp];
IMAGE: [Ii][Mm][Aa][Gg][Ee];
INFRASTRUCTURENODE: [Ii][Nn][Ff][Rr][Aa][Ss][Tt][Rr][Uu][Cc][Tt][Uu][Rr][Ee][Nn][Oo][Dd][Ee];
MODEL: [Mm][Oo][Dd][Ee][Ll];
PERSON: [Pp][Ee][Rr][Ss][Oo][Nn];
PERSPECTIVES: [Pp][Ee][Rr][Ss][Pp][Ee][Cc][Tt][Ii][Vv][Ee][Ss];
// RELATIONSHIPVIEW: [Rr][Ee][Ll][Aa][Tt][Ii][Oo][Nn][Ss][Hh][Ii][Pp][Vv][Ii][Ee][Ww];
RELATIONSHIP: [Rr][Ee][Ll][Aa][Tt][Ii][Oo][Nn][Ss][Hh][Ii][Pp];
SOFTWARESYSTEMINSTANCE: [Ss][Oo][Ff][Tt][Ww][Aa][Rr][Ee][Ss][Yy][Ss][Tt][Ee][Mm][Ii][Nn][Ss][Tt][Aa][Nn][Cc][Ee];
SOFTWARESYSTEM: [Ss][Oo][Ff][Tt][Ww][Aa][Rr][Ee][Ss][Yy][Ss][Tt][Ee][Mm];
STYLES: [Ss][Tt][Yy][Ll][Ee][Ss];
SYSTEMCONTEXT: [Ss][Yy][Ss][Tt][Ee][Mm][Cc][Oo][Nn][Tt][Ee][Xx][Tt];
SYSTEMLANDSCAPE: [Ss][Yy][Ss][Tt][Ee][Mm][Ll][Aa][Nn][Dd][Ss][Cc][Aa][Pp][Ee];
TAGS: [Tt][Aa][Gg][Ss];
USERS: [Uu][Ss][Ee][Rr][Ss];
VIEWS: [Vv][Ii][Ee][Ww][Ss];
WORKSPACE: [Ww][Oo][Rr][Kk][Ss][Pp][Aa][Cc][Ee];
NAMENAME: [Nn][Aa][Mm][Ee];

RIGHTARROW: '->';
BOOLEAN : 'true' | 'false' ;

LOCATION_TYPE : 'External' | 'Internal' | 'Unspecified';
INSTANCE_STRING: '"' [0-9.N]+ '"';

// Grab a POSITIVE_INT first so that it doesnt change into a number
POSITIVE_INT: DIGIT+ ;
INSTANCES: [0-9.N]+;
// A string can include anything between the quotes and even an escaped quote
STRING: '"' ( ~["\\] | '\\' . )* '"' | '\'' ( ~['\\] | '\\' . )* '\'' ;  // escape handling included
NUMBER: '-'? POSITIVE_INT ('.' POSITIVE_INT)? ; // Integer and floating-point

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;

LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);
// A space after the # sign denotes a comment
POUND_COMMENT: '# ' ~[\r\n]* -> channel(HIDDEN);
COMMENT: '/*' .*? '*/' -> channel(HIDDEN);

URLTEXT: [0-9a-zA-Z_()&</>!?.:\-{}]+ ;
LBRACKET  : '[' ;
RBRACKET  : ']' ;
SEMICOLON : ';' ;
COMMA     : ',' ;
fragment DIGIT: [0-9] ;

WS: [ \t\f]+ -> skip ; // channel(HIDDEN);

// New line appears here so it captures it last since it is used as a grammar component.
NEWLINE: '\r'? '\n' ;// Unix, Windows



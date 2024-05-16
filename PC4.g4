grammar PC4;

// Main entry point for parsing *.ds files
parse: (element | connector | legend | NEWLINE)+ EOF;

///////////////////// LEGEND //////////////////
// There must be at least one legend on a sheet to ensure that the sheet is parsed
//Legend: [Deployment View] "What is this view for".
//Legend: [System Landscape] "Some description". legend: Legend viewKeyword sentence NEWLINE;
legend: Legend viewKeyword sentence NEWLINE;

///////////////////// ELEMENT //////////////////
// Definition of a entity based on the provided pattern
// Element: "<b>Joe The Wonderkind</b> &NBSP; Again" [Person] "This person is cool" actor-1 10 100 100 2000 element: Element name elementKeyword relation uniqueId location? NEWLINE;
element: Element name elementKeyword relation uniqueId location? NEWLINE;

///////////////////// CONNECTOR //////////////////
// Definition of the connector between elements
// Connector: "Uses this component" ["technology is here"] rel-4 id-connector-1 actor-1 actor-3 connector: Connector relation catalog Relation unique ConnectorId sourceId targetId location? NEWLINE;
connector: Connector relation catalogRelation uniqueConnectorId sourceId targetId location? NEWLINE;

comment: LineComment;

elementKeyword: Person | User | Actor | Role | Existing_system | Software_system | Container;

// used only on the connectors between objects (the directed arrows)
relation: DESCRIPTION ('[' DESCRIPTION ']')?;

catalogRelation: 'rel-' DIGITS;

uniqueConnectorId: 'id-connector-' DIGITS;  // Identifier  "id-connector-1"
uniqueId: ('actor-' DIGITS) | ('ext-' DIGITS) | ('app-' DIGITS); // Identifier "actor-1", "app-1", "ext-1"
sourceId: uniqueId;
targetId: uniqueId;

// Optional name enclosed in curly braces
sentence: DESCRIPTION DESCRIPTION*;
name: DESCRIPTION;
//name: (IDENTIFIER (DIGITS)*)+;

//Keyword block with technology enclosed in square brackets
// keywordBlock: '[' elementKeyword (': '[' DESCRIPTION ']')? ']';

location: DIGITS DIGITS DIGITS DIGITS;

viewKeyword: SystemLandscapeView | SystemContextView | ContainerView | ComponentView
             | CodeView | ImageView | DynamicView | DeploymentView | FilteredView; // CustomView;

// Lexer rules for capturing name, technology, and description texts

Person: '[Person]';
User: '[User]';
Actor: '[Actor]';
Role: '[Role]';
Software_system: '[Software System]';
Existing_system: '[Existing System]';
Container: '[Container]';

Legend: 'Legend: ';
Connector: 'Connector:';
Element: 'Element: ';

SystemLandscapeView: '[System Landscape]';
SystemContextView: '[System Context]';
ContainerView: '[Container View]';
ComponentView: '[Component View]';
CodeView: '[Code View]';
ImageView: '[Image View]';
DynamicView: '[Dynamic View]';
DeploymentView: '[Deployment View]';
FilteredView: '[Filtered View]';

//IDENTIFIER: (LETTERS '-' DIGITS); // Identifier "actor-1"
DIGITS: [0-9]+;// Integer digits (includes location of the item in the drawing).
LETTERS: [a-zA-Z]+; // Simple rule for technology identifiers
SPECIALS: [_()&;</>,!?.]+;// Includes HTML type markers
TEXT: (DIGITS | LETTERS | SPECIALS)+;

DESCRIPTION: '"' (TEXT | WS) + '"'; // Descriptions can include spaces
NEWLINE: '\r'? '\n'; // Unix, Windows

// Comments start with // to the end of the line
LineComment: '//' ~[\r\n]* -> channel(HIDDEN);


// Spaces and tabs handling
WS : [ \t\f]+  -> channel(HIDDEN);
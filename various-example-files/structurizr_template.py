Branding = {
    "logo": "A Base64 data URI representation of a PNG/JPG/GIF file.",
    "font": {
      "name": "Times New Roman",
      "url": "https://archive.ics.uci.edu/ml",
    }
}

ElementStyle = {
    "tag": "Tag10",
    "width": 200,
    "height": 100,
    "background": "#ffffff",
    "stroke": "#000000",
    "strokeWidth": 10,
    "color": "#ff0000",
    "fontSize": 16,
    "shape": "Box",
    "icon": "",
    "border": "Solid",
    "opacity": 100,
    "metadata": False,
    "description": True
}

RelationshipStyle = {
    "tag": "StyleOwnerTag10",
    "thickness": 2,
    "color": "#ff0000",
    "fontSize": 16,
    "width": 200,
    "dashed": True,
    "routing": "Curved",
    "position": 50,
    "opacity": 100
}

User = {

    "username": "joe.blow@comany.com",
    "role": "ReadWrite",
}

HttpHealthCheck = {
    "name": "",
    "url": "https://archive.ics.uci.edu/ml",
    "interval": 0,
    "timeout": 0,
    "headers": {"name": "value"}
}

Perspective = {
    "name": "",
    "description": "",
    "value": ""
}

Dimensions = {
    "width": 100,
    "height": 200
}

AutomaticLayout = {
    "implementation": "Graphviz",
    "rankDirection": "TopBottom",
    "rankSeparation": 100,
    "nodeSeparation": 10,
    "edgeSeparation": 100,
    "vertices": True
}

FilteredView = {
    "key": "",
    "order": 0,
    "title": "The title of this view (optional).",
    "description": "",
    "properties": {"name": "value"},
    "baseViewKey": "Key1",
    "mode": "Include",
    "tags": "Tag1 Tag2",
}

ImageView = {
    "key": "",
    "order": 0,
    "title": "The title of this view (optional).",
    "description": "",
    "properties": {"name": "value"},
    "elementId": "ElementId1",
    "content": "https://contentview.org",
    "contentType": "image/png"
}

ElementView = {
    "id": "",
    "x": 0,
    "y": 0
}

Vertex = {
    "x": 0,
    "y": 0
}

RelationshipView = {
    "id": "",
    "description": "",
    "response": True,
    "order": 0,
    "vertices": [Vertex, Vertex],
    "routing": "Direct",
    "position": 50
}

DocumentationSection = {
    "content": "The Markdown or AsciiDoc content of the section.",
    "format": "Markdown",
    "order": 0,
}

Decision = {
    "id": "",
    "date": "2018-09-08T12:40:03Z",
    "status": "Proposed",
    "title": "The title of this view (optional).",
    "content": "The Markdown or AsciiDoc content of the section.",
    "format": "Markdown",
    "elementId": "ElementId10"
}

Image = {
    "name": "",
    "content": "The (base64 encoded) content of the image.",
    "type": "image/png",
}

Terminology = {
    "enterprise": "The terminology used when rendering the enterprise boundary.",
    "person": "The terminology used when rendering people.",
    "softwareSystem": "The terminology used when rendering software systems.",
    "container": "The terminology used when rendering containers.",
    "component": "The terminology used when rendering components.",
    "code": "The terminology used when rendering code elements.",
    "deploymentNode": "The terminology used when rendering deployment nodes.",
    "relationship": "The terminology used when rendering relationships."
}

Relationship = {
    "id": "RelationshipId1",
    "description": "",
    "tags": "Tag1 Tag2",
    "url": "https://archive.ics.uci.edu/ml",
    "properties": {"name": "value"},
    "perspectives": [Perspective],
    "sourceId": "",
    "destinationId": "",
    "technology": "",
    "interactionStyle": "Synchronous",
    "linkedRelationshipId": ""
}

AnimationStep = {
    "order": 0,
    "elements": ["ID1", "ID2", "ID3", "ID4"],
    "relationships": [Relationship],
}

SystemLandscapeView = {
    "key": "",
    "order": 0,
    "title": "The title of this view (optional).",
    "description": "",
    "properties": {"name": "value"},
    "paperSize": "A0_Landscape",
    "dimensions": Dimensions,
    "automaticLayout": AutomaticLayout,
    "enterpriseBoundaryVisible": False,
    "elements": [ElementView],
    "relationships": [Relationship],
    "animations": [AnimationStep]
}

SystemContextView = {
    "key": "",
    "order": 0,
    "title": "The title of this view (optional).",
    "description": "",
    "properties": {"name": "value"},
    "softwareSystemId": "SoftwareSystemId1",
    "paperSize": "A0_Landscape",
    "dimensions": Dimensions,
    "automaticLayout": AutomaticLayout,
    "enterpriseBoundaryVisible": False,
    "elements": [ElementView],
    "relationships": [Relationship],
    "animations": [AnimationStep]
}

ContainerView = {
    "key": "",
    "order": 0,
    "title": "The title of this view (optional).",
    "description": "",
    "properties": {"name": "value"},
    "softwareSystemId": "",
    "paperSize": "A0_Landscape",
    "dimensions": Dimensions,
    "automaticLayout": AutomaticLayout,
    "elements": [ElementView],
    "relationships": [Relationship],
    "animations": [AnimationStep],
    "externalSoftwareSystemBoundariesVisible": False
}

ComponentView = {
    "key": "",
    "order": 0,
    "title": "The title of this view (optional).",
    "description": "",
    "properties": {"name": "value"},
    "containerId": "ContainerId1",
    "paperSize": "A0_Landscape",
    "dimensions": Dimensions,
    "automaticLayout": AutomaticLayout,
    "elements": [ElementView],
    "relationships": [Relationship],
    "animations": [AnimationStep],
    "externalContainerBoundariesVisible": False
}

DynamicView = {
    "key": "",
    "order": 0,
    "title": "The title of this view (optional).",
    "description": "",
    "properties": {"name": "value"},
    "elementId": "ElementId1",
    "paperSize": "A0_Landscape",
    "dimensions": Dimensions,
    "automaticLayout": AutomaticLayout,
    "elements": [ElementView],
    "relationships": [Relationship],
    "externalBoundariesVisible": False
}

DeploymentView = {
    "key": "",
    "order": 0,
    "title": "The title of this view (optional).",
    "description": "",
    "properties": {"name": "value"},
    "softwareSystemId": "",
    "paperSize": "A0_Landscape",
    "dimensions": Dimensions,
    "automaticLayout": AutomaticLayout,
    "elements": [ElementView],
    "relationships": [Relationship],
    "animations": [AnimationStep],
    "externalSoftwareSystemBoundariesVisible": False,
    "environment": "Development"
},

Configuration = {
    "styles": {
        "elements": [ElementStyle],
        "relationships": [Relationship],
    },
    "lastSavedView": "Key0",
    "defaultView": "The key of the view that should be shown by default.",
    "themes": ["http_theme1", "http_theme2", "http_theme3"],
    "branding": Branding,
    "terminology": Terminology,
    "metadataSymbols": "SquareBrackets",
    "properties": {"name": "value"}
}

Views = {
    "systemLandscapeViews": [SystemLandscapeView],
    "systemContextViews": [SystemContextView],
    "containerViews": [ContainerView],
    "componentViews": [ComponentView],
    "dynamicViews": [DynamicView],
    "deploymentViews": [DeploymentView],
    "filteredViews": [FilteredView],
    "imageViews": [ImageView],
    "configuration": Configuration
}

WorkspaceConfiguration = {
    "users": [User, User],
    "visibility": "Private",
    "scope": "Landscape",
}

Documentation = {
    "sections": [DocumentationSection],
    "decisions": [Decision],
    "images": [Image]
}

APIResponse = {

    "success": True,
    "message": "A human readable response message.",
    "revision": 2
}

Component = {
    "id": "",
    "name": "",
    "description": "",
    "technology": "",
    "tags": "Tag1, Tag2",
    "url": "https://example.com",
    "group": "",
    "properties": {"Name": "Value"},
    "perspectives": [Perspective],
    "relationships": [Relationship],
    "documentation": Documentation
}

Container = {
    "id": "",
    "name": "",
    "description": "",
    "technology": "",
    "tags": "Tag1 Tag2",
    "url": "https://example.com",
    "components": [Component],
    "group": "",
    "properties": {"name": "value"},
    "perspectives": [Perspective],
    "relationships": [Relationship],
    "documentation": Documentation
}

Person = {
    "id": "",
    "name": "",
    "description": "",
    "tags": "Tag1 Tag2",
    "url": "",
    "location": "Unspecified",
    "group": "",
    "properties": {"name": "value"},
    "perspectives": [Perspective],
    "relationships": [Relationship]
}
InfrastructureNode = {
    "id": "InfrastructureNodeID1",
    "name": "",
    "description": "",
    "technology": "",
    "environment": "Deployment",
    "tags": "Tag1 Tag2",
    "url": "https://archive.ics.uci.edu/ml",
    "properties": {"name": "value"},
    "perspectives": [Perspective],
    "relationships": [Relationship],
}

SoftwareSystemInstance = {
    "id": "",
    "softwareSystemId": "",
    "instanceId": 10,
    "environment": "Deployment",
    "tags": "Tag1 Tag2",
    "properties": {"name": "value"},
    "perspectives": [Perspective],
    "relationships": [Relationship],
    "healthChecks": [HttpHealthCheck]
}

ContainerInstance = {
    "id": "",
    "containerId": "ContainingInstanceId",
    "instanceId": "ContainerInstance01",
    "environment": "Deployment",
    "tags": "Tag1 Tag2",
    "properties": {"name": "value"},
    "perspectives": [Perspective],
    "relationships": [Relationship],
    "healthChecks": [HttpHealthCheck],
}

DeploymentNode = {
    "id": "",
    "name": "",
    "description": "",
    "technology": "",
    "tags": "Tag1 Tag2",
    "url": "https://example.com",
    "components": [Component],
    "group": "",
    "properties": {"name": "value"},
    "environment": "Deployment",
    "instances": "",
    "children": [],  # [DeploymentNode], Recursive item
    "infrastructureNodes": [InfrastructureNode],
    "softwareSystemInstances": [SoftwareSystemInstance],
    "containerInstances": [ContainerInstance],
    "perspectives": [Perspective],
    "relationships": [Relationship]
}

SoftwareSystem = {
    "id": "",
    "name": "",
    "description": "",
    "location": "Unspecified",
    "tags": "Tagg1, Tag2",
    "url": "https://archive.ics.uci.edu/ml",
    "containers": [Container],
    "group": "",
    "properties": {"name", "value"},
    "perspectives": [Perspective],
    "relationships": [Relationship],
    "documentation": Documentation
}

Model = {
    "enterprise": {"properties": {"name": ""}},
    "people": [Person],
    "softwareSystems": [SoftwareSystem],
    "deploymentNodes": [DeploymentNode],
    "properties": {"name": "value"}
}

Workspace = {
    "id": 0,
    "name": "",
    "description": "",
    "version": "",
    "thumbnail": "",
    "lastModifiedDate": "2018-09-08T12:40:03Z",
    "lastModifiedUser": "john.doe@domain.com",
    "lastModifiedAgent": "DesignShift-python",
    "model": Model,
    "views": Views,
    "documentation": Documentation,
    "configuration": Configuration,
    "properties": {"name": "value"}
}

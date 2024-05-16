// from https://github.com/structurizr/examples/blob/main/dsl/plantuml-and-mermaid/dsl/workspace.dsl

//dsl/plantuml-and-mermaid/plugin
// see https://github.com/structurizr/dsl-plugins/tree/main/src/main/java/com/structurizr/dsl/plugins/plantuml for plugin source
// see https://github.com/structurizr/dsl-plugins/tree/main/src/main/java/com/structurizr/dsl/plugins/mermaid for plugin source

workspace {

    model {
        softwareSystem = softwareSystem "Software System" {
            !docs docs
        }
    }

    !plugin plantuml.PlantUMLEncoderPlugin {
        'plantuml.url' 'https://www.plantuml.com/plantuml'
    }

    !plugin mermaid.MermaidEncoderPlugin {
       'mermaid.url' 'https://mermaid.ink'
    }

}
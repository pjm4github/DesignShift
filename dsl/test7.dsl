workspace {

    configuration {
        scope softwaresystem
    }
    model {
        softwareSystem "Software System" {
            container "Container" {
                component "Component 1" {
                    properties {
                        structurizr.inspection.model.component.description ignore
                    }
                }
                component "Component 2"
                component "Component 3"
            }
        }
    }
    model {
        softwareSystem "Software System" {
            container "Container" {
                properties {
                    structurizr.inspection.model.component.description info
                }
                component "Component 1"
                component "Component 2"
                component "Component 3"
            }
        }
    }
    model {
            properties {
                structurizr.inspection.model.component.description ignore
            }
            softwareSystem "Software System" {
                container "Container" {
                    component "Component 1"
                    component "Component 2"
                    component "Component 3"
                }
            }
        }
    properties {
        structurizr.inspection.model.component.description ignore
    }

    model {
        softwareSystem "Software System" {
            container "Container" {
                component "Component 1"
                component "Component 2"
                component "Component 3"
            }
        }
    }
}

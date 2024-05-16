

// Assuming a file called script.kts is in the same directory as this file:
//workspace.views.createDefaultViews()
//workspace.views.views.forEach { it.disableAutomaticLayout() }

!script script.kts

//!script script.kts {
//    name value
//}

workspace {

    !script groovy {
    workspace.views.createDefaultViews()
    workspace.views.views.findAll // { it instanceof com.structurizr.view.ModelView }.each { it.disableAutomaticLayout() }
    }

    !identifiers hierarchical

    model {
        softwareSystem1 = softwareSystem "Software System 1" {
            api = container "API"
        }

        softwareSystem2 = softwareSystem "Software System 2" {
            api = container "API"
        }
    }
}
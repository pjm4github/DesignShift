workspace {

    model {
        user = person "User"
        softwareSystem = softwareSystem "Software System" {
            webApp = container "Web Application"
            database = container "Database"
        }

        user -> webApp "Uses the web app"
        webApp -> database "Queries data" "JDBC" "Web-to-DB Interaction"  {
            tag "webApp to database relation"
        }
    }

    views {
        systemContext softwareSystem {
            include *
            autolayout lr
        }

        containerView softwareSystem {
            include *
            autolayout lr
        }
    }
}
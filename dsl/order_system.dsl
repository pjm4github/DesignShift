// from https://eidivandiomid.medium.com/diagram-as-code-using-structurizr-c41f6dd0738f

workspace {
    model {
        User = person "User"
        Order = softwareSystem "Order System" {
            Ingestion = container "Order Ingestion" {
                Api = component "Api"
                Database = component "Database"
                Broker = component "Broker"
            }
        }
        Product = softwareSystem "Product System" {
            OrderListener = container "Order Listner" {
                Database = component "Database"
                Processor = component "Availability Processor"
            }
        }
        User -> Order.Ingestion.Api
        order.Ingestion.Api -> Order.Ingestion.Database
        Order.Ingestion.Api -> Order.Ingestion.Broker
        product.OrderListener.Processor -> Product.OrderListener.Database
        Order.Ingestion.Broker -> Product.OrderListener.Processor
    }
    views {
        systemLandscape {
            include *
        }
        systemContext Order {
            include *
        }

        container Order {
            include *
        }

        component Order.Ingestion {
            include *
        }
        systemContext Product {
            include *
        }

        container Product {
            include *
        }

        component Product.OrderListener {
            include *
        }

        properties {
            structurizr.sort "type"
        }
        theme default
    }
}
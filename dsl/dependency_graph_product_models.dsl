// https://github.com/XaaXaaX/structurizr-dependency-graph/blob/main/src/product/models.dsl

Product = softwareSystem "Product System" {
    OrderListener = container "Order Listner" {
        Database = component "Database"
        Processor = component "Availability Processor"
    }
}

product.OrderListener.Processor -> Product.OrderListener.Database
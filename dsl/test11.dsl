
!include people.dsl

!include model/people.dsl
!include model
!include https://example.com/model/people.dsl

!docs subdirectory

!adrs subdirectory

workspace {

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
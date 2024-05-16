// from https://docs.structurizr.com/dsl/cookbook/deployment-groups/

/* Imagine that you have a service comprised of an API and a database scheme, which are deployed together onto a single
   server. Now let’s say there are two instances of this entire service, each deployed onto a separate server.
   The container instance to container instance relationships are based upon the container to container relationships
   defined in the static structure part of the model. While this works out of the box in many cases,
   here we can see that the “Service API” on “Server 1” has a connection to the “Database Schema”
   on “Server 2”, and vice versa.
   If this is not the desired behaviour, you can use the “deployment group” feature, which provides a way to group
   software system/container instances and restrict how relationships are created between them.
   For example, we can create two deployment groups, and place one instance of both the
   “Service API” and “Database Schema” in each.

   */

workspace {

    model {
        softwareSystem = softwareSystem "Software System" {
            database = container "Database Schema"
            api = container "Service API" {
                -> database "Uses"
            }
        }

        production = deploymentEnvironment "Production" {
            serviceInstance1 = deploymentGroup "Service instance 1"
            serviceInstance2 = deploymentGroup "Service instance 2"

            deploymentNode "Server 1" {
                containerInstance api serviceInstance1
                deploymentNode "Database Server" {
                    containerInstance database serviceInstance1
                }
            }
            deploymentNode "Server 2" {
                containerInstance api serviceInstance2
                deploymentNode "Database Server" {
                    containerInstance database serviceInstance2
                }
            }
        }
    }

    views {
        deployment * production {
            include *
            autolayout
        }
    }

}
workspace some "wordsuerieu"  {
    model "model1" "This is a model that will work" {
        user = person "User" "A user of my software system."
        s = softwareSystem "Software System" "A software system." {
            cc = container "container system" {

                dd = component myComponent

            }
        }

        b = softwareSystem "SecondSytem" "Another software system."
        user -> s "Uses"
        b -> d "Is Part of"
        //container "Big Container" "[hdyg]"
    }
}
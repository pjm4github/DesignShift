workspace some "wordsuerieu"  {

    model "model1" "This is a model that will work" {

        user = person "User" "A user of my software system."
        s = softwareSystem "Software System" "A software system."
        softwareSystem "SecondSytem" "Another software system."
        user -> s "Uses"
    }

}
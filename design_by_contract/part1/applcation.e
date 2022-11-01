note
    description : "root class of the application"
    date        : "$Date$"
    revision    : "$Revision$"

class
    APPLICATION

inherit
    ARGUMENTS_32

create
    make

feature {NONE} -- Initialization

    make
        local
            Cat: CAT
            Dog: DOG
        do
            create Cat.make(2, "CatName")
            print("%NPET Name: ")
            io.put_string(Cat.get_name)
            print("%NPET Age: ")
            io.put_real(Cat.get_age)
            print("%N----------------------%N")

            create Dog.make(8, "DogName")
            print("%NPET Name: ")
            io.put_string(Dog.get_name)
            print("%NPET Age: ")
            io.put_real(Dog.get_age)

            print("%N--Error code--%N")
            create Dog.make(0, "Cat")
        end

end

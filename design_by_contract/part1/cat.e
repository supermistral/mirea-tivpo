note
    description : "Subclass {CAT} of Pet"
    date        : "$Date$"
    revision    : "$Revision$"
    
class
    CAT

inherit
    PET

create
    make

feature
    age: REAL
    name: STRING
        
    feature{ANY}
    
        make(a: REAL; n: STRING)
            require else
                a > 0
                n.capacity > 0
                n /= "Dog"
            do
                age := a
                name := n
                print("New Cat is created")
            end
        
    feature{ANY}
    
        get_age: REAL
            do
                Result := age;
            ensure then
                Result > 0
            end
    
    feature{ANY}
    
        get_name: STRING
            do
                Result := name
            ensure then
                Result.capacity > 0
            end

end

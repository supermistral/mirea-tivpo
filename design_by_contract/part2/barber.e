note
	description : "Summary description for {BARBER}."
	date        : "$Date$"
	revision    : "$Revision$"

class
	BARBER

create
	make

feature {NONE} -- Initialization

	make (a_id: INTEGER)
			-- Initialize with `a_id' as id
		require
			a_id > 0
		
		do
			id := a_id
		end

feature {CUSTOMER} -- Operations

	cut_hair (c: separate CUSTOMER)
		do
			print ("Barber "+id.out+ " is cutting Customer "+ c.id.out +" s hairs.%N")
			(create {EXECUTION_ENVIRONMENT}).sleep (2)
		end

feature -- Implementation

	id: INTEGER -- Unique Id

invariant
	valid_id: id > 0
end

class Guest:
    def __init__(self):
        self.first_name = "guest"
        self.last_name = ""

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name


class Room:
    def __init__(self, room_number, floor_number, capacity):
        self.is_occupied = False
        self.capacity = capacity
        self.room_number = room_number
        self.floor = floor_number
        self.room_bill = 1000 * capacity
        self.guests_list = []

    def __repr__(self):
        return "Room-"+str(self.get_room_number())

    def get_is_occupied(self):
        return self.is_occupied

    def set_is_occupied(self):
        self.is_occupied = True

    def get_capacity(self):
        return self.capacity

    def get_room_number(self):
        return self.room_number

    def get_floor(self):
        return self.floor

    def get_room_bill(self):
        return self.room_bill

    def add_to_bill(self, new_amount):
        self.room_bill += new_amount

    def add_guest_to_room(self, guest):
        self.guests_list.append(guest)


class Hotel:
    def __init__(self):
        self.levels = 2
        self.rooms = 2
        self.room_types = [self.rooms for _ in range(self.levels)]
        self.rooms_available = [[Room((i+1)*100+j, i, i+2) for j in range(self.rooms)] for i in range(self.levels)]
        self.rooms_booked = {}

    def remove_booked_room(self, room_number):
        del self.rooms_booked[room_number]

    def get_booked_room(self, room_number):
        return self.rooms_booked.get(room_number, None)

    def get_vacant_rooms(self, number_of_guests):
        room_type = []
        temp = number_of_guests
        temp_room_type = len(self.room_types)-1
        while temp > 0:
            if temp_room_type >= 0 and len(self.rooms_available[temp_room_type]) > 0:
                this_room = self.rooms_available[temp_room_type].pop(0)
                this_room_guest_count = min(temp, this_room.get_capacity())
                room_type.append((this_room, this_room_guest_count))
                self.room_types[temp_room_type] -= 1
                temp -= temp_room_type+2
            elif temp_room_type < 0 and temp > 0:
                return []
            else:
                temp_room_type -= 1
        return room_type

    def book_rooms(self, rooms):
        print(rooms)
        for room, guests in rooms:
            print("\nPlease enter guest details for Room-" + str(room.get_room_number()))
            for i in range(guests):
                new_guest = Guest()
                new_guest.set_first_name(input("Enter first name for guest-" + str(i) + " : "))
                new_guest.set_last_name(input("Enter last name for guest-" + str(i) + " : "))
                room.add_guest_to_room(new_guest)
            self.rooms_booked[room.get_room_number()] = room

    def check_in(self):
        number_of_guests = int(input("\nEnter total number of guests : "))
        if number_of_guests > 0:
            rooms = self.get_vacant_rooms(number_of_guests)
            if rooms:
                self.book_rooms(rooms)
            else:
                print("Sorry no rooms available !! ")
        else:
            print("enter more guests !!")

    def check_out(self):
        room_number = int(input("\nEnter rooms to vacant : "))
        room = self.get_booked_room(room_number)
        if room:
            print(room)
            print("Room bill is = ", room.get_room_bill())
            self.clear_room(room)
            print("Thanks for Booking")
            print(self.rooms_available)
        else:
            print("Room not found !! ")

    def clear_room(self, room):
        floor = room.get_floor()
        self.rooms_available[floor].append(room)
        self.room_types[floor] += 1

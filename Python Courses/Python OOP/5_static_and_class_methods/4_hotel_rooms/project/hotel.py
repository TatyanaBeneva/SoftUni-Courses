from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        
    @property
    def guests(self):
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room_number == room.number][0]
        return room.take_room(people)

    def free_room(self, room_number):
        room = [room for room in self.rooms if room_number == room.number][0]
        return room.free_room()

    def status(self):
        free_room_numbers = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_room_numbers = [str(room.number) for room in self.rooms if room.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_room_numbers)}\nTaken rooms: {', '.join(taken_room_numbers)}"

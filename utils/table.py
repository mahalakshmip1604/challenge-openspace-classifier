class Seat:
    """
    Represents a seat in the open space.
    Attributes:
        free (bool): Indicates whether the seat is free or occupied.
        occupant (str): The name of the occupant if the seat is occupied, otherwise None.
    """
    def __init__(self, free, occupant=None):
        self.free = free 
        self.occupant = occupant

    def set_occupant(self, name):
        """Assigns an occupant to the seat if it is free."""
        if self.free:
            self.occupant = name
            self.free = False
           

    def remove_occupant(self):
            """Removes the occupant from the seat if it is occupied."""
            if not self.free:
                removed_person = self.occupant
                self.occupant = None
                self.free = True
                return removed_person
            else:
                return None 
    def _str_(self):
        '''Returns a string representation of the Seat object, including whether it is free and the name of the occupant if it is occupied.'''
        return f"Seat(free={self.free}, occupant='{self.occupant}')"
    
class Table:
    """Represents a table in the open space.
    Attributes:
        capacity (int): The maximum number of seats at the table.
        seats (list): A list of Seat objects representing the seats at the table.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seats = [Seat(True, occupant="") for i in range(capacity)]

    def has_free_spot(self):
        """Checks if there is at least one free seat at the table."""
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self, name):
        """Assigns a seat to the given name if there is a free seat available."""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        print("Sorry, no free seats available.")

    def left_capacity(self):
        """Returns the number of free seats left at the table."""
        count = 0
        for seat in self.seats:           
            if seat.free:
                count += 1
        return count   
    
    def _str_(self):
        '''Returns a string representation of the Table object, including its capacity and the status of its seats.'''
        return f"Table(capacity={self.capacity}, seats={self.seats})"

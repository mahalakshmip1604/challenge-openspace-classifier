
from utils.table import Seat, Table
from random import  shuffle

class Openspace:
    """Represents an open space with multiple tables.
    Attributes:
        assign_tables (int): The number of tables in the open space.
        tables (list): A list of Table objects representing the tables in the open space.
    """
    def __init__(self, number_of_tables: int, table_capacity: int):
        self.assign_tables=number_of_tables
        self.tables = [Table(capacity=table_capacity) for _ in range(number_of_tables)]

    def organize(self, names: list):
        """Organizes the seating arrangement by randomly assigning names to tables."""
        shuffled_names = names.copy()
        shuffle(shuffled_names)
        for name in shuffled_names:
            for table in self.tables:
                                    
                if table.has_free_spot():
                    table.assign_seat(name)
                    assigned = True                   
                    break
                else:
                    assigned = False               
             
    def display(self):
        """Displays the seating arrangement in the terminal."""
        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i}:")
            num=1
            for seat in table.seats:
                if seat.free:
                    print("  - Free")
                else:                    
                    print(f"Seat{num}  - {seat.occupant}")
                    num += 1

    def store(self, filename: str):
        """Saves the seating arrangement to a file."""
        with open(filename, 'w') as file:
            for i, table in enumerate(self.tables, start=1):
                file.write(f"Table {i}:\n")
                for seat in table.seats:
                    if seat.free:
                        file.write("  - Free\n")
                    else:
                        file.write(f"  - {seat.occupant}\n")
    def _str_(self):     
        '''Returns a string representation of the Openspace object, including the number of tables and the details of each table.'''  
        return f"Openspace(assign_tables={self.assign_tables}, tables={self.tables})"


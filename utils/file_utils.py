import csv
def read_names_from_csv(filepath: str) -> list:
    """Reads names from a CSV file and returns them as a list."""
    names = []
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Ensure the row is not empty
                names.append(row[0])  # Assuming names are in the first column
    return names

def _str_(self):
    '''Returns a string representation of the Seat object, including whether it is free and the name of the occupant if it is occupied.'''
    return f"Seat(free={self.free}, occupant='{self.occupant}')"
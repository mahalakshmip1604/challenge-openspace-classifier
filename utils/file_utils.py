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
    return f"Seat(free={self.free}, occupant='{self.occupant}')"
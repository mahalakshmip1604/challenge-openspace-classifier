from utils.openspace import Openspace as OpenSpace
from utils.file_utils import read_names_from_csv
def main():
    """Main function to execute the open space seating arrangement.
    This function reads colleague names from a CSV file, prompts the user for the number of tables and their capacity,
    creates an OpenSpace instance, organizes the seating arrangement, saves the arrangement to a file, and displays it in the terminal.
    """

    input_filepath = "challenge-openspace-classifier\\new_colleagues.csv"
    output_filename = "challenge-openspace-classifier\\output.csv"

    # Creates a list that contains all the colleagues names
    names = read_names_from_csv(input_filepath)

    # User Inputs - Use the input if provided, otherwise use the default integer 
    tables_user_input = input("Enter the number of tables (default 6): ")
    tables = int(tables_user_input) if tables_user_input.strip() else 6

    capacity_user_input = input("Enter the capacity of each table (default 4): ")
    capacity = int(capacity_user_input) if capacity_user_input.strip() else 4

    # create an OpenSpace
    open_space = OpenSpace(number_of_tables=tables, table_capacity=capacity)

    # assign a colleague randomly to a table
    open_space.organize(names)

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display()
    print(f"Table arrangements have been saved to {output_filename} file.")

if __name__ == "__main__":
    main()
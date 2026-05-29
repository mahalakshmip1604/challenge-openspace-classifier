# OpenSpace Organizer #
forthebadge made-with-python

🏢 Description

Your company moved to a new office at CEVI Ghent. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues.

This script runs everyday to re-assign everybody to a new seat.


```text

📦 Repo structure
.
├── utils/
│   ├── openspace.py
│   ├── table.py
│   └── file_utils.py
├── main.py
├── new_colleagues.csv
├── notebook_guide.ipynb
├── output.csv
└── README.md

🛎️ Usage
1. Clone the repository to your local machine.
2. To run the script, you can execute the main.py file from your command line:

# main.py Description: 

User inputs will be taken for Tables and its capacity count.
The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.csv" file in your root directory.

Added addtional feature of adding new members if the capacity is not full.

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

    # Adding new colleagues if there is still place at the tables.
    if tables * capacity > len(names):
        print(f"Still place for new colleagues, you can add more names to the list.")        
        print("Enter items one by one. Type 'done' to finish.\nAlso it stops when capacity is reached.")
        items = []
        while True:
            user_entry = input("Enter Name: ")
            if user_entry.lower() == 'done' or len(items) + len(names) >= tables * capacity:
                break
            items.append(user_entry)
        for input_name in items:
            names.append(input_name)
    else:
        print(f"Warning: The total seating capacity ({tables * capacity}) is less than the number of colleagues ({len(names)}). Some colleagues will not be assigned a seat.")  
    

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

⏱️ Timeline
This project took two days for completion.

📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org.

Connect with me in [LinkedIn](www.linkedin.com/in/mahalakshmi-palanivel-4b6701296)

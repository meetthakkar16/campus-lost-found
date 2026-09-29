# Campus Lost and Found Matcher

## Overview

Campus Lost and Found Matcher is a command-line Python program for managing lost and found item reports on a campus.

The program allows users to:
- Add lost item reports
- Add found item reports
- View all reported items
- Search for items by item type
- Find possible matches between lost and found items
- Update an item's status
- View the number of active and finished items

The program stores all item information in memory while it is running.

## Features

### 1. Add Lost Item
The user can create a lost-item report by entering:
- Item type
- Brand
- Colour
- Location
- Date
- Description

The program automatically assigns a unique ID and sets the initial status to `active`.

### 2. Add Found Item
The user can create a found-item report using the same information. The program automatically assigns a unique ID and sets the initial status to `active`.

### 3. View Items
The program displays all reported items, including:
- ID
- Report type
- Type
- Brand
- Colour
- Location
- Date
- Description
- Status

If there are no items, the program displays `No items found`.

### 4. Search Item
The user can enter an item type to search for. The program displays every reported item whose `type` exactly matches the entered item type.

If no item matches, it displays `No matching items found`.

### 5. Find Possible Matches
The program compares lost-item reports with found-item reports.

A possible match is displayed when the `type` of a lost item is exactly the same as the `type` of a found item.

The current version does **not** compare brand, colour, location, date, or description when finding matches.

### 6. Update Item Status
The user can enter an item's ID and change its status. The program prompts for `active` or `finished` and updates the selected item.

### 7. View Status
The program counts and displays:
- Number of `active` items
- Number of `finished` items

### 8. Exit
The program exits when the user selects option `8`.

## How to Run

Python 3 is required.

Open a terminal in the project directory and run:

```bash
python main.py
```

No external Python libraries are required.

## Data Storage

The program uses:
- A list named `items` to store all reports.
- A variable named `next_id` to generate unique item IDs.
- Dictionaries to store the details of each item.

Data is stored only in memory. It is **not** saved to a file or database. Therefore, all reports are lost when the program is closed.

## Project Structure

```text
project-folder/
│
├── main.py
├── README.md
├── statement.md
└── TESTING.md
```

### `main.py`
Contains the complete Python program.

### `README.md`
Contains information about the project, its features, setup, and usage.

### `statement.md`
Contains the problem statement for the project.


## Technologies Used

- Python 3
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- User input

No external libraries or packages are required.

## Limitations

- Data is not permanently stored.
- The program is command-line based.
- Matching is based only on exact item type.
- Search uses an exact match for the item type.
- There is no user authentication system.
- Status input is accepted from the user without additional validation.

## Future Improvements

Possible future improvements include:
- Saving reports permanently using files or a database
- Adding a graphical user interface
- Adding stronger input validation
- Improving matching by comparing brand, colour, location, and other details
- Adding date validation
- Adding user accounts
- Adding advanced search and filtering

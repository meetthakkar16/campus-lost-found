# Problem Statement

## Campus Lost and Found Matcher

Students and staff on a campus may lose personal belongings or find items that belong to someone else. Managing these reports manually can make it difficult to keep track of items and identify possible matches.

The objective of this project is to create a simple command-line **Campus Lost and Found Matcher** using Python.

The program should allow a user to:

1. Report a lost item.
2. Report a found item.
3. View all reported items.
4. Search for reported items by item type.
5. Identify possible matches between lost and found items.
6. Update the status of an item.
7. View the number of active and finished reports.

Each item report contains:
- An automatically generated ID
- Report type (`lost` or `found`)
- Item type
- Brand
- Colour
- Location
- Date
- Description
- Status

A new report is initially given the status `active`. The user can later change an item's status to `finished`.

For the current version, a lost item and a found item are considered a possible match when their **item types are exactly the same**. Brand, colour, location, date, and description are stored and displayed, but they are not currently used by the matching logic.

The program stores reports in memory using a list of dictionaries. No external database or data file is required.

## Objective

The main objective is to build a simple Python-based system that demonstrates how basic programming concepts can be used to manage and search structured information.

The project demonstrates:
- Variables
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- User input
- Searching through stored data
- Updating stored data

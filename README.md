# Programming Fundamentals

## 1. Grades Catalog - Project Overview

This app helps manage student data and lab assignments in an academic setting. The application supports various operations like adding and removing students, assigning lab tasks, grading, and generating reports.

### Data Structure
- **Student**: Each student has a unique ID, name, and group.
- **Lab Assignment**: Each lab task is identified by a lab number and problem number, along with a description and a deadline.

## Features

1. **Manage Students and Lab Assignments**:
   - Add, delete, and modify student records.
   - Add, delete, and modify lab assignments.
   - Search for students and lab assignments.

2. **Assign and Grade Labs**:
   - Assign labs to students.
   - Record grades for lab assignments.

3. **Generate Statistics**:
   - List students and their grades for a given lab assignment, sorted alphabetically by name or by grade.
   - Identify students with an average lab grade below a certain threshold.
   - Display students whose average lab grades fall within a specified range.



## 2. Travel Agency - Project Overview

This app helps manage travel packages offered to clients. The application supports operations like adding new packages, modifying existing packages, searching for specific packages, and generating reports based on different criteria.

### Data Structure
- **Travel Package**: Each travel package is defined by a start date, end date, destination, and price.

## Features

1. **Manage Travel Packages**:
   - Add a new travel package.
   - Modify an existing travel package.
   - Delete travel packages based on various criteria (e.g., destination, duration, price).

2. **Search and Reporting**:
   - Search for travel packages within a specified date range.
   - Search for travel packages to a specific destination under a certain price.
   - Search for travel packages with a specific end date.
   - Generate reports such as the number of offers for a specific destination and the average price for a destination.
   - List all available travel packages in a given period, sorted by price.

3. **Filtering**:
   - Filter out offers that exceed a certain price and are for a different destination than specified.
   - Filter out offers that include stays during a specific month.

4. **Undo Operation**:
   - Revert the last operation that modified the list of travel packages.



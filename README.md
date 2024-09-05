# Programming Fundamentals

Welcome to the "Programming Fundamentals" repository! This repository contains two distinct projects that demonstrate different aspects of programming: a Grades Catalog application for managing student data and assignments, and a Travel Agency application for managing travel packages. Each project is designed to showcase fundamental programming techniques and concepts.

## Table of Contents

1. [Grades Catalog - Project Overview](#1-grades-catalog---project-overview)
   - [Data Structure](#data-structure-for-grades-catalog)
   - [Features](#features-of-grades-catalog)
   - [Installation](#installation-for-grades-catalog)
   - [Usage](#usage-for-grades-catalog)

2. [Travel Agency - Project Overview](#2-travel-agency---project-overview)
   - [Data Structure](#data-structure-for-travel-agency)
   - [Features](#features-of-travel-agency)
   - [Installation](#installation-for-travel-agency)
   - [Usage](#usage-for-travel-agency)


---

## 1. Grades Catalog - Project Overview

This app helps manage student data and lab assignments in an academic setting. The application supports various operations like adding and removing students, assigning lab tasks, grading, and generating reports.

### Data Structure for Grades Catalog

- **Student**: Each student has a unique ID, name, and group.
- **Lab Assignment**: Each lab task is identified by a lab number and problem number, along with a description and a deadline.

### Features of Grades Catalog

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

### Installation for Grades Catalog

To run the Grades Catalog application locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BiancaM30/Programming-Fundamentals.git
   cd Programming-Fundamentals/grades-catalog

2. **Install Dependencies**: Ensure you have Python installed (version 3.6 or higher). Install required packages:
   ```bash
    pip install -r requirements.txt

### Usage for Grades Catalog
To run the application, execute the main.py file in the grades-catalog directory:
    ```bash
   python main.py

---

## 2. Travel Agency - Project Overview

This app helps manage travel packages offered to clients. The application supports operations like adding new packages, modifying existing packages, searching for specific packages, and generating reports based on different criteria.

### Data Structure for Travel Agency
Travel Package: Each travel package is defined by a start date, end date, destination, and price.

### Features of Travel Agency
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

### Installation for Travel Agency

To run the Travel Agency application locally:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BiancaM30/Programming-Fundamentals.git
   cd Programming-Fundamentals/travel-agency


2. **Install Dependencies**: Ensure you have Python installed (version 3.6 or higher). Install required packages:
   ```bash
    pip install -r requirements.txt

### Usage for Travel Agency
To run the application, execute the main.py file in the travel-agency directory:
    ```bash
   python main.py

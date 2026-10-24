
# Bincom Python Assessment

## Overview

This project contains my solutions to the Bincom ICT Solutions Python preliminary assessment. It demonstrates Python programming fundamentals, data analysis, algorithms, number conversion, Fibonacci sequences, and PostgreSQL database integration.

## Tasks Implemented

### 1. Staff Colour Data Analysis
Stores the staff shirt-colour data for five working days (Monday to Friday), cleans the entries, and calculates the frequency of each colour.

### 2. Most-Worn Colour
Identifies the colour worn most frequently throughout the week.

**Result:** BLUE, with 30 occurrences.

### 3. Mean and Median
Calculates the mean and median of the colour frequency counts.

**Note:** Colours are categorical data, so a mean or median colour is not mathematically defined without a specified numerical encoding or ordering. The program therefore calculates these statistics using the frequency counts.

### 4. Variance
Calculates both the population variance and sample variance of the colour frequency counts.

### 5. Probability of Red
Calculates the probability of randomly selecting a red shirt from all recorded entries.

**Result:** 9/95, approximately 9.47%.

### 6. PostgreSQL Database Integration
Saves the colour names and their frequencies in a PostgreSQL database table named `colour_frequencies`.

### 7. Recursive Binary Search
Implements a recursive binary search algorithm to locate a user-entered number in a sorted list.

### 8. Binary-to-Decimal Conversion
Generates a random four-bit binary number containing only 0s and 1s and converts it to a base-10 integer.

### 9. Fibonacci Sequence
Calculates the sum of the first 50 Fibonacci terms, starting with 0 and 1.

**Result:** 20,365,011,073.

## Technologies Used

- Python 3
- PostgreSQL 16
- Psycopg 3 (PostgreSQL adapter for Python)
- Git and GitHub

## Project Structure

```text
bincom_python_test/
├── bincom_test.py
├── python_class_question.html
├── README.md
├── requirements.txt
└── .gitignore
```

## Prerequisites

Before running the program, ensure you have:

- Python 3 installed.
- PostgreSQL installed and running.
- A PostgreSQL database created for the assessment.
- Git installed (optional, for version control).

## Installation and Setup

### 1. Clone the repository

```bash
git clone "https://github.com/meem08/bincom"
cd bincom_python_test
```


### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure PostgreSQL

Create a database named `bincom_test` in PostgreSQL.

Set the following environment variables in PowerShell:

```powershell
$env:PGDATABASE = "bincom_test"
$env:PGUSER = "postgres"
$env:PGHOST = "localhost"
$env:PGPORT = "5432"
$env:PGPASSWORD = Read-Host "Enter your PostgreSQL password"
```


### 4. Run the program

```bash
python bincom_test.py
```

When prompted, enter a number to test the recursive binary search.

## Expected Results

Using the supplied colour data:

- Total colour entries: 95
- Number of distinct colour categories: 12
- Most-worn colour: BLUE (30 occurrences)
- Probability of red: approximately 9.47%
- Mean frequency: approximately 7.92
- Median frequency: 5.5
- Population variance: approximately 63.24
- Sample variance: approximately 68.99
- Sum of the first 50 Fibonacci terms: 20,365,011,073

The binary number and binary-search result depend on the generated number and user input, respectively.

## Notes

- Binary search requires a sorted list.
- The mean, median, and variance refer to colour frequency counts, not the colour names themselves.
- The PostgreSQL section requires a working database connection and valid environment variables.
- The original colour entries are preserved as supplied.

## Author

Submitted as part of the Bincom ICT Solutions Python preliminary assessment.

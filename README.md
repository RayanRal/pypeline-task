# Pypeline Task

This repository contains a coding test for Python candidates.

## Structure

- `mock_server/`: Contains the Flask server that provides paginated employee data.
- `task/`: This is where the candidate should implement their solution.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install requests  # Candidate will need this
   ```

## Running the Mock Server

In one terminal:
```bash
python mock_server/server.py
```
The server runs on `http://127.0.0.1:5001`.

## Candidate Task

The candidate should implement the `EmployeeAnalysis` class in `task/solution.py` with the following methods:

1. `get_employee_count()`: Returns the total number of employees.
2. `get_average_salary_by_department()`: Calculates the average salary for each department.
3. `get_top_3_highest_paid_employees()`: Finds the top 3 employees with the highest salary.

**Objective:** 
The class is initialized with a `base_url`. Use this URL to download all employee records (which is paginated) and implement the analysis logic.

## Validation

To validate the solution, run the following command in the terminal (ensure the mock server is NOT running, as the test suite handles its lifecycle):

```bash
pytest tests/test_solution.py
```

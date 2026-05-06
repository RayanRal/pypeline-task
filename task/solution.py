"""
Candidate Task: 
Write a script that downloads all employee data from the paginated API,
parses it, and uses this data to implement functions in EmployeeAnalysis
"""

import requests

class EmployeeAnalysis:
    def __init__(self, base_url="http://127.0.0.1:5001/employees"):
        self.base_url = base_url

    def get_employee_count(self):
        """
        Returns the total number of employees.
        """
        # TODO: Implement this
        return 0

    def get_average_salary_by_department(self):
        """
        Calculates the average salary for each department.
        Returns a dictionary: {department_name: average_salary}
        """
        # TODO: Implement this
        return {}

    def get_top_3_highest_paid_employees(self):
        """
        Finds the top 3 employees with the highest salary.
        Returns a list of employee dictionaries.
        """
        # TODO: Implement this
        return []

if __name__ == "__main__":
    # You can add some print statements here to test your implementation manually
    analysis = EmployeeAnalysis()
    pass

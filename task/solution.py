"""
Candidate Task:
Write a script that downloads all employee data from the paginated API,
parses it, and uses this data to implement functions in EmployeeAnalysis
"""

from collections import defaultdict
import requests


class EmployeeAnalysis:
    def __init__(self, base_url="http://127.0.0.1:5001/employees"):
        self.base_url = base_url

    def _get_employee_data(self):
        page = 1
        employees = []

        while True:
            response = requests.get(self.base_url, params={"page": page})
            response.raise_for_status()
            result = response.json()
            employees.extend(result["data"])

            if page >= result["total_pages"]:
                break

            page += 1

        return employees

    def get_employee_count(self):
        """
        Returns the total number of employees.
        """
        response = requests.get(self.base_url, params={"page": 1})
        response.raise_for_status()
        return response.json()["total"]

    def get_average_salary_by_department(self):
        """
        Calculates the average salary for each department.
        Returns a dictionary: {department_name: average_salary}
        """
        salary_total = defaultdict(int)
        emp_count = defaultdict(int)

        for employee in self._get_employee_data():
            department = employee["department"]
            salary_total[department] += employee["salary"]
            emp_count[department] += 1

        return {
            department: salary_total[department] / emp_count[department]
            for department in salary_total
        }

    def get_top_3_highest_paid_employees(self):
        """
        Finds the top 3 employees with the highest salary.
        Returns a list of employee dictionaries.
        """
        data = self._get_employee_data()
        return sorted(data, key=lambda employee: employee["salary"], reverse=True)[:3]


if __name__ == "__main__":
    analysis = EmployeeAnalysis()
    pass

import sys
import os
import pytest

# Add the parent directory to sys.path so we can import the task module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task.solution import EmployeeAnalysis

@pytest.fixture
def analysis():
    return EmployeeAnalysis()

def test_get_employee_count(analysis):
    count = analysis.get_employee_count()
    assert count == 100

def test_get_average_salary_by_department(analysis):
    averages = analysis.get_average_salary_by_department()
    
    expected = {
        "Engineering": 55250.0,
        "HR": 54850.0,
        "Marketing": 54950.0,
        "Sales": 55050.0,
        "Product": 55150.0
    }
    
    assert averages == expected

def test_get_top_3_highest_paid_employees(analysis):
    top_3 = analysis.get_top_3_highest_paid_employees()
    
    assert len(top_3) == 3
    
    # IDs should be 100, 99, 98
    ids = [e["id"] for e in top_3]
    assert 100 in ids
    assert 99 in ids
    assert 98 in ids
    
    # Salaries should be 60000, 59900, 59800
    salaries = sorted([e["salary"] for e in top_3], reverse=True)
    assert salaries == [60000, 59900, 59800]

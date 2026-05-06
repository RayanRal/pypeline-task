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
    assert count == 90

def test_get_average_salary_by_department(analysis):
    averages = analysis.get_average_salary_by_department()
    
    expected = {
        "Engineering": 54750.0,
        "HR": 54350.0,
        "Marketing": 54450.0,
        "Sales": 54550.0,
        "Product": 54650.0
    }
    
    assert averages == expected

def test_get_top_3_highest_paid_employees(analysis):
    top_3 = analysis.get_top_3_highest_paid_employees()
    
    assert len(top_3) == 3
    
    # IDs should be 90, 89, 88
    ids = [e["id"] for e in top_3]
    assert 90 in ids
    assert 89 in ids
    assert 88 in ids
    
    # Salaries should be 59000, 58900, 58800
    salaries = sorted([e["salary"] for e in top_3], reverse=True)
    assert salaries == [59000, 58900, 58800]

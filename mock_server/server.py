import os
from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    # Sample data: 100 employees
    employees = []
    departments = ["Engineering", "HR", "Marketing", "Sales", "Product"]

    for i in range(1, 91):
        dept = departments[i % len(departments)]
        employees.append({
            "id": i,
            "name": f"Employee {i}",
            "department": dept,
            "salary": 50000 + (i * 100),
            "start_date": "2020-01-01",
            "end_date": None if i % 10 != 0 else "2023-01-01"
        })

    @app.route('/employees', methods=['GET'])
    def get_employees():
        page = request.args.get('page', default=1, type=int)
        per_page = 20
        
        start = (page - 1) * per_page
        end = start + per_page
        
        paginated_data = employees[start:end]
        
        return jsonify({
            "page": page,
            "per_page": per_page,
            "total": len(employees),
            "total_pages": (len(employees) + per_page - 1) // per_page,
            "data": paginated_data
        })
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5001, debug=True)

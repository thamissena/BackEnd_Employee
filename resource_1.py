from flask_restful import Resource,reqparse
from models import EmployeeModel,ReviewModel
from datetime import date, datetime



class Employees(Resource):
    def get(self):
        return {"Employees":[employee.json() for employee in EmployeeModel.query.all()]}


    def post(self):

        argumento = reqparse.RequestParser()
        argumento.add_argument('name', type=str, required=True, help="Name is required")
        argumento.add_argument('birth_date', type=str, required=True, help="Birth date is required")
        argumento.add_argument('address', type=str, required=True, help="Address is required")
        argumento.add_argument('phone', type=str, required=True, help="Phone is required")
        argumento.add_argument('email',type=str, required=True, help="Email is required")
        argumento.add_argument('job_title',type=str, required=True, help="Job title is required")
        argumento.add_argument('department', type=str, required=True, help="Department is required")

        valor = argumento.parse_args()

        if EmployeeModel.find(valor['email']):
            return {"message": "Employee with this email already exists"}, 400
        
        valor['birth_date'] = datetime.strptime(valor['birth_date'], '%Y-%m-%d').date()
        obj_employee = EmployeeModel(id, **valor)
        obj_employee.save()
        return obj_employee.json(), 201
    
    def put(self, id):
        argumento = reqparse.RequestParser()
        argumento.add_argument('name', type=str, required=True, help="Name is required")
        argumento.add_argument('birth_date', type=str, required=True, help="Birth date is required")
        argumento.add_argument('address', type=str, required=True, help="Address is required")
        argumento.add_argument('phone', type=str, required=True, help="Phone is required")
        argumento.add_argument('email',type=str, required=True, help="Email is required")
        argumento.add_argument('job_title',type=str, required=True, help="Job title is required")
        argumento.add_argument('department', type=str, required=True, help="Department is required")
        
        valor = argumento.parse_args()
        valor['birth_date'] = datetime.strptime(valor['birth_date'], '%Y-%m-%d').date()
        employee = EmployeeModel.find(id)

        if employee:
            employee.update(**valor)
            employee.save( )

            review = ReviewModel(
                employee_id=id,
                review_date=date.today(),
                summary=f"Updated info for {employee.name}"
            )
            review.save()
            
            return employee.json(), 200
        return {"message": "Employee not found"}, 404

            

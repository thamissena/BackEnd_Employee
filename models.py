from datetime import date
from conection import db



class EmployeeModel(db.Model):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key= True)  
    name = db.Column(db.String(100), nullable= False) 
    birth_date = db.Column(db.Date, nullable= False) 
    address = db.Column(db.String(200), nullable= False)
    phone = db.Column(db.String(15), nullable= False)
    email = db.Column(db.String(100),unique =True, nullable= False)
    job_title = db.Column(db.String(50), nullable= False)
    department = db.Column(db.String(50), nullable= False)
    reviews = db.relationship('ReviewModel', backref="EmployeeModel", lazy=True)

    def __init__(self,id, name, birth_date, address, phone, email, job_title, department):
        self.id = id  
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.phone = phone 
        self.email = email
        self.job_title = job_title
        self.department = department
   
    def age_caculate(self):
         age = date.today().year - self.birth_date.year - ((date.today.month, date.today.day) < (self.birth_date.month, self.birth_date.day))
         return age
    
    def last_review_summary(self):
            if self.reviews:
                last_review = max(self.reviews, key=lambda r: r.review_date)
                return f"Review on {last_review.review_date}: {last_review.summary}"
            return None
       
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age":self.age_caculate() ,
            "phone":self.phone ,
            "email": self.email,
            "job_title": self.job_title,
            "department": self.department,
            "last_review_summary": self.last_review_summary()
        }
        
    @classmethod
    def find(cls,id):
        return cls.query.filter_by(id = id).first()
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
        
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self,name, birth_date, address, phone, email, job_title, department):
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.phone = phone 
        self.email = email
        self.job_title = job_title
        self.department = department
        db.session.commit()
           
    
class ReviewModel(db.Model):
    __tablename__ = "review"

    id = db.Column (db.Integer, primary_key= True)
    employee_id = db.Column (db.Integer, db.ForeignKey('employee.id'), nullable = False)
    review_date = db.Column (db.Date, nullable= False) 
    summary = db.Column (db.Text, nullable= False)  

    def __init__(self,id, employee_id, review_date,  summary):
        self.id = id  
        self.employee_id = employee_id
        self.review_date = review_date
        self. summary =  summary
       

    @classmethod
    def find(cls,id):
        return cls.query.filter_by(id = id).first()
        
        
    def save(self):
        db.session.add(self)
        db.session.commit()


   
   
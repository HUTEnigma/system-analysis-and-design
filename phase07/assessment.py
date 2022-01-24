import database

class Assessment:
    
    def __init__(self, StudentID, term , course):
        self.StudentID = str(StudentID)
        self.term = term
        self.course = course
    def through_Courses(self, course_name):
        db, dbconnection = database.get_database_connection()
        db.execute(f'select * from arzeshyabi where course_name = "{course_name}"')
        arzeshyabiquery = db.fetchall()
    def show_Teacher_courseNum(self, teacher_id):
        db, dbconnection = database.get_database_connection()
        db.execute(f'select * from arzeshyabi where teacher_id = {teacher_id}')
        arzeshyabiquery = db.fetchall()
        
    def Question_List(self):
        db, dbconnection = database.get_database_connection()
        db.execute(f'select * from questions')
        questions = db.fetchall()
        print(questions)
    def Answers():
        pass 
    def submit():
        pass
    def search():
        pass 
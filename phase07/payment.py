import database
class payment:
    def __init__(self , studentID , type ):
        self.studentID = studentID
        self.type = type 
    def show_debt(self):
        db, dbconnection = database.get_database_connection(False)
        db.execute(f'select debt from student where STU_id = {self.studentID}')
        debt = db.fetchone()
        print(debt)
    def send_to_payment():
        pass
    def check_debt():
        pass 
    def Type_recognition():
        pass 
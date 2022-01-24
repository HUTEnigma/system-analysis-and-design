from audioop import avg
from student import student
import pymysql
import database
import time

class course_taking :
    
   
    def __init__(self , courseID= '',module = '' , studentID='' , givendate='' , giventime='' , type=''):
        self.courseID = courseID
        self.module = module
        self.studentID = studentID
        self.givendate = givendate
        self.giventime = giventime
        self.type = type  
    @staticmethod
    def check_given_timedate(givendate ,giventime ):
        sal = '2021/01/20'
        zaman = '01:01:00'
        givendate = time.strptime(givendate , r'%Y/%m/%d')
        giventime = time.strptime(giventime , r'%H:%M:%S')
        sal = time.strptime(sal, r'%Y/%m/%d')
        zaman = time.strptime(zaman , r'%H:%M:%S')
        if givendate >= sal and giventime >= zaman:
            return True
        else : 
            print("تاریخ انتخاب واحد شما گذشته است و اجازه دسترسی به این قسمت را ندارید")
            return False
        
   
    def check_Requierdcourse(self, course_name, student_id, teacher_id, moadel):
        
        db, dbconnection = database.get_database_connection()
        
        check_avg = self.check_Avg(moadel)
        if check_avg == False:
            return
        
        check_group = self.check_Group(self , course_name, teacher_id, student_id )
        if check_group == False:
            return
        db.execute(f'select * from student where STU_id = {student_id}')
        student = db.fetchone()
        dbconnection.cursorclass= pymysql.cursors.DictCursor
       
        if student == None:
            print('daneshjooyi ba in id vojood nadarad')
            return
        
        db.execute(f'select * from erae_shode where course_name = "{course_name}" and sem_num = {1} and teacher_id={teacher_id}')
        erae_shode = db.fetchone()
        if erae_shode == None:
            print('in dars dar in term erare nashode')
            return
        
        db.execute(f'select * from pishniaz where course_name = "{course_name}" ')
        pishniaz_row = db.fetchone()
        courses = list()
        if pishniaz_row != None:
            if pishniaz_row['course1'] != '':
                courses.append(pishniaz_row['course1'])
            if pishniaz_row['course2'] != '':
                courses.append(pishniaz_row['course2'])
            if pishniaz_row['course3'] != '':
                courses.append(pishniaz_row['course3'])
        akhz_shode_ha_query = []
        if(len(courses) >= 1):

            db.execute(f'select course_name, teacher_id from akhz_kardan where STU_id = {student_id} and status = "pass"')
            akhz_shode_ha_query = db.fetchall()
            akhz_shode_ha = map(lambda x: x['course_name'], akhz_shode_ha_query)
            for pishniaz in courses:
                if pishniaz not in akhz_shode_ha:
                    print(f'shoma pishniaze in dars ra ba name {pishniaz} pas nakardaid')
                    return
                    
        if self.check_finaldateTime(student_id, course_name, teacher_id, akhz_shode_ha_query )== False:
            return

        self.add_course(student_id ,course_name, teacher_id , erae_shode)
        
        
    def check_finaldateTime(self, student_id, course_name, teacher_id, akhz_shode_ha):
        db, dbconnection = database.get_database_connection()
        db.execute(f'select * from erae_shode where course_name = "{course_name}" and teacher_id = {teacher_id}')
        erae_shode = db.fetchone()
        for akhz_shode in akhz_shode_ha:
            db.execute(f'select * from erae_shode where course_name = "{akhz_shode["course_name"]}" and teacher_id = {akhz_shode["teacher_id"]}')
            query = db.fetchone()
            saat_emtehan = query['saat_emtehan']
            tarihk_emtehan = query['tarihk_emtehan']
            if erae_shode['tarihk_emtehan'] ==  tarihk_emtehan and erae_shode['saat_emtehan'] == saat_emtehan:
                print('saat emtehane darse shoma tadakhol darad')
                return False
        return True
                
    def add_course(self, student_id ,course_name, teacher_id , erae_shode):
        db, dbconnection = database.get_database_connection()
        D_name = erae_shode["D_name"]    
        db.execute(f'insert akhz_kardan (STU_id, course_name, teacher_id, d_name, sem_num) values ({student_id}, "{course_name}", {teacher_id}, "{D_name}", "{1}")')
        dbconnection.commit()
        print('dars ba movafaghiat baraye shoma bardashte shod')
        
        
    def delete_course(self, course_name, student_id, teacher_id):
        db, dbconnection = database.get_database_connection()
        db.execute(f'delete from akhz_kardan where course_name="{course_name}" and STU_id = {student_id} and teacher_id = {teacher_id}')
        dbconnection.commit()
        print("dars ba movafaghiat hazf shod")
    def check_Group(self , goroh_darsi, course_name, teacher_id, student_id ):
        db, dbconnection = database.get_database_connection()
        
        db.execute(f'select educationalGroup from student where STU_id = {student_id}')
        gorooh_darsi = db.fetchone()['educationalGroup']
        
        db.execute(f'select course_group from course where course_name = "{course_name}", teacher_id = {teacher_id}')
        group = db.fetchone()
        if(group['course_group'] != goroh_darsi):
            self.send_Error('in dars baraye goroohe darsie shoma eraee nashode ast')
            return False
        return True
    def send_Error(self, error):
        print(error)
    def Check_MinMax_Moudle(self, tedad_vahedha):
        db, dbconnection = database.get_database_connection()
        db.execute(f'select * from akhz_kardan where STU_id = {self.student_id} and status = "progress"')
        courses = db.fetchall()
        all_vahed = 0
        for course_row in courses:
            db.execute(f'select vahed from course where course_name = "{course_row["course_name"]}"')
            vahed = db.fetchone()
            vahed = vahed['vahed']
            all_vahed = all_vahed + int(vahed)
        db.execute(f'select vahed from course where course_name = "{self.course_name}"')
        vahed = db.fetchone()
        vahed = vahed['vahed']
        all_vahed = all_vahed + int(vahed)
        if all_vahed > tedad_vahedha:
            self.send_Error('tedad vahed haye shoma az hade mojaz gozashte ast')
            return False
        return True
    def check_Avg(self, avg_score):
        avg_score = int(avg_score)
        if avg_score <= 12:
            return self.Check_MinMax_Moudle(3)
        if avg_score >= 12 and avg_score < 17:
            return self.Check_MinMax_Moudle(20)
        if avg_score >= 17:
            return self.Check_MinMax_Moudle(24)   
    def send_request():
        pass 
    def Type_recognition():
        pass
    def show_preRegitery(self):
        db, dbconnection = database.get_database_connection()
        db.execute(f'select * from akhz_kardan where STU_id = {self.student_id} and status = "progress"')
        akhz_shodeha = db.fetchall()
        print(akhz_shodeha)
    def submit():
        pass 
    def search():
        pass 
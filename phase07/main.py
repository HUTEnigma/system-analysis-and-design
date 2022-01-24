from assessment import Assessment
from student import student
from course_taking import course_taking
import time
import mysql.connector

now = time.localtime()
sal = time.strftime(r"%Y/%m/%d", now)
zaman = time.strftime(r'%H:%M:%S', now)
course_taking.check_given_timedate(sal, zaman)

""" dbcursor.execute('select * from student')
result = dbcursor.fetchall() """
print ('agar mikahid darsi ra ezafe konid 1 ra varod konid va agar mikhahid darsi ra hazf konid 2 ra vared konid ')
vorodi = input ("number")
print('lotfan name dars va shomare daneshjooie khod ra vared konid')
course_name = input('name dars')
student_id = input('shomare daneshjooyi')
teacher_id = input('shamare teacher')
moadel = input('moadel')
course_obj = course_taking()
course_obj.course_name = course_name
course_obj.student_id = student_id
course_obj.teacher_id = teacher_id
if vorodi == '1' :
    course_obj.check_Requierdcourse(course_name, student_id, teacher_id , moadel )
if vorodi == '2' :
    course_obj.delete_course(course_name, student_id, teacher_id)

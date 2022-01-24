class login:
    def init(self,userID,password,securityCode,type):
        self.userID = userID
        self.password = password
        self.securityCode = securityCode
        self.type = type


    def Check_User_Pass_Student(self):
		# SELECT * FROM student WHERE student_id = ?
        student = getStudent(self.userID)
        if student.password != self.password:
			Send_Error('Wrong Credentials')

    def Check_User_Pass_Teacher(self):
		# SELECT * FROM teacher WHERE teacher_id = ?
        teacher = getTeacher(self.userID)
        if teacher.password != self.password:
			Send_Error('Wrong Credentials')

    def Check_User_Pass_Member(self):
        # SELECT * FROM member WHERE member_id = ?
        member = getTeacher(self.userID)
        if member.password != self.password:
			Send_Error('Wrong Credentials')

    def Check_SecurityCode(self, code):
        if self.securityCode != code:
			Send_Error('Security Code Does Not Match')

    def Log_in(self):
        if self.type == 'student':
			Check_User_Pass_Student()
		elif self.type == 'teacher':
			Check_User_Pass_Teacher()
		elif self.type == 'member':
			Check_User_Pass_Member()
		else Send_Error('Unknown User Type')
		
		Check_SecurityCode()
		return True

    def Send_Error(self, msg):
        raise Exception(msg)


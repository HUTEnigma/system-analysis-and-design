from person import person


class student(person):
    person_obj = None
    def __init__(self , daneshjo, studentNum , avg , degree , course , status , department , 
     orientation , highschoolName , lastDegreeAvg , firstNameEng , lastNameEng , password ,
     firstName , lastName , fatherName , nationalCode , birthDate ,selPhoneNum 
        , address , cityofResidence , birthcertificatecode , postalcode , birthcity , deen , 
        homeNum , nationality , maritalstatus , lastdegree , lastdegreeenddate , sex , dutysystemstatus , email):
        self.person_obj = daneshjo
        self.studentNum = studentNum
        self.avg = avg
        self.degree = degree
        self.course = course
        self.status = status
        self.department = department
        self.orientation = orientation
        self.highschoolName = highschoolName
        self.lastDegreeAvg = lastDegreeAvg
        self.firstNameEng = firstNameEng
        self.lastNameEng = lastNameEng
        self.password = password
        self.firstName = firstName
        self.lastName = lastName 
        self.fathername = fatherName
        self.nationalCode = nationalCode
        self.birthDate = birthDate
        self.selPhoneNum = selPhoneNum
        self.address = address
        self.cityofResidence = cityofResidence
        self.birthcertificatecode = birthcertificatecode
        self.postalcode = postalcode
        self.birthcity = birthcity
        self.deen = deen
        self.homeNum = homeNum
        self.nationality = nationality
        self.maritalstatus = maritalstatus
        self.lastdegree = lastdegree
        self.lastdegreeenddate = lastdegreeenddate
        self.sex = sex
        self.dutysystemstatus = dutysystemstatus
        self.email = email
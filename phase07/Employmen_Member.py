class Employment:	
    def __init__(self,personalCode,insuranceType,insuranceCode,Salary,bankAccNum,lastDegreeUniName,employmentDate,type,officeNum,vacationDate,firstName,lastName
				fatherName,nationalCode,birthDate,selPhoneNum,,address,cityofResidence,birthcertificatecode,postalcode,birthcity,deen,homeNum,nationality,
				maritalstatus,lastdegree, lastdegreeenddate, sex, dutysystemstatus, email):
        self.personalCode = personalCode
        self.insuranceType = insuranceType
        self.insuranceCode = insuranceCode
        self.Salary = Salary
        self.bankAccNum = bankAccNum
        self.lastDegreeUniName = lastDegreeUniName
        self.employmentDate = employmentDate
        self.type = type
        self.officeNum = officeNum
        self.vacationDate = vacationDate
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
        
class Teacher(Employment):
    def __init__(self,personalCode,insuranceType,insuranceCode,Salary,bankAccNum,lastDegreeUniName,employmentDate,officeNum,vacationDate,type,department,course,password):
        super().__init__(personalCode,insuranceType,insuranceCode,Salary,bankAccNum,lastDegreeUniName,employmentDate,officeNum,vacationDate,type,firstName,lastName
				fatherName,nationalCode,birthDate,selPhoneNum,,address,cityofResidence,birthcertificatecode,postalcode,birthcity,deen,homeNum,nationality,
				maritalstatus,lastdegree, lastdegreeenddate, sex, dutysystemstatus, email)
        
        self.department = department
        self.course = course
        self.type = type
        self.password = password

class Member(Employment):
    def __init__(self,personalCode,insuranceType,insuranceCode,Salary,bankAccNum,lastDegreeUniName,employmentDate,officeNum,vacationDate,type,department,password):
        super().__init__(personalCode,insuranceType,insuranceCode,Salary,bankAccNum,lastDegreeUniName,employmentDate,officeNum,vacationDate,type,firstName,lastName
				fatherName,nationalCode,birthDate,selPhoneNum,,address,cityofResidence,birthcertificatecode,postalcode,birthcity,deen,homeNum,nationality,
				maritalstatus,lastdegree, lastdegreeenddate, sex, dutysystemstatus, email)

        self.department = department
        self.type = type
        self.password = password

class Employment:
    def __init__(self,personalCode,insuranceType,insuranceCode,Salary,bankAccNum,lastDegreeUniName,employmentDate,type,officeNum,vacationDate):
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
        
class Teacher(Employment):
    def __init__(self,personalCode,insuranceType,insuranceCode,Salary,bankAccNum,lastDegreeUniName,employmentDate,officeNum,vacationDate,type,department,course,password):
        super().__init__(personalCode,insuranceType,insuranceCode,Salary,bankAccNum,lastDegreeUniName,employmentDate,officeNum,vacationDate,type)
        
        self.department = department
        self.course = course
        self.type = type
        self.password = password

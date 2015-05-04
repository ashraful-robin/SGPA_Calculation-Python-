"""

	Every time I tell the word I am a beginner. So still I am learning. In the learning time I have create some files.
	It's one of then.

	It's a simple OOP concept. It's for calculating SPGA of a semester. 

"""

class SGPA_Calculation:

    def __init__(self):
        self.n_course = 0
        self.total_credit = 0.0
        self.courseCode = []
        self.courseCredit = []
        self.courseGradePoint = []
        self.sgpa = 0.0
        self.temp = 0
        self.temp2 = 0
        self.temp3 = 0
        self.temp4 = 0
        self.temp5 = 0

    def inpuT(self):
        self.total_credit = eval(input("Enter total credit of this semester :"))
        self.n_course = int(input("How many courses you have : "))
        print ("OK! Enter one by one \n")
        for i in range(0,self.n_course):
            self.temp = input("Course Name %d : " %(i+1))
            self.courseCode.append(self.temp)
            self.temp2 = int(input("%s Credit Hour : " %self.courseCode[i]))
            self.courseCredit.append(self.temp2)
            self.temp3 = int(input("%s Grade Point : " %self.courseCode[i]))
            self.courseGradePoint.append(self.temp3)

    def calculation(self):
        for i in range(0,self.n_course):
            self.temp5 = self.courseGradePoint[i] * self.courseCredit[i]
            self.temp4 = self.temp4 + self.temp5
        self.sgpa = (self.temp4 / self.total_credit)


    def outpuT(self):
        print ("Your Courses : \n%s\n" %self.courseCode)
        for i in range(0,self.n_course):
            print ("Credit of %s = %d" %(self.courseCode[i], self.courseCredit[i]))
            print("Grade Point of %s = %d" %(self.courseCode[i], self.courseGradePoint[i]))
        print ("\nYour SGPA is : %.2f" %(self.sgpa))

ob = SGPA_Calculation()     # ob is an object of SGPA_Calculation Class

ob.inpuT()                  # I am are calling inpuT() function

ob.calculation()			# I am calling here the calculation() function

ob.outpuT()					# As well as calling the outpuT() function

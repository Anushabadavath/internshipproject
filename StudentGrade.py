class Student():
    def studdata(self) :
        self.name=input("ENTER STUDENT NAME: ")
        print("ENTER ALL TEST MARKS")
        print("------------------------------")
        self.Telugu = int(input("Enter Telugu Marks:"))
        self.Hindi = int(input("Enter Hindi Marks:"))
        self.English = int(input("Enter English Marks:"))
        self.Science = int(input("Enter Science Marks:"))
        self.Social = int(input("Enter Social Marks:"))
        self.Maths= int(input("Enter Maths Marks:"))
    def studtot(self):
        self.totmar = (self.Telugu+self.Hindi+self.English+self.Maths+self.Science+self.Social)
        print("Total marks={}".format(self.totmar))
        print("*"*50)
        self.Percent= round((self.totmar/600)*100,2)
        print("Student Percentage ={}".format(self.Percent))
        print("*"*50)
    def studgrade(self):
        if(self.totmar >=600):
            print("Student Grade = A")
        elif(self.totmar >= 500):
            print("Student Grade = B")
        elif(self.totmar >= 400):
            print("Student Grade = C")
        elif(self.totmar >= 300):
            print("Student Grade = D")
            print("*"*50)
    def studcomment(self) :
        if(self.totmar >=90):
            print("Excellent")
        elif(self.totmar >=80):
            print("Good")
        elif self.totmar >=70:
            print("Satisfactory")
        elif (self.totmar >=60):
            print("Need Improvement")
        elif (self.totmar >=50):
            print("Poor")
            print("*"*50)
#Main program
s=Student()
s.studdata()
s.studtot()
s.studgrade()
s.studcomment()


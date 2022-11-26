# Write a program that has a class person storing name and date of birth (DOB) of a person. The program should subtract the DOB from today’s date to find out whether a person is eligible to vote or not using constructor (A person is eligible to vote if age is greater than or equal to 18)
import datetime
class person():
    def __init__(self, name, dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if today< datetime.date(today.year, self.dob.month, self.dob.day):
            age-=1
        if age>=18:
            print("Congratulation!! {}, you are eligible to vote.".format(self.name))
        else:
            print("Oops... Sorry!! {}, You should be at least 18 years of age to cast your vote.".format(self.name))
name=input("Enter your name: ")
dob_str=input("Enter your date of birth (yyyy/mm/dd): ")
# dob=datetime.date(int(dob_str[0]), int(dob_str[1]), int(dob_str[2]))
dob=datetime.datetime.strptime(dob_str, "%Y/%m/%d").date()



print(name, " , Your date of birth is: ", dob)
p=person(name, dob)
p.check()
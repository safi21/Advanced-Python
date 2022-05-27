import datetime

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def calculate_age(self):
        dob = self.dob.split('-')
        year, month, day = map(int, dob)
        birthdate = datetime.date(year, month, day)
        today = datetime.date.today()
        return today.year-birthdate.year -((today.month, today.day) < (birthdate.month, birthdate.day))

if __name__ == "__main__":
    name = input("Enter your name: ")
    dob = input("Enter your date of birth: ")
    person = Person(name, dob)
    age = person.calculate_age()
    print("Age of {} is {}".format(name, age))
from datetime import date

class Employee:
    def __init__(self, name, nationality, birth):
        self.name = name
        self.nationality = nationality
        self.birth = birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birth.year
        if today < date(today.year, self.birth.month, self.birth.day):
            age -= 1
        return age

person1 = Employee("Rima", "French", date(1973, 3, 12))
person2 = Employee("Jun", "American", date(1990, 8, 9))

print(f'{person1.name} is {person1.calculate_age()}')
print(f'{person2.name} is {person2.calculate_age()}')


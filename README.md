
# < El primer repositorio, the first repository, que uso, that i use > #


        def age(self):
         today = datetime.date.today()
         age = today.year - self.birthdate.year
        
         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
                 age -= 1
                       return age

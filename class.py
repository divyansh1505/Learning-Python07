class Employee:
    language = "py"
    salary = "1250000"

#ab me jisko bhi employee bna dunga, fir uski lang or salary 
# python or 12.5 lakh hojayegi

shraddha = Employee()
shraddha.name = "Shraddha"
print(shraddha.name, shraddha.language, shraddha.salary)

aman = Employee()
aman.name = "Aman"
print(aman.name, aman.language, aman.salary)

# Here name is object attribute, salary and language are 
# class attributes as they directly belong to the class

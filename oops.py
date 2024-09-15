class Employee:
    language = "py"    #class attribute
    salary = "1250000"


shraddha = Employee()
shraddha.language = "JavaScript"   #instance attribute
print(shraddha.language, shraddha.salary)

# Instance attributes, take preference over class attributes during assignment &
# retrieval.
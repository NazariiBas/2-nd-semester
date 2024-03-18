class Auditorium:
    '''
    Клас що описує Аудиторію
    self.number - номер аудиторії
    self.capacity - вмістимість аудиторії
    self,equipment - обладнання аудиторії(якщо воно є)

    '''
    
    def __init__(self, number, capacity, equipment=None):
        self.number = number  
        self.capacity = capacity  
        self.equipment = equipment or []  

    def __str__(self):
        return f"Auditorium {self.number} (Capacity: {self.capacity}, Equipment: {', '.join(self.equipment)})"

    def add_equipment(self, equipment):
        self.equipment.append(equipment)

    def remove_equipment(self, equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)


class UniversityAuditorium(Auditorium):
    '''
    Клас що описує тип аудиторії який наслідує клас аудиторій
    '''
    def __init__(self, number, capacity, equipment=None, building=None):
        super().__init__(number, capacity, equipment)
        self.building = building  

    def __str__(self):
        return f"University Auditorium {self.number} (Capacity: {self.capacity}, Building: {self.building}, Equipment: {', '.join(self.equipment)})"



auditorium1 = Auditorium("101", 50, ["Projector", "Whiteboard"])
print(auditorium1)

university_auditorium1 = UniversityAuditorium("101", 100, ["Projector", "Whiteboard"], "Main Building")
print(university_auditorium1)

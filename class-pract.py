class Auditorium:
    def __init__(self, number, capacity, equipment):
        self.number = number  
        self.capacity = capacity  
        self.equipment = equipment  

    def display_info(self):
        print(f"Auditorium {self.number}:")
        print(f"Capacity: {self.capacity} seats")
        print("Equipment:")
        for item in self.equipment:
            print(f"- {item}")


auditorium1 = Auditorium(101, 50, ["projector", "whiteboard", "computers"])
auditorium2 = Auditorium(102, 30, ["whiteboard", "chairs", "tables"])

auditorium1.display_info()
print()
auditorium2.display_info()

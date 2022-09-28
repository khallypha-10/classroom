


def my_dict(**kwargs):
    return kwargs
 
d = my_dict(name='sulaiman', id_num='1500603' )

class Lesson():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.students = []


    def add_student(self,d):
        
        if not self.quota():
            return False
        self.students.append(d)
        return True

    def quota(self):
        return self.capacity - len(self.students)
    

    


school = Lesson(25)


sucess = school.add_student(d)


print(f"{d} has enrolled into the class")

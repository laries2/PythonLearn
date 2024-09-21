class Robot:
    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = "30"
r1.introduce_self()


# Better way to work with objects
class Department:
    def __init__(self, category, supervisor, members):
        self.category = category
        self.supervisor = supervisor
        self.members = members

    def details(self):
        print("Category: " + self.category)
        print("supervisor: " + self.supervisor)
        print("Number of Members: ", self.members)

d1 = Department("ict", "Hillary Bett", 88)


d1.details()
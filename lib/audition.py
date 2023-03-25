
class Audition:

    all= []

    def __init__(self, actor, location, hired, role):
        self.actor = actor
        self.location = location
        self.hired = hired
        self.role = role
        Audition.all.append(self)


    def what_role(self):
        return self.role

    def call_back(self):
        if self.hired is False:
            self.hired = True
        elif self.hired is True:
            print("You have already called and hired this actor.")


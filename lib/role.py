from .audition import Audition

class Role:

    all= []

    def __init__(self, character_name):
        self.character_name = character_name
        Role.all.append(self)

    @property
    def auditions(self):
        return [a for a in Audition.all if a.role == self]
    
    @property
    def actors(self):
        return [a.actor for a in self.auditions()]
    
    @property
    def locations(self):
        return [l.location for l in self.auditions()]
    
    @property
    def lead(self):
        for a in self.auditions():
            if a.hired is True:
                return a.actor
            return print("No actor has been hired for this role.")

    @property
    def understudy(self):
        if self.auditions[1].hired is True:
            return self.auditions[1].actor
        return print("No actor has been hired for understudy for this role.")




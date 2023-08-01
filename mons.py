from random import randint

class Egg():
    def __init__(self):
        self.lifespan = 60000
    
class Baby():
    def __init__(self):
        self.lifespan = 120000
        self.happiness = 0
        self.max_happiness = 10
        self.hunger = 0
        self.max_hunger = 10
        if randint(0, 100) > 50:
            self.sex = "Male"
        else:
            self.sex = "Female"
        self.items = []

class Teen():
    def __init__(self, sex, items):
        self.lifespan = 60000
        self.happiness = 0
        self.max_happiness = 10
        self.hunger = 0
        self.max_hunger = 10
        self.sex = sex
        self.items = items

class Adult():
    def __init__(self, sex, items):
        self.lifespan = 60000
        self.happiness = 0
        self.max_happiness = 10
        self.hunger = 0
        self.max_hunger = 10
        self.sex = sex
        self.items = items

class Elder():
    def __init__(self, sex, items):
        self.lifespan = 60000
        self.happiness = 0
        self.max_happiness = 10
        self.hunger = 0
        self.max_hunger = 10
        self.sex = sex
        self.items = items

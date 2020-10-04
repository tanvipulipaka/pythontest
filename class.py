# storage of different properties of car 
class Car(object):

    def __init__(self, model, color, company, speed_limit):

        self.color = color 
        self.company = company 
        self.speed_limit = speed_limit
        self.model = model


    def start(self):

        print("started" + self.model)

    def stop(self):

        print("stopped" + self.speed_limit)

#self is only for computer to see what property it is associated with
mercedes = Car("A6", "red", "Audi", 120)
print(mercedes.color)
print(mercedes.start())  


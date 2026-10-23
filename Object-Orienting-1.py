class vehicle: 
    def __init__(self,max_speed,milege):
        self.max_speed = max_speed
        self.milege = milege

model_x = vehicle(240,18)
print(model_x.max_speed)
print(model_x.milege)
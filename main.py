import random

class Venue():
    def __init__(self, name, x_max, y_max, origins, checkpoints):
        self.name = name
        self.x_max = x_max
        self.y_max = y_max
        self.origins = origins
        self.checkpoints = checkpoints
        self.define_persons()
    
    def define_persons(self):
        self.persons = []

        for origin in self.origins:
            for i in range(origin.flowrate):
                x = origin.x + random.randint(-origin.size, origin.size)
                y = origin.y + random.randint(-origin.size, origin.size)
                self.persons.append(Person(i, x, y, self.checkpoints))
        


class Person():
    def __init__(self, id, x, y, checkpoints):
        self.id = id
        self.x = x
        self.y = y
        self.checkpoints = checkpoints
        self.current_checkpoint = self.checkpoints[0]
        self.color  = random.randint(1, 15)
        self.in_line = False
        self.done = False

    def go(self, x, y):
        arrived_x = False
        arrived_y = False   

        if self.x < x:
            steps_x = 1
        elif self.x > x:
            steps_x = -1
        else:
            steps_x = 0
            arrived_x = True   

        if self.y < y:
            steps_y = 1
        elif self.y > y:
            steps_y = -1
        else:
            steps_y = 0
            arrived_y = True

        self.x = self.x + steps_x
        self.y = self.y + steps_y

        if arrived_x and arrived_y:
            return True
        else:
            return False

    def move(self):
        if self.go(self.current_checkpoint.x, self.current_checkpoint.y):
            try:
                self.current_checkpoint = self.checkpoints[self.checkpoints.index(self.current_checkpoint)+1]
            except:
                self.done = True


class Checkpoint():
    def __init__(self, name, x, y, flowrate):
        self.name = name
        self.x = x
        self.y = y
        self.flowrate = flowrate


class Origin():
    def __init__(self, name, x, y, size, flowrate):
        self.name = name
        self.x = x
        self.y = y
        self.size = size
        self.flowrate = flowrate


# class Line():
#     def __init__(self, origin_x, origin_y, mid_points_x, mid_points_y, checkpoint):
#         self.origin_x = origin_x
#         self.origin_y = origin_y
#         self.mid_points_x = mid_points_x
#         self.mid_points_y = mid_points_y
#         self.checkpoint = checkpoint
        
from constants import SUCCESS 

class DriveSensors:
    
    def __init__(self):
        self.pos_x = 0.0
        self.pos_y = 0.0
        pass
        
    def drive_forward_on_range(self, rangeX, speed):
        self.pos_x += rangeX
        return {'state':SUCCESS, 
                'coords':[self.pos_x,  1.0]
                }
        
    def drive_back_on_range(self, rangeX, speed):
        self.pos_x -= rangeX 
        return {'state':SUCCESS, 
                'coords':[self.pos_x,  1.0]
                }
        
    def get_cur_speed(self):
        return {'state': SUCCESS, 
                'speed': 0.0
                }
        
    
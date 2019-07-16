from variables import SUCCESS 

class Sensors_drives:
    
    def __init__():
        return
        
    def drive(self, speed):
        calc_route(self, pointX, pointY, speed)
        return [[0.0, 0.5],[0.5, 1.0],[1.0, 1.5]]
        
    def drive_on_route(self, 
        map_dots = [[0.0, 0.0], [1.1, 1.4], [2.0, 2.0]], 
        speed = 0):
        return
        
    def calc_route(self, pointXY, options = {}):
        return {'state':SUCCESS, 
                'route':[[0.0, 0.0], [1.1, 1.4], [2.0, 2.0]]}
        
    def drive_forward_on_range(self, rangeX, speed):
        self.pos_x += rangeX
        return {'state':SUCCESS, 'coords':[self.pos_x,  1.0]}
        
    def drive_back_on_range(self, rangeX, speed):
        self.pos_x -= rangeX 
        return {'state':SUCCESS, 'coords':[self.pos_x,  1.0]}
        
    
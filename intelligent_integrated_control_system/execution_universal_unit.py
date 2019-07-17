from constants import SUCCESS 

class ExecutionUniversalUnit:
        
    def __init__(self, pointX, pointY):
        self.pointX = pointX
        self.pointY = pointY
        pass

    def drive(self, speed):
        return self.calc_route(self.pointX, self.pointY, speed)
        
    def drive_on_route(self, map_dots = [[0.0, 0.0],[1.1, 1.4],[2.0, 2.0]], speed = 0):
        return {'state': SUCCESS}
        
    def calc_route(self, pointXY, options = {}):
        return {'state':SUCCESS, 
                'route':[[0.0, 0.0], [1.1, 1.4], [2.0, 2.0]]
               }
                
    def get_count_range_to_pointXY(self,pointX, pointY):
        return {'state': SUCCESS,
                'range_to_point': 9.57
               }
               
    def get_arrival_time(self):
        return {'state': SUCCESS,
                'arrival_time': 15.20
                }
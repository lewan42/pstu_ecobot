from constants import SUCCESS 

class SteeringControlUnit:
    
    def __init__(self):
        pass
        
    def turn_wheels(self, angle = 14.5):
        return {'state': SUCCESS,
                'angle wheels': angle
                }
        
    def turn_around(self,angle):
        return {'state': SUCCESS
               }
        
    def get_angle_wheels(self):
        return {'state': SUCCESS,
                'angle_wheels': 45.20
                }
        
    def check_wheels(self):
        return True
        
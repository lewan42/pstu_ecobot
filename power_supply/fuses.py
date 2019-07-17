from constants import SUCCESS

class Fuses:
    
    def __init__(self):
        pass
    
    def get_status_headlights(self):
        return {'forward_left' : SUCCESS,
                'forward_right' : SUCCESS,
                'back_left' : SUCCESS,
                'back_right' : SUCCESS
               }
               
    def get_status_breaks(self):
        return {'back_left': SUCCESS,
                'back_right': SUCCESS
               }
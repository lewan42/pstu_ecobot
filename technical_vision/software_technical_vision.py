from constants import SUCCESS

class SoftwareTechnicalVision:
    def __init__(self):
        pass
        
    def check_status_software_technical_vision(self):
        return {'state': SUCCESS,
                'position':self.get_position(),
                'speed' : self.get_cur_speed(),
                'time': self.get_cur_time(),
                'camera_zoom' : self.get_camera_zoom(),
                'angle_wheels': self.get_angle_wheels(),
                'test':12345
                }
                
# angle opu (get set)
# scan objects
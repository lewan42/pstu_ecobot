from constants import SUCCESS 
from constants import FAIL 

class BasicTurningDevice:
    def __init__(self):
        pass
        
    def get_angleZ_OPU(self):
        return {'state': SUCCESS, 'angleZ_OPU': self.angleZ_OPU}
        
    def set_angleZ_OPU(self, angle):
        try:
            self.angleZ_OPU += angle
            assert -45 < self.angleZ_OPU < 45
            return {'state': SUCCESS, 'angleZ_OPU': self.angleZ_OPU}
        except AssertionError:
            self.angleZ_OPU -= angle
            return {'state': FAIL, 'angleZ_OPU': self.angleZ_OPU}
        
    def get_angleY_OPU(self):
        return {'state': SUCCESS, 'angleY_OPU': self.angleY_OPU}
        
    def set_angleY_OPU(self, angle):
        try:
            self.angleY_OPU += angle
            assert -90 <= self.angleY_OPU <= 90
            return {'state': SUCCESS, 'angleY_OPU': self.angleY_OPU}
        except AssertionError:
            self.angleY_OPU -= angle
            return {'state': FAIL, 'angleY_OPU': self.angleY_OPU}
        
    def scan_objects(self):
        return {'state': SUCCESS,
                'object1': "table",
                'object2': "chair"}
        
    def scan_objects_on_pointXY(self, pointX, pointY):
        return {'state': SUCCESS,
                'object1': "box",
                'object2': "door"}
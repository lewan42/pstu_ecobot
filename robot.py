# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:24:04 2019

@author: student
"""

SUCCESS = 0
FAIL = 1

ANGLE_VIEW = 0 # viewing angle camera
MAX_ANGLE_OPY_LEFT = -90;
MAX_ANGLE_OPY_RIGHT = 90;

class Robot:
    
    def __init__(self):
        self.angleY_OPU = 0
        self.angleZ_OPU = 0
        self.pos_x = 0.0
        self.pos_y = 0.0
        return
        
    def drive(self, speed):
        calc_route(self, pointX, pointY, speed)
        return [[0.0, 0.5],[0.5, 1.0],[1.0, 1.5]]
        
    def drive_on_route(self, 
        map_dots = [[0.0, 0.0], [1.1, 1.4], [2.0, 2.0]], 
        speed = 0):
        return
        
    def calc_route(self, pointX = 0, pointY = 0, options = {}):
        return {'state':SUCCESS, 
                'route':[[0.0, 0.0], [1.1, 1.4], [2.0, 2.0]]}
        
    def drive_forward_on_range(self, rangeX, speed):
        self.pos_x += rangeX
        print("forward "+ str(self.pos_x))
        return {'state':SUCCESS, 'coords':[self.pos_x,  1.0]}
        
    def drive_back_on_range(self, rangeX, speed):
        self.pos_x -= rangeX 
        print("back "+str(self.pos_x))
        return {'state':SUCCESS, 'coords':[self.pos_x,  1.0]}
        
    def turn_wheels(self, angle = 14.5):
        return {'state': SUCCESS,
                'angle wheels': angle}
        
    def turn_around(self,angle):
        return {'state': SUCCESS}
        
    def scan_objects(self):
        return {'state': SUCCESS,
                'object1': "table",
                'object2': "chair"}
        
    def scan_objects_on_pointXY(self, pointX, pointY):
        return {'state': SUCCESS,
                'object1': "box",
                'object2': "door"}
        
    def get_count_range_to_pointXY(self,pointX, pointY):
        return {'state': SUCCESS,'range_to_point': 9.57}
        
    def check_status(self):
        return {'state': SUCCESS,
                'position':self.get_position(),
                'speed' : self.get_cur_speed(),
                'time': self.get_cur_time(),
                'camera_zoom' : self.get_camera_zoom(),
                'angle_wheels': self.get_angle_wheels(),
                'test':12345}
        
    def get_cur_speed(self):
        return {'state': SUCCESS, 'speed': 0.0}
        
    def get_cur_time(self):
        return {'state': SUCCESS,'time': 14.54}
        
    def get_position(self):
        return {'state': SUCCESS,
                'posX': 0.5,
                'posY': 1.5}
                
    def get_camera_zoom(self):
        return {'state': SUCCESS, 'camera_zoom': 1.0}
        
    def get_arrival_time(self):
        return {'state': SUCCESS, 'arrival_time': 15.20}
        
    def get_angleZ_OPU(self):
        return {'state': SUCCESS, 'angleZ_OPU': self.angleZ_OPU}
        
    def set_angleZ_OPU(self, angle):
        try:
            self.angleZ_OPU += angle
            assert -45 < self.angleZ_OPU < 45
            print ("angleZ " + str(self.angleZ_OPU), SUCCESS)
            return (self.angleZ_OPU, SUCCESS)
        except AssertionError:
            print ("angleZ " + str(self.angleZ_OPU), FAIL)
            return (self.angleZ_OPU, FAIL)
        
    def get_angleY_OPU(self):
        return {'state': SUCCESS, 'angleY_OPU': self.angleY_OPU}
        
    def set_angleY_OPU(self, angle):
        try:
            self.angleY_OPU += angle
            assert -90 < self.angleY_OPU < 90
            print ("angleY " + str(self.angleY_OPU), SUCCESS)
            return (self.angleY_OPU, SUCCESS)
        except AssertionError:
            print ("angleY " + str(self.angleY_OPU), FAIL)
            return (self.angleY_OPU, FAIL)

            
    def check_wheels(self):
        return True
        
    def get_angle_wheels(self):
        return {'state': SUCCESS, 'angle_wheels': 45.20}
        
    def powef_on(self):
        return {'state': SUCCESS, 'status': "power_on"}
        
    def power_off(self):
        return {'state': SUCCESS, 'status': "power_off"}
        
    
        
    
        
    
        
        
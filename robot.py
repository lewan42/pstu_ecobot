# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:24:04 2019

@author: student
"""

class Robot:
    
    def __init__(self):
        return
        
    def drive(self, speed):
        calc_route(self, pointX, pointY, speed)
        return [[0.0, 0.5],[0.5, 1.0],[1.0, 1.5]]
        
    def drive_on_route(self, map_dots = [[0.0, 0.0], [1.1, 1.4], [2.0, 2.0]], speed):
        return
        
    def calc_route(self, pointX, pointY, speed):
        return [[0.0, 0.0], [1.1, 1.4], [2.0, 2.0]]
        
    def drive_forward_on_range(self, rangeX, speed):
        return [1.0, 1.0]
        
    def drive_back_on_range(self, rangeX, speed):
        return [-1.0, -1.0]
        
    def turn_wheels(self, angle):
        return []
        
    def turn_around(self,angle):
        return []
        
    def scan_objects(self):
        return []
        
    def scan_objects_on_pointXY(self, pointX, pointY):
        return []
        
    def get_count_range_to_pointXY(self,pointX, pointY):
        return {'range to point': 9.57}
        
    def check_status(self):
        return {'position':get_position(self),
                'speed' : get_cur_speed(self),
                'time': get_cur_time(self),
                'camera zoom' : get_camera_zoom(self),
                'angle wheels': get_angle_wheels(self)}
        
    def get_cur_speed(self):
        return {'speed': 0.0}
        
    def get_cur_time(self):
        return {'time': 14.54}
        
    def get_position(self):
        return {'posX': x,
                'posY': y}
                
    def get_camera_zoom(self):
        return {'camera zoom': 1.0}
        
    def get_arrival_time(self):
        return {'arrival time': 15.20}
        
    def check_wheels(self):
        return True
        
    def get_angle_wheels(self):
        return 45.0
        
    def powef_on(self):
        return
        
    def power_off(self):
        return
        
    
        
    
        
    
        
        
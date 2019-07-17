# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:24:04 2019

@author: student
"""
import fractal_path_finder as fpf
import drive_sensors as ds

#transfer to variable.py
#SUCCESS = 0
#FAIL = 1
#ANGLE_VIEW = 0 # viewing angle camera
#MAX_ANGLE_OPY_LEFT = -90;
#MAX_ANGLE_OPY_RIGHT = 90;

class Robot:
    
    def __init__(self):
        self.angleY_OPU = 0
        self.angleZ_OPU = 0
        self.pos_x = 0.0
        self.pos_y = 0.0
        return
        
#transfer to driver_sensors.py
    #def drive(self, speed):
     #   calc_route(self, pointX, pointY, speed)
      #  return [[0.0, 0.5],[0.5, 1.0],[1.0, 1.5]]
        
    #def drive_on_route(self, 
     #   map_dots = [[0.0, 0.0], [1.1, 1.4], [2.0, 2.0]], 
      #  speed = 0):
       # return
        
    #def drive_forward_on_range(self, rangeX, speed):
     #   self.pos_x += rangeX
        #print("forward "+ str(self.pos_x))
      #  return {'state':SUCCESS, 'coords':[self.pos_x,  1.0]}
        
    #def drive_back_on_range(self, rangeX, speed):
     #   self.pos_x -= rangeX 
      #  print("back "+str(self.pos_x))
       # return {'state':SUCCESS, 'coords':[self.pos_x,  1.0]}
        
        
   # def calc_route(self, pointXY, options = {}):
    #    return {'state':SUCCESS, 
     #           'route':[[0.0, 0.0], [1.1, 1.4], [2.0, 2.0]]}
        
      #TRANSFER TO BLOCK_RUDDER_CONTROL  
   # def turn_wheels(self, angle = 14.5):
    #    return {'state': SUCCESS,
     #           'angle wheels': angle}
        
    #def turn_around(self,angle):
     #   return {'state': SUCCESS}
        
    #to Basic_turning_device    
  #  def scan_objects(self):
   #     return {'state': SUCCESS,
    #            'object1': "table",
     #           'object2': "chair"}
        
    #def scan_objects_on_pointXY(self, pointX, pointY):
     #   return {'state': SUCCESS,
      #          'object1': "box",
       #         'object2': "door"}
       
       #to block_execution universal
   # def get_count_range_to_pointXY(self,pointX, pointY):
    #    return {'state': SUCCESS,'range_to_point': 9.57}
     
     #to software_iisc
   # def check_status(self):
    #    return {'state': SUCCESS,
    #            'position':self.get_position(),
     #           'speed' : self.get_cur_speed(),
      #          'time': self.get_cur_time(),
       #         'camera_zoom' : self.get_camera_zoom(),
        #        'angle_wheels': self.get_angle_wheels(),
         #       'test':12345}
        
        #to sensors drives
    #def get_cur_speed(self):
      #  return {'state': SUCCESS, 'speed': 0.0}
        
    def get_cur_time(self):
        return {'state': SUCCESS,'time': 14.54}
      
      #transfer to inertial navigation system
   #def get_position(self):
   #     return {'state': SUCCESS,
    #            'posX': 0.5,
     #           'posY': 1.5}
     
#to stereo camera    
 #   def get_camera_zoom(self):
  #      return {'state': SUCCESS, 'camera_zoom': 1.0}
    
#to EXECUTION UNIVERSAL UNIT    
  #  def get_arrival_time(self):
   #     return {'state': SUCCESS, 'arrival_time': 15.20}
        
        # basic turning device
  #  def get_angleZ_OPU(self):
   #     return {'state': SUCCESS, 'angleZ_OPU': self.angleZ_OPU}
        
   # def set_angleZ_OPU(self, angle):
    #    try:
     #       self.angleZ_OPU += angle
      #      assert -45 < self.angleZ_OPU < 45
       #     return {'state': SUCCESS, 'angleZ_OPU': self.angleZ_OPU}
       # except AssertionError:
        #    self.angleZ_OPU -= angle
         #   return {'state': FAIL, 'angleZ_OPU': self.angleZ_OPU}
        
    #def get_angleY_OPU(self):
     #   return {'state': SUCCESS, 'angleY_OPU': self.angleY_OPU}
        
    #def set_angleY_OPU(self, angle):
     #   try:
      #      self.angleY_OPU += angle
       #     assert -90 <= self.angleY_OPU <= 90
        #    return {'state': SUCCESS, 'angleY_OPU': self.angleY_OPU}
        #except AssertionError:
         #   self.angleY_OPU -= angle
          #  return {'state': FAIL, 'angleY_OPU': self.angleY_OPU}

     #to block rudder control       
  #  def check_wheels(self):
   #     return True
        
   # def get_angle_wheels(self):
    #    return {'state': SUCCESS, 'angle_wheels': 45.20}
        
        #to POWER SUPPLY
 #   def powef_on(self):
  #     return {'state': SUCCESS, 'status': "power_on"}
        
   # def power_off(self):
    #    return {'state': SUCCESS, 'status': "power_off"}
        
    
        
    
        
    
        
        
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:24:04 2019

@author: student
"""
from constants import SUCCESS 
from intelligent_integrated_control_system.software_intelligent_integrated_control_system import SoftwareIntelligentInregratedControlSystem
from intelligent_integrated_control_system.execution_universal_unit import ExecutionUniversalUnit
from chassis.drive_sensors import DriveSensors
from technical_vision.pivot_device import PivotDevice

software_intelligent_integrated_control_system = SoftwareIntelligentInregratedControlSystem()
execution_universal_unit = ExecutionUniversalUnit(10.5, 12.6)
drive_sensors = DriveSensors()
pivot_device = PivotDevice()

class Robot:
    
    def __init__(self):
        pass
        
#transfer to driver_sensors.py
    #def drive(self, speed):
     #   calc_route(self, pointX, pointY, speed)
      #  return [[0.0, 0.5],[0.5, 1.0],[1.0, 1.5]]
        
    #def drive_on_route(self, 
     #   map_dots = [[0.0, 0.0], [1.1, 1.4], [2.0, 2.0]], 
      #  speed = 0):
       # return
        
    def drive_forward_on_range(self, rangeX, speed):
        return drive_sensors.drive_forward_on_range(rangeX, speed)
        
    def drive_back_on_range(self, rangeX, speed):
        return drive_sensors.drive_back_on_range(rangeX, speed)
        
    def calc_route(self, pointXY, options = {}):
        return execution_universal_unit.calc_route(pointXY)
        
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
     
     
    def check_status(self):
        return software_intelligent_integrated_control_system.check_status_software_intelligent_integrated_control_system()
        
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
        
    def set_angleZ_OPU(self, angle):
        return pivot_device.set_angleZ_OPU(angle) 
        
    #def get_angleY_OPU(self):
     #   return {'state': SUCCESS, 'angleY_OPU': self.angleY_OPU}
        
    def set_angleY_OPU(self, angle):
       return pivot_device.set_angleY_OPU(angle)

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
        
    
        
    
        
    
        
        
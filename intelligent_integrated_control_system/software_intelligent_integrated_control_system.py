from constants import SUCCESS 

from intelligent_integrated_control_system.strapdown_unit import StrapdownUnit
from chassis.steering_control_unit import SteeringControlUnit
from chassis.drive_sensors import DriveSensors

strapdown_unit = StrapdownUnit()
steering_control_unit = SteeringControlUnit()
drive_sensors = DriveSensors()

class SoftwareIntelligentInregratedControlSystem:
    
    def __init__(self):
        pass
        
    def check_status_software_intelligent_integrated_control_system(self):
        return {'state': SUCCESS,
                'position':strapdown_unit.get_position(),
                'speed' : drive_sensors.get_cur_speed(),
                'angle_wheels': steering_control_unit.get_angle_wheels()
                }
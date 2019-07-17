from constants import SUCCESS

class PowerSupply:
    
    def __init__(self):
        pass
    
    def powef_on(self):
        return {'state': SUCCESS,
                'status': "power_on"
                }
        
    def power_off(self):
        return {'state': SUCCESS,
                'status': "power_off"
                }
        
    
from constants import SUCCESS

from pivot_device import PivotDevice
from stereo_camera import StereoCamera


class SoftwareTechnicalVision:
    def __init__(self):
        pass
        
    def check_status_software_technical_vision(self):
        return {'state': SUCCESS,
                'get_angleZ_OPU':PivotDevice.get_angleZ_OPU(),
                'get_angleY_OPU' : PivotDevice.get_angleY_OPU(),
                'scan_objects': PivotDevice.scan_objects(),
                'camera_zoom' : StereoCamera.get_camera_zoom()
                }
                
# angle opu (get set)
# scan objects
from sensorx.sensor_set import SensorSet
from type.type import Type

class Sensor:
    def __init__(self, dim:int, freq:int, id:int=None, parent_sensor:SensorSet=None):
        self._dim = dim
        self._sensor_set_id = sensor_set_id
        self._freq = freq


    def get_heirarchical_ids(self):
        pass
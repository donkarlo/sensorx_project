from sensorx.sensor import Sensor as BaseSensor
from sensorx.sensor_set import SensorSet
from sensorx.type.type import Type


class Sensor(BaseSensor):
    def __init__(self, type:Type, id:int=None, sensor_set:SensorSet=None, freq:int=None):
        pass
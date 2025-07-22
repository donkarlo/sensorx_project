from typing import Union

from sensorx.sensor import Sensor


class SensorSet:
    '''
    Sensors of the same parent for example sensors of a robot
    '''
    def __init__(self, sensors: list[Sensor, ...], sensor_set_id=None , parent_id=None):
        '''
        For example a GPS and LIDAR in a Robot. But it can be a set of related sensors for some reason event in multiple robots
        :param sensors:
        :param parent_id: if the two sensors in this sensor set belongs to a multi robot system
        :param sensor_set_id: current body, current robot
        '''
        #@todo either it should be a set of sets or set of sensors
        # if the sensors do not have ids automatically generate unique ids
        self._sensors = sensors
        self._parent_id = parent_id
        #@todo assign automatically
        self.sensor_set_id = sensor_set_id

    def print_sensors():
        print ("To print sensors")

    def get_sensor_set_id(self):
        return self.sensor_set_id
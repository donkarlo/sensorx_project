from typing import Union

from sensorx.sensor import Sensor


class SensorSet:
    '''
    Sensors of the same parent for example member_sensors of a robot
    '''
    def __init__(self, member_sensors: list[Sensor, ...], sensor_set_id=None, parent_id=None):
        '''
        For example a GPS and LIDAR in a Robot. But it can be a set of related member_sensors for some reason event in multiple robots
        :param member_sensors:
        :param parent_id: if the two member_sensors in this sensor set belongs to a multi robot system
        :param sensor_set_id: current body, current robot
        '''
        #@todo either it should be a set of sets or set of member_sensors
        # if the member_sensors do not have ids automatically generate unique ids
        self._memeber_sensors = member_sensors
        self._parent_id = parent_id
        #@todo assign automatically
        self.sensor_set_id = sensor_set_id

    def print_sensors():
        print ("To print member_sensors")

    def get_sensor_set_id(self):
        return self.sensor_set_id
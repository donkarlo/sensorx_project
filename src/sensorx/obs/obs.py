from typing import Union
import numpy as np
from mathx.linalg.matrix.col_vec import ColVec

from sensorx.sensor import Sensor


class Obs:
    '''
    For sensor, time, obs
    '''
    def __init__(self, sensor:Sensor, time:float, col_vec:ColVec):
        self.__sensor:Sensor = sensor
        self.__time = time
        self._col_vec = col_vec
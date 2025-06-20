from typing import Union
import numpy as np

class Obs:
    '''
    For sensor, time, obs
    '''
    def __init__(self, sensor_id:int, time:float, obs_vec:ColumnVec):
        self.__sensor_id = sensor_id
        self.__time = time
        self.__vec = vec
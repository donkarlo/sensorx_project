from typing import Union
import numpy as np


class SensorSetTimeValSeq:
    def __init__(self):
        ''''''
        # it will hold sensor id as key and a single_sensor_time_val_seq as the data for that in a heirarchical order
        self._all = {}
        self._time_seq = {}
        self._val_seq = {}
        self._time_val_seq = {}



    def add_one_time_val_for_a_sensor(self
                                      , sensor
                                      , time
                                      , val:Union[list,np.ndarray]
                                      , validity_check:bool=False):
        pass
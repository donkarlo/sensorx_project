import numpy as np

from sensorx.sensor import Sensor
from sensorx.time_value.time_val import TimeVal


class SingleSensorTimeValueSeq:
    def __init__(self, sensor:Sensor):
        self._sensor = sensor

        #initial state
        self._time_seq:list[float] = []
        self._vals_seq:list[np.ndarray] = []
        self._time_val_seq:list[TimeVal] = []

    def add_one_time_val(self, time, value, validity_check:bool=False):
        '''
        :param time:
        :param value:
        :param validity_check:
        :return:
        '''
        self._time_seq.append(time)
        self._val_seq.append(value)
        self._time_val_seq.append(TimeVal(time,val))

from sensor import Sensor


class SingleSensorTimeValueSeq:
    def __init__(self, sensor:Sensor):
        self._sensor = sensor

        #initial state
        self._time_seq = []
        self._vals_seq = []
        self._time_values_seq = []

    def add_one_time_val(self, time, value, validity_check:bool=False):
        '''
        :param time:
        :param value:
        :param validity_check:
        :return:
        '''
        self._time_seq.append(time)
        self._vals_seq.append(value)
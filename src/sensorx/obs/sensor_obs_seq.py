import numpy as np

from sensorx.sensor import Sensor
from sensorx.obs.obs import SensorTimeVec


class SensorObsSeq:
    def __init__(self, sensor_id:int):
        self._sensor_id = sensor_id

        #initial state
        self._obss = None

    def add_obs(self, obs:Obs):
        if self._obss is None:
            self._obss = []
        self._obss.append(obs)

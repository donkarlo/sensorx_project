import numpy as np

from sensorx.sensor import Sensor
from sensorx.obs.obs import SensorTimeVec


class Obss:
    def __init__(self, sensor_id:int, obss:list[Obs,...]=None):
        self._sensor_id = sensor_id

        #initial state
        self._obss_list = None

    def add_obs(self, obs:Obs):
        if self._obss_list is None:
            self._obss_list = []
        self._obss_list.append(obs)

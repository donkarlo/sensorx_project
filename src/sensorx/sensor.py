from type.type import Type

class Sensor:
    def __init__(self, type:Type, id:None , sensor_set_id:None):
        self._sensor_set_id = sensor_set_id

    def get_heirarchical_ids(self):
        pass
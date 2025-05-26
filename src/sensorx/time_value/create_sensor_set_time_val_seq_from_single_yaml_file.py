import yaml
from yaml import CLoader

class CreateSensorSetTimeValSeqFromSingleYamlFile:
    def __init__(self, path_to_yaml_file):
        self._path_to_yaml_file = path_to_yaml_file

    def save(self):
        pass

    def __generate_sensor_set_time_val_seq(self):
        with open(self._path_to_yaml_file, "r") as file:
            topic_rows = yaml.load_all(file, Loader=CLoader)
from sensorx.obs.sensor_set_obss_from_yaml_file import SensorSetObsSeqFromYamlFile

class BootForTwoRobotsAndTwoSensors:
    def __generate_sensor_set_time_val_seq(self):
        self._topics_yaml_file = SensorSetObsSeqFromYamlFile()
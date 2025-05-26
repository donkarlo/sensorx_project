from sensorx.time_value.create_sensor_set_time_val_seq_from_single_yaml_file import CreateSensorSetTimeValSeqFromSingleYamlFile

class BootForTwoRobotsAndTwoSensors:
    def __generate_sensor_set_time_val_seq(self):
        self._topics_yaml_file = CreateSensorSetTimeValSeqFromSingleYamlFile()
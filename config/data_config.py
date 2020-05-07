import os
import configparser

runPath = os.path.dirname(os.path.realpath(__file__))

class Config:
    def __init__(self, **kwargs):
        config = configparser.ConfigParser()
        print(runPath)
        print(os.path.join('config/configuration.ini'))
        config.read(os.path.join('config/configuration.ini'))
        raw_input = config['Input']
        self._cleaned_data_path = raw_input.get('Cleaned_data_path', 'data/sample.csv')

    def get_property(self, property_name):
        if property_name == 'cleaned_data_path':
            return self._cleaned_data_path

class DataConfig(Config):

    @property
    def cleaned_data_path(self):
        return self.get_property('cleaned_data_path')

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

username = config['default']['username']
email = config['default']['email']
prefered_time = config['default']['prefered_time']

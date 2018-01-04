import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'simmons_accountancy_winter_2018_cubesite'
    

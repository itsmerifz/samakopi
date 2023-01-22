import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
  DEBUG = False
  PORT = 5000
  CSRF_ENABLED = True
  SECRET_KEY = os.environ.get('SECRET_KEY') #pake md5
  
class ProductionConfig(Config):
  DEBUG = False
  ENV = 'production'
  
class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True
  ENV = 'development'
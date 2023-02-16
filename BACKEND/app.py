from flask import Flask
from os import path
from routes.routers import router
import database.db_model as database

basedir = path.abspath(path.dirname(__file__))

def init_app():  
  app = Flask(__name__)
  app.config['CORS_HEADERS'] = 'Content-Type'
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+ path.join(basedir,"database.db")
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
  app.register_blueprint(router)
  
  # Development
  app.config.from_object('config.DevelopmentConfig')
  
  # Production
  app.config.from_object('config.ProductionConfig')
  
  # Connect to database
  database.db.init_app(app)
  with app.app_context():
    database.db.create_all()
    
  return app

if __name__ == '__main__':    
  init_app().run()
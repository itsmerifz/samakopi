from flask import Flask
from routes.routes import router

def init_app():  
  app = Flask(__name__)
  app.config['CORS_HEADERS'] = 'Content-Type'
  
  app.register_blueprint(router)
  
  # Development
  app.config.from_object('config.DevelopmentConfig')
  
  # Production
  app.config.from_object('config.ProductionConfig')
  
  return app

if __name__ == '__main__':    
  init_app().run()
from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
from os import path

db = SQLAlchemy()

class Predict(db.Model):
  uuid = db.Column(db.String(255), primary_key=True)
  text = db.Column(db.Text())
  label = db.Column(db.String(100))
  percentage = db.Column(db.String(10))
  create_at = db.Column(db.DateTime())
  
  def __init__(self, uuid, text, label, percentage, create_at):
    self.uuid = uuid
    self.text = text
    self.label = label
    self.percentage = percentage
    self.create_at = create_at
    


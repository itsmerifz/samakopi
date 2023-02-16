from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Categories(db.Model):
  id = db.Column(db.String(200), primary_key=True)
  uuid = db.Column(db.String(255))
  text = db.Column(db.Text())
  label = db.Column(db.String(100))
  percentage = db.Column(db.String(10))
  create_at = db.Column(db.DateTime())
  
  def __init__(self, id, uuid, text, label, percentage, create_at):
    self.id = id
    self.uuid = uuid
    self.text = text
    self.label = label
    self.percentage = percentage
    self.create_at = create_at
    

class Mediasi(db.Model):
  id = db.Column(db.String(200), primary_key=True)
  uuid = db.Column(db.String(255), )
  text = db.Column(db.Text())
  label = db.Column(db.String(100))
  percentage = db.Column(db.String(10))
  create_at = db.Column(db.DateTime())

  def __init__(self, id, uuid, text, label, percentage, create_at):
    self.id = id
    self.uuid = uuid
    self.text = text
    self.label = label
    self.percentage = percentage
    self.create_at = create_at
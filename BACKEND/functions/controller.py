from flask import jsonify
import uuid
import database.db_model as model
import datetime
from sqlalchemy.exc import SQLAlchemyError

db = model.db

def create_predict_result_data(_data: dict[str], text_predict: str) -> str:
  try:
    data = model.Categories(str(uuid.uuid4()), text_predict, _data['hasil'], _data['percentage'], datetime.datetime.now())
    db.session.add(data)
    db.session.commit()
  except SQLAlchemyError as e:
    error = str(e.__dict__['orig'])
    return str(error)
  
def create_mediasi_data(_data: dict[str], text_predict: str) -> str:
  try:
    data = model.Mediasi(str(uuid.uuid4()), text_predict, _data['hasil'], _data['percentage'], datetime.datetime.now())
    db.session.add(data)
    db.session.commit()
  except SQLAlchemyError as e:
    error = str(e.__dict__['orig'])
    return str(error)
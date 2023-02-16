from flask import jsonify
import uuid
import database.db_model as model
import datetime

db = model.db

def create_predict_result_data(_data: dict[str], text_predict: str) -> str:
  try:
    data = model.Categories(str(_data['id']) ,str(uuid.uuid4()), text_predict, _data['hasil'], _data['percentage'], datetime.datetime.now())
    db.session.add(data)
    if db.session.commit():
      return 'success'
    else:
      raise Exception('Failed to add data')
  except Exception as e:
    return str(e)
  
def create_mediasi_data(_data: dict[str], text_predict: str) -> str:
  try:
    data = model.Mediasi(str(_data['id']) ,str(uuid.uuid4()), text_predict, _data['hasil'], _data['percentage'], datetime.datetime.now())
    db.session.add(data)
    if db.session.commit():
      return 'success'
    else:
      raise Exception('Failed to add data')
  except Exception as e:
    return str(e)
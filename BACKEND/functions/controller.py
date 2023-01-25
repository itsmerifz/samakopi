from flask import jsonify
from database.database import get_database

db = get_database()

def create_predict_result_data(_data: dict[str], text_predict: str):
  try:
    result = db.collection('predict_result').document(str(_data['id'])).set({
      'hasil': _data['hasil'],
      'percentage': _data['percentage'],
      'setuju': False,
      'data': text_predict,
    })
    if result:
      return 'success'
    else:
      raise Exception('Failed to add data')
  except Exception as e:
    return str(e)
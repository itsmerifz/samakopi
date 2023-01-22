from flask import jsonify
from database.database import init_database

db = init_database()

def create_predict_result_data(data: dict[str]):
  """
        create_predict_result_data() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post'}
  """
  try:
    breakpoint()
    _data = data
    result = db.document(str(_data['id'])).set({
      'status': _data['status'],
      'hasil': _data['hasil'],
      'percentage': _data['percentage'],
      'setuju': False,
    })
    if result:
      return 'success'
    else:
      raise Exception('Failed to add data')
  except Exception as e:
    return jsonify({
      "error": e
      }), 500
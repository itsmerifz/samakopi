from flask import Blueprint, jsonify, request, json
from werkzeug.exceptions import HTTPException
import numpy as np
from functions.tokenizer import tokenize
from model.model import load_rnn_model
from functions.web_scrapper import get_web_texts
from functions.controller import create_predict_result_data
from functions.stopword import remove_stopword
import preprocessor as p
import calendar
import time

router = Blueprint('routes', __name__, url_prefix='/api')

@router.route('/rnnwebpredict', methods=['POST'])
def rnn_webpredict():
  classes = ['Konflik Caleg', 'Konflik Dualisme Kepengurusan', 'Konflik Dukungan Capres', 'Konflik Elite Politik']
  try:
    model = load_rnn_model()
    
    recieved_data = request.get_json()
    if not recieved_data:
      return jsonify({
        'error': 'No data provided'
        }), 404
    
    link = str(recieved_data['link'])
    texts = get_web_texts(link)
    texts = p.clean(texts)
    texts = remove_stopword(texts)
    padded_data = tokenize(texts)
    pred = model.predict(padded_data)
    date = calendar.timegm(time.gmtime())
    if pred is not None:
      data = {
        'id': date,
        'status': 'success',
        'hasil': classes[np.argmax(pred)],
        'percentage': '{:.2f}%'.format(pred[0][np.argmax(pred)] * 100)
      }
      create_predict_result_data(data, texts)
      return jsonify(data), 200
    
  except Exception as e:
    return jsonify({
      'error': str(e)
    }), 500
    
@router.errorhandler(HTTPException)
def handler_error(e):
  response = e.get_response()
  response.data = json.dumps({
    "code": e.code,
    "name": e.name,
    "description": e.description,
  })
  response.content_type = "application/json"
  return response

from flask import Blueprint, jsonify, request, json
from werkzeug.exceptions import HTTPException
import numpy as np
from functions.tokenizer import tokenize
from model.model import load_rcnn_model, load_rcnn_mediation_model, label_categories, label_mediation
from functions.web_scrapper import get_web_texts
from functions.controller import create_predict_result_data, create_mediasi_data
from functions.stopword import remove_stopword
import preprocessor as p
import calendar
import time

router = Blueprint('routes', __name__, url_prefix='/api')
date = calendar.timegm(time.gmtime())

@router.route('/rcnnwebpredict', methods=['POST'])
def rcnn_webpredict():
  try:
    model = load_rcnn_model()
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
    if pred is not None:
      data = {
        'id': str(date),
        'status': 'success',
        'hasil': label_categories[np.argmax(pred)],
        'percentage': '{:.2f}%'.format(pred[0][np.argmax(pred)] * 100)
      }
      create_predict_result_data(data, texts)
      return jsonify(data), 200
    
  except Exception as e:
    return jsonify({
      'error': str(e)
    }), 500
    
@router.route('/rcnnpredict', methods=['POST'])
def rcnn_predict():
  try:
    model = load_rcnn_model()
    recieved_data = request.get_json()
    if not recieved_data:
      return jsonify({
        'error': 'No data provided'
        }), 404
    text = str(recieved_data['text'])
    text = p.clean(text)
    text = remove_stopword(text)
    padded_data = tokenize(text)
    pred = model.predict(padded_data)
    if pred is not None:
      data = {
        'id': str(date),
        'status': 'success',
        'hasil': label_categories[np.argmax(pred)],
        'percentage': '{:.2f}%'.format(pred[0][np.argmax(pred)] * 100)
      }
      create_predict_result_data(data, text)
      return jsonify(data), 200
  except Exception as e:
    return jsonify({
      'error': str(e)
    }), 500
    
@router.route('/rcnnwebmediasi', methods=['POST'])
def rcnn_mediasi_webpredict():
  try:
    model = load_rcnn_mediation_model()
    recieved_data = request.get_json()
    if not recieved_data:
      return jsonify({
        'error': 'No data provided'
        }), 404
    text = str(recieved_data['text'])
    text = p.clean(text)
    text = remove_stopword(text)
    padded_data = tokenize(text)
    pred = model.predict(padded_data)
    if pred is not None:
      data = {
        'id': str(date),
        'status': 'success',
        'hasil': label_mediation[np.argmax(pred)],
        'percentage': '{:.2f}%'.format(pred[0][np.argmax(pred)] * 100)
      }
      create_mediasi_data(data, text)
      return jsonify(data), 200
  except Exception as e:
    return jsonify({
      'error': str(e)
    }), 500

@router.route('/rcnnmediasi', methods=['POST'])
def rcnn_mediasi():
  try:
    model = load_rcnn_model()
    recieved_data = request.get_json()
    if not recieved_data:
      return jsonify({
        'error': 'No data provided'
        }), 404
    text = str(recieved_data['text'])
    text = p.clean(text)
    text = remove_stopword(text)
    padded_data = tokenize(text)
    pred = model.predict(padded_data)
    if pred is not None:
      data = {
        'id': str(date),
        'status': 'success',
        'hasil': label_categories[np.argmax(pred)],
        'percentage': '{:.2f}%'.format(pred[0][np.argmax(pred)] * 100)
      }
      create_predict_result_data(data, text)
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

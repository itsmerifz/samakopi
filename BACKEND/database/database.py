from firebase_admin import credentials, firestore, initialize_app
from flask import jsonify

default_app = None

def init_database():
  try:
    cred = credentials.Certificate('D:\KULIAH\SKP n SKRIPSWITT\RIL PROJECT SKRIPSWITT\BACKEND\database\samakopi-firebase.json')
    global default_app
    if default_app is None:
      default_app = initialize_app(cred)
    return 'initialize success'
  except Exception as e:
    return jsonify({
      "error": e
      }), 500

def get_database():
  try:
    if default_app is None:
      init_database()
    db = firestore.client()
    return db
  except Exception as e:
    return jsonify({
      "error": e
      }), 500
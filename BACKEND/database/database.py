from firebase_admin import credentials, firestore, initialize_app
from flask import jsonify

def init_database():
  try:
    cred = credentials.Certificate('D:\KULIAH\SKP n SKRIPSWITT\RIL PROJECT SKRIPSWITT\BACKEND\database\samakopi-firebase.json')
    default_app = initialize_app(cred)
    if default_app is None:
      raise Exception('Error while initializing database')
    db = firestore.client()
    return db
  except Exception as e:
    return jsonify({
      "error": e
      }), 500

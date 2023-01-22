import tensorflow
from tensorflow.keras.models import load_model

def load_rnn_model():
  try: 
    model = load_model('D:\KULIAH\SKP n SKRIPSWITT\RIL PROJECT SKRIPSWITT\BACKEND\model\h5\model2.h5')
    if model == None:
      raise Exception('Model not found')
    return model
  except Exception as e:
    print(str(e))
    
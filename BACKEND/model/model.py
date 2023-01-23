import tensorflow as tf

classes = ['Konflik Caleg', 'Konflik Dualisme Kepengurusan', 'Konflik Dukungan Capres', 'Konflik Elite Politik']

def load_rnn_model():
  try: 
    model = tf.keras.models.load_model('D:\KULIAH\SKP n SKRIPSWITT\RIL PROJECT SKRIPSWITT\BACKEND\model\h5\model2.h5')
    if model == None:
      raise Exception('Model not found')
    return model
  except Exception as e:
    print(str(e))
    
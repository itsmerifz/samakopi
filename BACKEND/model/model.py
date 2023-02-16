import tensorflow as tf

label_categories = ['Konflik Caleg', 'Konflik Dukungan Capres', 'Konflik Elite Politik', 'Konflik Kepengurusan Partai']
label_mediation = ["Keputusan Pimpinan", "Jalur Hukum", "Musyawarah",  "Tidak Ada"]

def load_rcnn_model():
  try: 
    model = tf.keras.models.load_model('D:\KULIAH\SKP n SKRIPSWITT\RIL PROJECT SKRIPSWITT\BACKEND\model\h5\modelfix.h5', compile=False)
    if model == None:
      raise Exception('Model not found')
    return model
  except Exception as e:
    return str(e)
    
def load_rcnn_mediation_model():
  try: 
    model = tf.keras.models.load_model('D:\KULIAH\SKP n SKRIPSWITT\RIL PROJECT SKRIPSWITT\BACKEND\model\h5\modelfix-mediasi.h5', compile=False)
    if model == None:
      raise Exception('Model not found')
    return model
  except Exception as e:
    return str(e)
    
import tensorflow as tf
import pickle

def tokenize(text: str):
  try:
    MAX_SEQUENCE_LENGTH = 250
    with open('D:\KULIAH\SKP n SKRIPSWITT\RIL PROJECT SKRIPSWITT\BACKEND\model\datatoken.pickle', 'rb') as handle:
      tokenizer = pickle.load(handle)
    sample = [text]
    sequence = tokenizer.texts_to_sequences(sample)
    padded = tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)
    if padded is None:
      raise Exception('Error while tokenizing')
    return padded
  except Exception as e:
    print(str(e))

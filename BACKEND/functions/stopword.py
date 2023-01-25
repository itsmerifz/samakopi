import pickle

def remove_stopword(text: str):
  try:
    with open('D:\KULIAH\SKP n SKRIPSWITT\RIL PROJECT SKRIPSWITT\BACKEND\model\stopword.pickle', 'rb') as handle:
      stopword = pickle.load(handle)
    filtered_word = [word for word in text.split() if word not in stopword]
    return " ".join(filtered_word)
  except Exception as e:
    return str(e)
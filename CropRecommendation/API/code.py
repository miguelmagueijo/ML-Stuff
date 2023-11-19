import pickle
import pandas as pd
import time

def messageWithSecondsFrom(start: float, msg: str) -> str:
    return f"{msg}: {round(time.time() - start, 4)}s"


rf_model_file = open("../rf_model.pkl", "rb")

start = time.time()
rfc_model = pickle.load(rf_model_file)
print(messageWithSecondsFrom(start, "To load model, I took"))

predict_me = pd.DataFrame({'N': [100], 'P': [25], 'K': [26], 'temperature': [25.5], 'humidity': [53.2], 'ph': [8.4], 'rainfall': [150.23]})

start = time.time()
print("My prediction is...", rfc_model.predict(predict_me))
print(messageWithSecondsFrom(start, "To predict, I took"))
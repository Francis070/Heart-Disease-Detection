import joblib as jl
import numpy as np

model = jl.load('heart_disease_detector_model.pkl')

def predict_disease(input_list):
    input_features = np.array(input_list)
    final_list = input_features.reshape(1, -1)

    result = model.predict(final_list)
    print(result)

    return result
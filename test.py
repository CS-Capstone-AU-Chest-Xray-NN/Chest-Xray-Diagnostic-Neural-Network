import cv2
import numpy as np
import pandas as pd
from keras.models import model_from_json
from sklearn.preprocessing import LabelEncoder

from generator import ImageGenerator

def load_model(path):
    with open(path, 'r') as f:
        model = model_from_json(f.read())
        model.load_weights(path.replace('json', 'h5'))
        return model

if __name__ == '__main__':
    labels = pd.read_csv('data/labels.csv')
    X = labels.Image_Index
    y = LabelEncoder().fit_transform(labels.Finding_Labels).reshape(-1, 1)

    model = load_model('data/model.json')
    prediction = model.predict_generator(ImageGenerator(X, y, 100), verbose=1)
    y = np.argmax(y, axis=1)
    prediction = np.argmax(prediction, axis=1)

    print('Precision:', model.precision_score(y, prediction))
    print('Recall:', model.recall_score(y, prediction))
    print('F1:', model.f1_score(y, prediction))

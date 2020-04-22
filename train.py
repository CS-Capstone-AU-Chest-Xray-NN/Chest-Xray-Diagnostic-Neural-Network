import numpy as np
import pandas as pd

from model import Model

if __name__ == '__main__':
    labels = pd.read_csv('data/labels.csv')
    X = labels.Image_Index
    y = LabelEncoder().fit_transform(labels.Finding_Labels).reshape(-1, 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    X_train = X_train.reshape(X_train.shape[0], 1024, 1024, 1)
    X_test = X_test.reshape(X_test.shape[0], 1024, 1024, 1)
    X_train = X_train.astype('float32') /= 255
    X_test = X_test.astype('float32') /= 255
    y_train = np_utils.to_categorical(y_train, 15)
    y_test = np_utils.to_categorical(y_test, 15)

    model = Model(X_train, y_train, 25, 100, 15)

    y_pred = model.predict(X_test)
    y_test = np.argmax(y_test, axis=1)
    y_pred = np.argmax(y_pred, axis=1)

    print('Precision:', model.precision_score(y_test, y_pred))
    print('Recall:', model.recall_score(y_test, y_pred))
    print('F1:', model.f1_score(y_test, y_pred))

    model.save('data/model.json')

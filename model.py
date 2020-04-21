import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score


class Model():
    def __init__(self, X_train, y_train, kernel_size, filters, channels, epoch, batch_size, classes, gpus):
        self.X_train = X_train
        self.y_train = y_train
        self.kernel_size = kernel_size
        self.filters = filters
        self.channels = channels
        self.epoch = epoch
        self.batch_size = batch_size
        self.classes = classes
        self.gpus = gpus

        self.fit()

    def fit(self):
        pass

    def predict(self, X_test):
        return self.model.predict(X_test)

    def argmax(self, array):
        return np.argmax(array, axis=1)

    def precision_score(self, y_test, y_pred):
        return precision_score(y_test, y_pred, average='weighted')

    def recall_score(self, y_test, y_pred):
        return recall_score(y_test, y_pred, average='weighted')

    def f1_score(self, y_test, y_pred):
        return f1_score(y_test, y_pred, average='weighted')

if __name__ == '__main__':
    pass

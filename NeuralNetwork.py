import tensorflow as tf
from tensorflow import keras

def load_dataset(name):
    filenames, labels = load_data(name)
    dataset = tf.data.Dataset.from_tensor_slices((tf.constant(filenames), tf.constant(labels)))
    dataset = dataset.map(parse_image)
    return dataset

def load_data(name):
    mapping = {}
    with open('data/{}.txt'.format(name), 'r') as f:
        for line in f.readlines():
            mapping[line.strip()] = None

    with open('data/data.csv', 'r') as f:
        for line in (l.strip() for l in f.readlines()):
            data = line.split(',')
            filename, label = data[0], data[1]
            if filename in mapping:
                mapping[filename] = label

    filenames = []
    labels = []
    for filename, label in mapping.items():
        filenames.append('data/{}/{}'.format(name, filename))
        # dumb hack to make sure shape matches
        # there is 100% a better way to do this
        labels.append([label] * 1024)

    return filenames, labels

def parse_image(filename, label):
    image = tf.io.read_file(filename)
    image = tf.io.decode_png(image)
    image = tf.image.resize(image, (1024, 1024))
    return image, label

if __name__ == '__main__':
    train_dataset = load_dataset('training')
    test_dataset = load_dataset('testing')

    model = keras.Sequential([
        keras.layers.Flatten(),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(64),
        keras.layers.BatchNormalization(),
        keras.layers.Activation('relu'),
        keras.layers.Dense(1),
        keras.layers.BatchNormalization(),
        keras.layers.Activation('sigmoid')
    ])

    model.compile(
        loss='binary_crossentropy',
        optimizer=tf.keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0),
        metrics=['accuracy']
    )

    model.fit(train_dataset)
    # _, accuracy = model.evaluate(test_dataset, verbose=0)
    # print(accuracy)

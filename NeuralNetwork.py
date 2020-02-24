import tensorflow as tf

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
        labels.append(label)
    
    return filenames, labels

def parse_image(filename, label):
    image = tf.io.read_file(filename)
    image = tf.io.decode_png(image)
    image = tf.image.resize(image, (1024, 1024))
    return image, label

if __name__ == '__main__':
    train_dataset = load_dataset('training')

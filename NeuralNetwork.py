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
        filenames.append(filename)
        labels.append(label)
    
    return filenames, labels

if __name__ == '__main__':
    train_filenames, train_labels = load_data('training')
    print(train_filenames, train_labels)

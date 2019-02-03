from keras.datasets import imdb

(train_images,train_labels),(test_images,test_labels) = imdb.load_data(num_words=10000)

a =train_images[1]

word_index = imdb.get_word_index()


reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])

decoded_review = ' '.join([reverse_word_index.get(i-3,'?') for i in train_images[0]])
print(reverse_word_index.get(10))

#=========ENCODING THE INTEGER MATRIX INTO BINARY MATRIX=========================
import numpy as np
def vectorise_sequence(sequence,dimension=10000):
    result = np.zeros((len(sequence),dimension))
    for i, sequen in enumerate(sequence):
        result[i,sequen] = 1
    return result

train_images = vectorise_sequence(train_images)
test_images = vectorise_sequence(test_images)

y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')

#============================ DEFINING MODEL===========================
from keras import layers,models

model = models.Sequential()
model.add(layers.Dense(16,activation='relu',input_shape=(10000,)))
model.add(layers.Dense(16,activation='relu'))
model.add(layers.Dense(1,activation='sigmoid'))

#-=====================----COMPLILING THE MODEL=================

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

#======================MAKIN
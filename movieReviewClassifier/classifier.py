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

x_train = vectorise_sequence(train_images)
y_test = vectorise_sequence(test_images)

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

#======================MAKINGG VALIDATION SET

x_val = x_train[:10000]
partial_x_train = x_train[10000:]

y_val = y_train[:10000]
partial_y_train = y_train[10000:]

#======================= FITTING THE MODEL====================
history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=[x_val,y_val])










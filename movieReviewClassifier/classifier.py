from keras.datasets import imdb

(train_images,train_labels),(test_images,test_labels) = imdb.load_data(num_words=10000)

a =train_images[1]

word_index = imdb.get_word_index()


reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])

decoded_review = ' '.join([reverse_word_index.get(i-3,'?') for i in train_images[0]])
print(reverse_word_index.get(10))
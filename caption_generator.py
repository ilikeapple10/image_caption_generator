import numpy as np
from PIL import Image
from pickle import dump, load
from keras.models import load_model
from keras.applications.xception import Xception, preprocess_input
from keras.preprocessing.sequence import pad_sequences
import os
import random


allImages = list()
def chooseRandomImage(directory='Flicker8k_Dataset'):
    for img in os.listdir(directory): #Lists all files
        allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosenImage = 'Flicker8k_Dataset\\' + allImages[choice] #Do Whatever you want with the image file
    return chosenImage
#'image_caption_generator\\Flicker8k_Dataset\\12830823_87d2654e31.jpg'
random_image = chooseRandomImage()
img_path = random_image
def extract_features(filename, model):

        image = Image.open(filename)

        image = image.resize((299,299))
        image = np.array(image)
        # for images that has 4 channels, we convert them into 3 channels
        if image.shape[2] == 4: 
            image = image[..., :3]
        image = np.expand_dims(image, axis=0)
        image = image/127.5
        image = image - 1.0
        feature = model.predict(image)
        return feature

def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def generate_desc(model, tokenizer, photo, max_length):
    in_text = '|start|'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        pred = model.predict([photo,sequence], verbose=0)
        pred = np.argmax(pred)
        word = word_for_id(pred, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'end':
            break
    return in_text

max_length = 32
tokenizer = load(open("tokenizer.p","rb"))
model = load_model("models\\model_9.h5")
xception_model = Xception(include_top=False, pooling="avg")
photo = extract_features(img_path, xception_model)
description = generate_desc(model, tokenizer, photo, max_length)
image = Image.open(img_path)
image.show()
print("\n\n")
print(description)
print(img_path)
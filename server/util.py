import numpy as np
from keras.models import load_model
import cv2

model_path = '../model/dogs_and_cats.h5'
model = load_model(model_path)
def predictions(img_path, model):
    img = cv2.imread(img_path)
    img_resized = cv2.resize(img, (128,128))
    x = np.array(img_resized)
    x = np.expand_dims(x, axis=0)
    pred = model.predict(x)[0]
    preds = ''
    if pred >= 0.5:
        print(pred)
        preds = "DOG"
    else:
        print(pred)
        preds = "CAT"
    return preds

if __name__ == '__main__':
    print(predictions('../model/test1/5.jpg', model))
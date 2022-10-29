from flask import Flask, redirect, url_for, request, render_template
import os
from werkzeug.utils import secure_filename
from keras.models import load_model
import util

app = Flask(__name__)
model_path = '../model/dogs_and_cats.h5'
model = load_model(model_path)


if __name__ == '__main__':
    app.run(debug=True)

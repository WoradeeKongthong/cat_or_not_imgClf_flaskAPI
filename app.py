from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from flask import Flask, request

import os
import sys
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# Define model path
MODEL_PATH = 'model/final_model.h5'

# Load the model
model = load_model(MODEL_PATH)
#model._make_predict_function()

# model prediction function
def model_predict(img_path, model):
    # load image
    img = image.load_img(img_path, target_size=(64,64))
    
    # preprocessing
    # convert img to array
    img = img_to_array(img)
    # reshape
    sample = img.reshape(1,64,64,3)
    
    # create generator without data augmentation
    datagen = ImageDataGenerator(featurewise_center=True)
    datagen.mean = [123.68, 116.779, 103.939]
    # prepare iterator
    sample_it = datagen.flow(sample, batch_size=1)

    # make prediction
    result = model.predict(sample_it)   
    return result


@app.route('/', methods=['GET'])
def index():
    return "Welcome All"

@app.route('/predict', methods=['POST'])
def predict_form_file():
    # get the file from post request
    f = request.files['file']
    
    # save the file to ./uploads
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(basepath, secure_filename(f.filename))
    f.save(file_path)
    
    # make prediction
    preds = model_predict(file_path, model)
    if preds[0][0] == 0:
        result = 'This input picture is not a cat'
    else:
        result = 'This input picture is a cat'
    return result
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)

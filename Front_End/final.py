import keras
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from numpy import expand_dims, argmax
from PIL import Image

model = load_model("resnet90.h5")
classes=['Unhealthy', 'Healthy']

img_path = "static/uploaded_image.png"

def check_paddy_health(img_path):
    image = load_img(img_path, grayscale=False, color_mode='rgb', target_size=(80,80))
    image = img_to_array(image)
    image /= 255
    image = expand_dims(image, axis = 0)
    prediction = model.predict([image])
    # print(classes[argmax(prediction[0])])
    return classes[argmax(prediction[0])]

print(check_paddy_health(img_path))



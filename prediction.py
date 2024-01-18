import keras
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from numpy import expand_dims, argmax

model = load_model("resnet60.h5")
classes=['Hispa', 'Healthy', 'BrownSpot', 'LeafBlast']

def check_paddy_health(img_path):
    image = load_img(img_path, grayscale=False, color_mode='rgb', target_size=(80,80))
    image = img_to_array(image)
    image /= 255
    image = expand_dims(image, axis = 0)
    prediction = model.predict([image])
    return classes[argmax(prediction[0])]

print(check_paddy_health('/media/harshvardhanpandey/1E48765F4876359D/IIIT Hyderabad/Megathon2023/IMG_20190419_123623.jpg'))
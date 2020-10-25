import numpy as np
import cv2
from PIL import Image

def get_vector(request, size):
    img = Image.open(request.FILES['file'])
    img.thumbnail(size)
    # img = cv2.imread(img)
    # resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    vector = np.array(img).reshape(-1)
    vector = vector.tolist()
    for i in range(len(vector)):
        vector[i] = vector[i] / 255
    return str(vector)




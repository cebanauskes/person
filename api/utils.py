import numpy as np
from PIL import Image

def get_vector(request, size):
    img = Image.open(request.FILES['file'])
    img.thumbnail(size)
    vector = np.array(img).reshape(-1)
    vector = vector.tolist()
    for i in range(len(vector)):
        vector[i] = vector[i] / 255
    return str(vector)




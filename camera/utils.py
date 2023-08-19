import cv2
import numpy as np
import base64

def get_decoded_image(encoded_image: str):
    extracted_data = encoded_image[encoded_image.find('/9'):]
    img_bytes = base64.b64decode(extracted_data)
    img_raw = np.frombuffer(img_bytes,np.int8)
    img = cv2.imdecode(img_raw,cv2.IMREAD_COLOR)
    return img

def get_encoded_image(img):
    _,encoded_img = cv2.imencode(".jpeg",img)
    encoded_img = np.array(encoded_img)
    return "data:image/jpeg;base64," + base64.b64encode(encoded_img.tobytes()).decode("utf-8")
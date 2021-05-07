# ready to run example: PythonClient/multirotor/hello_drone.py
import airsim
import os
import cv2
import numpy as np

def parse_camera(in_image):
    img1d = np.fromstring(in_image.image_data_uint8, dtype=np.uint8) # get numpy array
    image = img1d.reshape(in_image.height, in_image.width, 3) # reshape array to 3 channel image array H X W X 3
    # print(img1d.shape, image.shape, end='\r')
    cv2.imshow('image', image)
    cv2.waitKey()

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# take images
responses = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])
print('Retrieved images: %d', len(responses))

parse_camera(responses[0])



import cv2
import os
from tqdm import tqdm


image_folder = 'Data/Frames_CHK'
video_name = f'Output/Result.mp4'
fps = 30.0

Frames = []

for files_ in os.listdir(image_folder):
    if os.path.isfile(os.path.join(image_folder,files_)):
        Frames.append(files_)

image = f"{image_folder}/{Frames[0]}"
height, width, channel = cv2.imread(image).shape

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(video_name, fourcc, fps,(width, height))

for frame in tqdm(Frames, colour='#35d70d'):
    data = cv2.imread((f"{image_folder}/{frame}"))
    video.write(data)

cv2.destroyAllWindows()
video.release()
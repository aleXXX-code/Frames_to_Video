import cv2
import os
from tqdm import tqdm


def render_Video(image_folder, videoName, fps: float, formatVid="mp4"):
    folder = f"Input/{image_folder}"
    video_name = f'Output/{videoName}.{formatVid}'
    
    Frames = []

    for files_ in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, files_)):
            Frames.append(files_)
    sorted(Frames)

    image = f'{folder}/{Frames[0]}'
    height, width, channel = cv2.imread(image).shape

    fourcc = None

    if formatVid == "avi":
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
    elif formatVid == "mp4":
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    else:
        print("Format UnSupported")
        cv2.destroyAllWindows()

    video = cv2.VideoWriter(video_name, fourcc, fps, (width,height))

    for frame in tqdm(Frames, colour='#35d70d'):
        data = cv2.imread((f"{folder}/{frame}"))
        video.write(data)


    
if __name__ == "__main__":
    Frame_folder = input("Folder Name: ")
    Video_name = input("Name of Video: ")
    fps = float(input("Enter fps: "))
    format_vid = input("Format avi/mp4: ")

    render_Video(Frame_folder, Video_name, fps, format_vid)

    cv2.destroyAllWindows()
    cv2.VideoWriter().release()

    

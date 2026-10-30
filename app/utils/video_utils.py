import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frames.append(frame)
        
    return frames

def save_video(output_frames, output_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 24, (output_frames[0].shape[1], output_frames[0].shape[0]))
    
    for frame in output_frames:
        out.write(frame)
    
    out.release()
    
    
def crop_player_img(tracks, video_path):
    
    video_frames = read_video(video_path)
    
    for track_id, player in tracks['players'][0].items():
        bbox = player['bbox']
        frame = video_frames[0]
        
        # crop bbox from frame
        cropped_img = frame[int(bbox[1]): int(bbox[3]), int(bbox[0]): int(bbox[2])]
        
        # save the cropped image
        cv2.imwrite(f'output_videos/cropped_img.jpg', cropped_img)
    
        break
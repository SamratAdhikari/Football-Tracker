import cv2
import numpy as np
from utils import read_video, save_video, crop_player_img, interpolate_ball_positions
from tracker import Tracker
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner


VIDEO_PATH = 'input_videos/video.mp4'
isCroppedImgReq = False


def main():
    # read video
    video_frames = read_video(VIDEO_PATH)
    
    # initialize tracker
    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path="stubs/track_stubs.pkl")
    
    # interpolate ball positions
    tracks['ball'] = interpolate_ball_positions(tracks['ball'])
    
    # save croppped image of a player
    if isCroppedImgReq:
        crop_player_img(tracks, VIDEO_PATH)
        return # stop the code execution
    
    # assign player teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], tracks['players'][0])
    
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num], track['bbox'], player_id)
            
            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]
            
    # assign ball aquisition
    player_assigner = PlayerBallAssigner()
    team_possesssion = []
    
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)
        
        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            team_possesssion.append(tracks['players'][frame_num][assigned_player]['team'])
        
        else:
            team_possesssion.append(team_possesssion[-1])
    team_possesssion = np.array(team_possesssion)

    # draw output
    output_video_frames = tracker.draw_annotations(video_frames, tracks, team_possesssion)
    
    # save video
    save_video(output_video_frames, 'output_videos/video.avi')


if __name__ == "__main__":
    main()

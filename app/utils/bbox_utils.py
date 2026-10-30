import pandas as pd

def get_center_bbox(bbox):
    x1, y1, x2, y2 = bbox
    
    return int((x1+x2)/2), int((y1+y2)/2)

def get_bbox_width(bbox):
    return bbox[2] - bbox[0] # x2 - x1


def measure_distance(p1, p2):
    return (((p1[0]) - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def interpolate_ball_positions(ball_positions):
    ball_positions = [x.get(1, {}).get('bbox', []) for x in ball_positions]
    df_ball_positions = pd.DataFrame(ball_positions, columns = ['x1', 'y1', 'x2', 'y2'])
    
    # interpolate misisng values
    df_ball_positions = df_ball_positions.interpolate()
    df_ball_positions = df_ball_positions.bfill()
    
    ball_positions = [{1: {'bbox': x}} for x in df_ball_positions.to_numpy().tolist()]
    
    return ball_positions


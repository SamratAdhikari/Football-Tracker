def get_possession_rect_dims(overlay_shape):
    height, width = overlay_shape

    x1 = int(width * 0.80)
    y1 = int(height * 0.87)

    x2 = int(width * 0.98)
    y2 = int(height * 0.96)
    
    return x1, y1, x2, y2


def get_possession_text_pos(overlay_shape):
    height, width = overlay_shape[:2]

    x = int(width * 0.82)
    y = int(height * 0.90)

    return x, y
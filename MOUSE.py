def mouse_motion(x, y):
    global yaw, pitch, last_x, last_y, first_mouse, camera_front

    if first_mouse:
        last_x, last_y = x, y
        first_mouse = False

    xoffset = x - last_x
    yoffset = last_y - y  # reversed: y ranges bottom to top
    last_x, last_y = x, y

    xoffset *= sensitivity
    yoffset *= sensitivity

    yaw += xoffset
    pitch += yoffset

    # constrain the pitch
    if pitch > 89.0:
        pitch = 89.0
    if pitch < -89.0:
        pitch = -89.0

    front = [0.0, 0.0, 0.0]
    front[0] = np.cos(np.radians(yaw)) * np.cos(np.radians(pitch))
    front[1] = np.sin(np.radians(pitch))
    front[2] = np.sin(np.radians(yaw)) * np.cos(np.radians(pitch))
    camera_front = np.array(front) / np.linalg.norm(front)
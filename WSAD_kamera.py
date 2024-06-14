def keyboard(key, x, y):
    global camera_pos
    camera_speed = move_speed
    print(key)
    if key == b'\x1b':  # ESC key
        sys.exit()
    if key == b'w':
        camera_pos[0] += camera_speed * camera_front[0]
        camera_pos[1] += camera_speed * camera_front[1]
        camera_pos[2] += camera_speed * camera_front[2]
    if key == b's':
        camera_pos[0] -= camera_speed * camera_front[0]
        camera_pos[1] -= camera_speed * camera_front[1]
        camera_pos[2] -= camera_speed * camera_front[2]
    if key == b'a':
        camera_pos[0] -= np.cross(camera_front, camera_up)[0] * camera_speed
        camera_pos[1] -= np.cross(camera_front, camera_up)[1] * camera_speed
        camera_pos[2] -= np.cross(camera_front, camera_up)[2] * camera_speed
    if key == b'd':
        camera_pos[0] += np.cross(camera_front, camera_up)[0] * camera_speed
        camera_pos[1] += np.cross(camera_front, camera_up)[1] * camera_speed
        camera_pos[2] += np.cross(camera_front, camera_up)[2] * camera_speed
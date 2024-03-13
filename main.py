import cv2
import mediapipe as mp


cam = cv2.VideoCapture(1) # start the webcam
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True) # load the face mesh model

while True:
    _, frame = cam.read() # read the frame from the webcam
    frame = cv2.flip(frame, 1) # flip the frame horizontally
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert frame to RGB
    output = face_mesh.process(rgb_frame) # process the frame
    landmarks_points = output.multi_face_landmarks # get the landmarks eg points on the face
    #print(landmarks_points)
    frame_height, frame_width, _ = frame.shape
    if landmarks_points:
        landmarks = landmarks_points[0].landmark
        for landmark in landmarks[474:478]:
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 1, (0, 255, 0))
            print(x, y)
    cv2.imshow('Eye control mouse', frame)
    cv2.waitKey(1)
import cv2
import mediapipe as mp


cam = cv2.VideoCapture(0) # start the webcam
face_mesh = mp.solutions.face_mesh.FaceMesh() # load the face mesh model

while True:
    _, frame = cam.read() # read the frame from the webcam
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert frame to RGB
    output = face_mesh.process(rgb_frame) # process the frame
    landmarks_points = output.multi_face_landmarks # get the landmarks eg points on the face
    print(landmarks_points)
    cv2.imshow('Eye control mouse', frame)
    cv2.waitKey(1)
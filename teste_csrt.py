import cv2

print("Versão:", cv2.__version__)

tracker = cv2.TrackerCSRT_create()

print("Rastreador criado com sucesso!")
import cv2 #biblioteca pra trabalhar com imagens
import mediapipe as mp #biblioteca com ferramentas de reconhecimento de imagem

#inicializar o opencv e o mediapipe
webcam = cv2.VideoCapture(1)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    #ler frames da webcam
    verificador, frame = webcam.read()

    if not verificador:
        break

    #reconhecer rostos
    lista_rostos = reconhecedor_rostos.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:

            #desenha o contorno
            desenho.draw_detection(frame, rosto)


    cv2.imshow("Reconhecimento facial", frame)

    #parar o loop usando ESC
    if cv2.waitKey(5) == 27:
        break

webcam.release()


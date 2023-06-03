import cv2
import time
import math

p1 = 530
p2 = 300
xS = []
yS = []

video = cv2.VideoCapture("bb3.mp4")

# Cargar rastreador 
tracker = cv2.TrackerCSRT_create()

# Leer el primer cuadro del video
returned, img = video.read()

# Seleccionar el cuadro delimitador en la imagen
bbox = cv2.selectROI("Rastreando", img, False)

# Inicializar el rastreador en la imagen y el cuadro delimitador
tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)

    cv2.putText(img,"Rastreando Objeto",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def goal_track(img, bbox):
    x, y,w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])

    #######################
    # AGREGAR CÓDIGO AQUÍ #
    #######################
    #                     #
    #Obtener los putos centrales del cuadro delimitador###
    c1 = x + int(w/2)
    c2 = y + int(h/2)

    #Crear un circulo en medio
    cv2.circle(img, (c1, c2), 2, (255,0,53), 5)
    #Canasta
    cv2.circle(img, (int(p1), int(p2)), 2, (252,5,7), 5)

    #Calcular distancia#
    dist = math.sqrt(((c1-p1) **2) + (c2-p2)**2)
    print(dist)

    if (dist <= 20):
        cv2.putText(img,"Canasta",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2) 
    xS.append(c1) 
    yS.append(c2) 
    for i in range(len(xS)-1): 
        cv2.circle(img,(xS[i],yS[i]),2,(0,0,255),5)

    #                     #
    #######################

while True:
    
    check, img = video.read()   

    # Actualizar el rastreador en la imagen y el cuadro delimitador
    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img,"Perdido",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    #######################
    # AGREGAR CÓDIGO AQUÍ #
    #######################
    #                     #
    goal_track(img, bbox)
    


    #                     #
    #######################

    cv2.imshow("Resultado", img)
            
    key = cv2.waitKey(25)
    if key == 32:
        print("Detenido")
        break

video.release()
cv2.destroyALLwindows()
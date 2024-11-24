#importar la libreria de opencv
import cv2

#para leer una imagen 
img = cv2.imread('imagen_1.jpg')
#aqui la llamamos para poder mostrarla
cv2.imshow("ventana1", img)
#Se mostrara la imagen al presionar alguna tecla
cv2.waitKey()
cv2.destroyAllWindows()

#para guardar una imagen
cv2.imwrite('imagenguardar.jpg',img)
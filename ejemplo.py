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

##Gray Images-----
img_gray = cv2.imread('imagen_1.jpg', cv2.IMREAD_GRAYSCALE)
# Es lo mismo | img_gray = cv2.imread('imagen_1.jpg', 0)
cv2.imshow("ventana2",img_gray)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('imagenguardargris.jpg',img_gray)

##waitKey()
# Proyecto: Generación de Imágenes Híbridas

Este proyecto tiene como objetivo generar imágenes híbridas combinando dos imágenes de entrada mediante el uso de filtros espaciales. A medida que observes estas imágenes desde diferentes distancias, notarás que las características de cada imagen resaltan de manera distinta:

De cerca: Predominan las características de baja frecuencia de la primera imagen (suavizada).
De lejos: Sobresalen las características de alta frecuencia de la segunda imagen (bordes).
Este efecto también se puede simular reduciendo la escala de la imagen híbrida.


#Cómo Funciona el Programa

#1. Entrada

El programa requiere dos imágenes de entrada del mismo tamaño. Si las imágenes no tienen el mismo tamaño, el programa ajustará la segunda imagen para que coincida con la primera.

En el directorio imágenes/ del proyecto, encontrarás pares de imágenes listas para probar.

#2. Proceso
El programa aplica los siguientes filtros espaciales:

Filtro Gaussiano (Low-pass):

Este filtro suaviza la primera imagen, eliminando detalles de alta frecuencia.
Resultado: Una versión borrosa de la imagen que resalta características generales.
Filtro Laplaciano (High-pass):

Este filtro resalta los bordes y detalles finos de la segunda imagen.
Resultado: Una imagen donde predominan las características de alta frecuencia.
Combinación de Imágenes:

Las dos imágenes filtradas se combinan para formar una imagen híbrida.
De cerca: Verás los detalles de la primera imagen.
De lejos: Notarás las características de la segunda imagen.

#3. Salida

El programa genera dos versiones de la imagen híbrida:

Imagen híbrida completa: Una versión con la resolución original de las imágenes.
Imagen híbrida reducida: Una versión de 100x100 píxeles que simula cómo se ve la imagen desde lejos.

#Instrucciones para Ejecutar el Programa

#1. Requisitos
Python 3.8 o superior.
Instala las librerías necesarias con el siguiente comando:

pip install opencv-python numpy

#2. Configuración del Directorio
Coloca tus imágenes en la carpeta imágenes/ o especifica sus rutas en el código.
Edita las rutas en el archivo hybrid_image.py

img1_path = "imágenes/imagen1.jpg"  # Primera imagen (low-pass)
img2_path = "imágenes/imagen2.jpg"  # Segunda imagen (high-pass)
output_path = "imágenes/hybrid_full.jpg"  # Salida en tamaño completo
small_output_path = "imágenes/hybrid_small.jpg"  # Salida en tamaño reducido

#3. Ejecución
python hybrid_image.py

##Detalles del Código

#Cargar Imágenes

El programa utiliza cv2.imread para cargar las imágenes en formato color (BGR). Si las imágenes tienen tamaños diferentes, la segunda imagen se redimensiona automáticamente para que coincida con la primera.

#Filtro Gaussiano (Low-pass)

El filtro Gaussiano suaviza la primera imagen:

cv2.GaussianBlur(canal, gaussian_kernel, sigmaX=sigma)

Kernel: (31, 31) (ajustable).
Sigma: 15 (ajustable).

#Filtro Laplaciano (High-pass)

El filtro Laplaciano resalta los bordes y detalles finos de la segunda imagen:

cv2.Laplacian(canal, cv2.CV_64F, ksize=laplacian_ksize)

#Normalización

cv2.normalize(filtro, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

#Combinación de Imágenes

canal_hybrid = cv2.addWeighted(low_pass_channel, 0.5, high_pass_channel, 0.5, 0)

#Generación de Resultados

El programa genera dos versiones de la imagen híbrida:

Tamaño completo: Guardada como hybrid_full.jpg.
Tamaño reducido (100x100 píxeles): Guardada como hybrid_small.jpg.















 

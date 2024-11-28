import cv2
import numpy as np
import os

def create_hybrid_image(img1_path, img2_path, output_path, small_output_path, gaussian_kernel=(31, 31), sigma=15, laplacian_ksize=3):
    """
    Crea una imagen híbrida combinando imágenes en color con filtros Gaussiano y Laplaciano.

    Parámetros:
    - img1_path: Ruta de la primera imagen (low-pass).
    - img2_path: Ruta de la segunda imagen (high-pass).
    - output_path: Ruta para guardar la imagen híbrida en tamaño completo.
    - small_output_path: Ruta para guardar la imagen híbrida en tamaño pequeño.
    - gaussian_kernel: Tamaño del kernel para el filtro Gaussiano.
    - sigma: Desviación estándar para el filtro Gaussiano.
    - laplacian_ksize: Tamaño del kernel para el filtro Laplaciano.
    """
    # Verificar existencia de las imágenes
    if not os.path.exists(img1_path):
        raise FileNotFoundError(f"La primera imagen no existe: {img1_path}")
    if not os.path.exists(img2_path):
        raise FileNotFoundError(f"La segunda imagen no existe: {img2_path}")

    # Cargar imágenes en color
    img1 = cv2.imread(img1_path, cv2.IMREAD_COLOR)
    img2 = cv2.imread(img2_path, cv2.IMREAD_COLOR)

    if img1 is None or img2 is None:
        raise ValueError("No se pudieron cargar una o ambas imágenes. Verifica las rutas y el formato de los archivos.")

    # Asegurarse de que ambas imágenes tengan el mismo tamaño
    if img1.shape != img2.shape:
        print("Redimensionando imágenes para que tengan el mismo tamaño...")
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Dividir en canales BGR
    b1, g1, r1 = cv2.split(img1)
    b2, g2, r2 = cv2.split(img2)

    # Aplicar filtros Gaussiano (low-pass) y Laplaciano (high-pass) a cada canal
    b_low = cv2.GaussianBlur(b1, gaussian_kernel, sigmaX=sigma)
    g_low = cv2.GaussianBlur(g1, gaussian_kernel, sigmaX=sigma)
    r_low = cv2.GaussianBlur(r1, gaussian_kernel, sigmaX=sigma)

    b_high = cv2.Laplacian(b2, cv2.CV_64F, ksize=laplacian_ksize)
    g_high = cv2.Laplacian(g2, cv2.CV_64F, ksize=laplacian_ksize)
    r_high = cv2.Laplacian(r2, cv2.CV_64F, ksize=laplacian_ksize)

    # Normalizar los valores del high-pass

    b_high = cv2.normalize(b_high, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    g_high = cv2.normalize(g_high, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    r_high = cv2.normalize(r_high, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Combinar imágenes para cada canal
    b_hybrid = cv2.addWeighted(b_low, 0.5, b_high, 0.5, 0)
    g_hybrid = cv2.addWeighted(g_low, 0.5, g_high, 0.5, 0)
    r_hybrid = cv2.addWeighted(r_low, 0.5, r_high, 0.5, 0)

    # Fusionar canales en una imagen híbrida final
    hybrid_image = cv2.merge([b_hybrid, g_hybrid, r_hybrid])

    # Guardar la imagen híbrida en tamaño completo

    cv2.imwrite(output_path, hybrid_image)
    print(f"Imagen híbrida completa guardada en: {output_path}")

    # Reducir la imagen híbrida a un tamaño pequeño
    small_hybrid = cv2.resize(hybrid_image, (100, 100))
    cv2.imwrite(small_output_path, small_hybrid)
    print(f"Imagen híbrida pequeña guardada en: {small_output_path}")

    # Mostrar imágenes
    cv2.imshow("Low-Pass Image", cv2.merge([b_low, g_low, r_low]))
    cv2.imshow("High-Pass Image", cv2.merge([b_high, g_high, r_high]))
    cv2.imshow("Hybrid Image", hybrid_image)
    cv2.imshow("Hybrid Image (Small)", small_hybrid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Ejecución principal
if __name__ == "__main__":
    img1_path = "dog.jpg"           # Cambia esto por la ruta de tu primera imagen
    img2_path = "cat.jpg"           # Cambia esto por la ruta de tu segunda imagen
    output_path = "imagen_hibrida_completa.jpg"          # Ruta donde guardarás la imagen híbrida completa
    small_output_path = "imagen_hibrida_pequena.jpg"     # Ruta donde guardarás la imagen híbrida pequeña

    try:
        create_hybrid_image(img1_path, img2_path, output_path, small_output_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")


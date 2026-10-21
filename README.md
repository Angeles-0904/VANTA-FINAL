# VANTA — Smart Waste Intelligence Lab

Aplicación local de clasificación de residuos con tres checkpoints PyTorch reales: CNN desde cero, MobileNetV2 y ViT-B/16. La interfaz está en Streamlit y el orden de salida procede de `models/class_names.json`.

## Modelos y resultados

Se buscan checkpoints primero en `models/` y después en la ubicación original `D:\decimo\VAunidad1\MODELOS FINALES\`. `models/class_names.json` y `models/comparison_results.csv` contienen los metadatos pequeños del proyecto. Para mover la aplicación a otro equipo, copia los tres archivos `.pth` a `models/`; no se incluyen en este repositorio para evitar duplicar pesos grandes.

El CSV `comparison_results.csv` en `models/` alimenta Research Lab y Overview; si no está allí, la app busca junto a los archivos originales. Los resultados mostrados son los valores reportados por ese archivo; la app no los vuelve a calcular.

## Inicio en Windows y VS Code

1. Abre `D:\decimo\VAunidad1\VANTA` en VS Code.
2. Abre una terminal PowerShell en esa carpeta y crea el entorno:

   ```powershell
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   Si PowerShell bloquea la activación, usa `\.venv\Scripts\activate.bat` desde Command Prompt.

3. Instala PyTorch y torchvision apropiados para tu equipo desde el selector oficial de PyTorch. Después instala las dependencias restantes:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

   Para CPU, la instalación estándar de PyTorch funciona. El wheel de CUDA depende de tu GPU y controladores.

4. Ejecuta:

   ```powershell
   streamlit run app.py
   ```

5. En Live Vision o Model Arena, selecciona Webcam y permite el acceso a la cámara cuando el navegador lo solicite. También puedes cargar un JPG, PNG o WebP.

## Errores frecuentes

- **Checkpoint ausente:** verifica que los tres `.pth` están en `models/` o en `D:\decimo\VAunidad1\MODELOS FINALES\`.
- **No se encuentra class_names.json:** restaura el archivo original o colócalo en `models/`. Debe listar diez clases en el orden de entrenamiento.
- **Pesos incompatibles:** comprueba que el checkpoint corresponde a la arquitectura declarada y que la versión de torchvision puede construir MobileNetV2/ViT-B/16 con esas capas de salida. El cargador usa `strict=True` para exponer incompatibilidades.
- **torch/torchvision no se importan:** instala versiones compatibles desde el selector de PyTorch dentro del entorno `.venv` activo.
- **Cámara bloqueada:** concede permisos de cámara al navegador/sistema operativo y recarga la pestaña. El cargador de archivos es una alternativa.
- **Primera inferencia lenta o falta de memoria:** la primera predicción carga el checkpoint; ViT-B/16 requiere más memoria. Reiniciar Streamlit libera la memoria de los modelos.
- **No aparecen métricas:** coloca `comparison_results.csv` en `D:\decimo\VAunidad1\MODELOS FINALES\` o ajusta `METRICS_PATH` en `src/config.py`.

La app no entrena modelos automáticamente y no afirma que una predicción sea correcta sin etiqueta de referencia.

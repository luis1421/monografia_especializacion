# monografia_especializacion

Este repositorio se crea con el propósito de apoyar las labores de análisis y predicción, por lo tanto, está compuesto por paquetes de python (text_analysis) y una API creada con FastAPI (ml_app), la cual va a permitir desplegar el modelo entrenado para este trabajo.

Para el despliegue del modelo en AWS se siguieron los siguientes pasos:

1. Se entrenó el modelo en Google Colab con una GPU, posteriormente se guardó el modelo en el local.
2. Una vez se tiene una cuenta disponible en AWS, se sube el modelo en un bucket de S3 (contenedor de objetos).
3. Creación de aplicación en FastAPI para desplegar el modelo, la cual tiene su ambiente virtual, archivo requirements y  carga el modelo desde el bucket. 
4. Crear archivo de dockerfile e imagen de Docker.
5. Se crea un repositorio en amazon ECR, donde se va a guardar la imagen de Dokcer
6. Se crea una máquina virtual en EC2 de aws (t2.large, CPU 2, RAM 8 GB). 
7. Dentro de la máquina virtual creada se extrae la imagen del repositorio, se corre, se activan los permisos y el modelo queda desplegado como un Endpoint.

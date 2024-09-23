# Info de la materia: ST0263: Tópicos Especiales en Telemática
#
# Estudiante(s):
### Angel Martinez Doria, admartined@eafit.edu.co
### David Londoño Sanchez, dlondonos2@eafit.edu.co

# Profesor: Juan Carlos Montoya Mendoza, jcmontoy@eafit.edu.co

# Reto N1. Aplicaciones P2P
#
# 1. breve descripción de la actividad
En esta actividad se implementó una red P2P con un tracker que facilita el descubrimiento de nodos. Cada nodo actúa tanto como cliente y servidor, permitiendo la comunicación directa entre nodos a través de gRPC. La solución fue diseñada, desarrollada y probada en un ambiente distribuido utilizando contenedores Docker desplegados en AWS.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Ejecucion y registro de nodos: Los nodos se inician y registran correctamente con el tracker y actualizan su estado.
- Descubrimiento de nodos: Los nodos pueden solicitar al tracker la información de otros nodos activos para establecer conexiones.
- Subida de archivos al sistema.
- Descarga de archivos desde la red.
- Búsqueda de archivos disponibles.
- Registro de pares en el tracker.
- Consulta de pares que poseen un archivo específico.
- Partición de archivos en trozos para la transferencia.
- Uso de gRPC para la comunicación cliente-servidor y entre pares.
- Definición de servicios y mensajes en un archivo .proto.
- Manejo de múltiples peticiones concurrentes en el servidor utilizando ThreadPoolExecutor.

## 1.2.  Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Mecanismos de desconexion para tolerancia de fallas: El tracker no cuenta con un mecanismo robusto para manejar caídas de nodos o desconexiones inesperadas, lo que podría generar inconsistencias en la lista de nodos activos.
- Almacenamiento/recuperación eficiente: El almacenamiento de archivos se realiza de forma básica en el sistema de archivos local, sin utilizar estructuras de datos distribuidas o optimizadas.
- Transferencia de archivos real: La transferencia de archivos se simula, no se realiza una transmisión real de datos entre pares.
- Replicación robusta: La replicación de archivos se implementa de forma básica y podría mejorarse para garantizar la disponibilidad y tolerancia a fallos.
- Sistema completamente distribuido y descentralizado: El uso de un tracker centralizado introduce un punto único de fallo.
- Se hizo el intento pero por problemas de tiempo no se logro el despliegue en AWS correctamente:
![WhatsApp Image 2024-09-22 at 11 23 51 PM](https://github.com/user-attachments/assets/b8c1eb6f-5b23-4e4c-b50f-b317c6222db0)

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
- Arquitectura: La arquitectura sigue un patrón cliente-servidor dentro de una red P2P. El tracker actúa como servidor de descubrimiento, mientras que los nodos actúan como clientes/servidores. El diseño también utiliza el patrón de comunicación gRPC para permitir el intercambio de datos.
![Red P2P](https://github.com/user-attachments/assets/e8e9b698-53cd-4727-99a3-89d751e50374)
#### Patrones y buenas prácticas:
- Separación de responsabilidades: El tracker solo maneja el descubrimiento y no interviene en la comunicación entre nodos.
- Uso de hilos (Threads) en los nodos para manejar múltiples conexiones concurrentes.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

### - Lenguaje de programación: Python 3.x
#### Librerías:
- grpc (versión 1.66.1 o superior)
- protobuf (versión 3.x)
- concurrent.futures
- threading
- os
- sys
- socket
- queue

## detalles del desarrollo.
- El código del cliente y del servidor se encuentra en los archivos peer_client.py y tracker_server.py, respectivamente.
- El archivo p2p.proto define los servicios gRPC, los mensajes y los tipos de datos utilizados para la comunicación.
- Los archivos p2p_pb2.py y p2p_pb2_grpc.py son generados automáticamente a partir de p2p.proto y contienen las clases y métodos necesarios para interactuar con los servicios gRPC.

## Organización del código
#### Estructura de directorios:
- /src
- /tracker.py
- /peer.py``
- /proto_files/
- /tracker.proto
- /peer.proto

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

- Lenguaje de programación: Python 3.9
- Librerías:
- grpcio (v1.41.0)
- protobuf (v3.17.3)
- Otros mencionados en la sección anterior.
- Ambiente de ejecución:
#

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
Los puertos son configurados por gRcp, no se cuenta con base de datos pues cada peer sube y baja archivos entre ellos, y le preguntan al tracker donde están ubicados

## como se lanza el servidor.
Para lanzar el sistema lo primero es correr el tracker "python tracker.py" luego se corre la cantidad de peers que se desee "python peer.py" (correr al menos 2). Luego la consola de los peers presenta 3 comandos, upload, search y download; para subir un archivo a la red escribimos upload en consola, luego copiamos la dirección del archivo desde el explorador de archivos de windows. Para buscar o descargar un archivo que se encuentra en la red, copiaremos el comando respectivo y escribimos el nombre y tipo de archivo del archivo que se busca.

# mostrar resultados o pantallazos
![WhatsApp Image 2024-09-22 at 11 20 12 PM](https://github.com/user-attachments/assets/59444d97-bbcc-478f-9286-b99668e238e8)

# Referencias:
### Choles, J. J. [@johanj.choles5566]. (s/f). Sistema P2P comunicación por API REST y gRPC. Youtube. Recuperado de https://www.youtube.com/watch?v=gJkHndseGgc
### Feregrino [@feregri_no]. (s/f). RPC - Usando gRPC en Python y C#. Youtube. Recuperado de https://www.youtube.com/watch?v=2oY9PbaE71A
### gRPC Python Quickstart: https://grpc.io/docs/languages/python/quickstart/
### Protobuf Language Guide: https://developers.google.com/protocol-buffers/docs/proto3

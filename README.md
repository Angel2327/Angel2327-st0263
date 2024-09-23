# Info de la materia: ST0263: Tópicos Especiales en Telemática
#
# Estudiante(s):
### Angel Martinez Doria, admartined@eafit.edu.co
### David Londoño Sanchez, dlondonos2@eafit.edu.co

# Profesor: Juan Carlos Montoya Mendoza, jcmontoy@eafit.edu.co

# Reto N1. Aplicaciones P2P`
#`
# 1. breve descripción de la actividad
En esta actividad se implementó una red P2P con un tracker que facilita el descubrimiento de nodos. Cada nodo actúa tanto como cliente y servidor, permitiendo la comunicación directa entre nodos a través de gRPC. La solución fue diseñada, desarrollada y probada en un ambiente distribuido utilizando contenedores Docker desplegados en AWS.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Ejecucion y registro de nodos: Los nodos se inician y registran correctamente con el tracker y actualizan su estado.
Descubrimiento de nodos: Los nodos pueden solicitar al tracker la información de otros nodos activos para establecer conexiones.
Subida de archivos al sistema.
Descarga de archivos desde la red.
Búsqueda de archivos disponibles.
Registro de pares en el tracker.
Consulta de pares que poseen un archivo específico.
Partición de archivos en trozos para la transferencia.
Comunicación entre pares:
Uso de gRPC para la comunicación cliente-servidor y entre pares.
Definición de servicios y mensajes en un archivo .proto.
Manejo de múltiples peticiones concurrentes en el servidor utilizando ThreadPoolExecutor.
Despliegue en AWS: Se realizó el despliegue de la red P2P utilizando instancias de AWS, cumpliendo con el requerimiento de entorno distribuido.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Mecanismos de desconexcion para tolerancia de fallas: El tracker no cuenta con un mecanismo robusto para manejar caídas de nodos o desconexiones inesperadas, lo que podría generar inconsistencias en la lista de nodos activos y con el tracker se genera un punto de falla y no tiene replicación ni un mecanismo de respaldo en caso de fallo.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
Arquitectura: La arquitectura sigue un patrón cliente-servidor dentro de una red P2P. El tracker actúa como servidor de descubrimiento, mientras que los nodos actúan como clientes/servidores. El diseño también utiliza el patrón de comunicación gRPC para permitir el intercambio de datos.
Patrones y buenas prácticas:
Separación de responsabilidades: El tracker solo maneja el descubrimiento y no interviene en la comunicación entre nodos.
Uso de contenedores Docker para facilitar el despliegue y la escalabilidad.
Uso de hilos (Threads) en los nodos para manejar múltiples conexiones concurrentes.
Despliegue distribuido utilizando AWS para simular un entorno de red P2P realista.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

#### Lenguaje de programación: Python 3.9
#### Librerías y paquetes:
#### grpcio (v1.41.0): Para la implementación de las comunicaciones gRPC.
#### protobuf (v3.17.3): Para serialización de datos entre los nodos.
#### docker (v20.10.8): Para contenedores y despliegue.
#### Otros: threading, socket, os, json para el manejo interno de la red P2P.

## detalles del desarrollo.
Los nodos se registran automáticamente en el tracker y comienzan a intercambiar datos con otros nodos una vez descubiertos.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

# Organización del código
#### Estructura de directorios:
#### /src
   ####  /tracker.py
   ####  /peer.py
   ####  /proto_files/
   ####      /tracker.proto
   ####      /peer.proto

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

#### Lenguaje de programación: Python 3.9
#### Librerías:
#### grpcio (v1.41.0)
#### protobuf (v3.17.3)
#### Otros mencionados en la sección anterior.
#### Ambiente de ejecución:
#### AWS EC2 (Ubuntu 20.04)
#

## IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# Referencias:
### Choles, J. J. [@johanj.choles5566]. (s/f). Sistema P2P comunicación por API REST y gRPC. Youtube. Recuperado de https://www.youtube.com/watch?v=gJkHndseGgc
### Feregrino [@feregri_no]. (s/f). RPC - Usando gRPC en Python y C#. Youtube. Recuperado de https://www.youtube.com/watch?v=2oY9PbaE71A

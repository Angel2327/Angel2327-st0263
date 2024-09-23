# info de la materia: ST0263: Tópicos Especiales en Telemática
#
# Estudiante(s):
# Angel Martinez Doria, admartinedeafir.edu.co
# David Londoño Sanchez, dlondonos2@eafit.edu.co

# Profesor: Juan Carlos Montoya Mendoza, jcmontoy@eafit.edu.co

# Reto N1. Aplicaciones P2P
#
# 1. breve descripción de la actividad
#
En esta actividad se implementó una red P2P con un tracker que facilita el descubrimiento de nodos. Cada nodo actúa tanto como cliente y servidor, permitiendo la comunicación directa entre nodos a través de gRPC. La solución fue diseñada, desarrollada y probada en un ambiente distribuido utilizando contenedores Docker desplegados en AWS.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
Arquitectura: La arquitectura sigue un patrón cliente-servidor dentro de una red P2P. El tracker actúa como servidor de descubrimiento, mientras que los nodos actúan como clientes/servidores. El diseño también utiliza el patrón de comunicación gRPC para permitir el intercambio de datos.
Patrones y buenas prácticas:
Separación de responsabilidades: El tracker solo maneja el descubrimiento y no interviene en la comunicación entre nodos.
Uso de contenedores Docker para facilitar el despliegue y la escalabilidad.
Uso de hilos (Threads) en los nodos para manejar múltiples conexiones concurrentes.
Despliegue distribuido utilizando AWS para simular un entorno de red P2P realista.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

Lenguaje de programación: Python 3.9
Librerías y paquetes:
grpcio (v1.41.0): Para la implementación de las comunicaciones gRPC.
protobuf (v3.17.3): Para serialización de datos entre los nodos.
docker (v20.10.8): Para contenedores y despliegue.
Otros: threading, socket, os, json para el manejo interno de la red P2P.

## como se compila y ejecuta.
## detalles del desarrollo.
Los nodos se registran automáticamente en el tracker y comienzan a intercambiar datos con otros nodos una vez descubiertos.
## detalles técnicos
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
Organización del código
Estructura de directorios:
/src
    /tracker.py
    /peer.py
    /proto_files/
        /tracker.proto
        /peer.proto
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto

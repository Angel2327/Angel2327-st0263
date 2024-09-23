# Defina la versión inicial de la arquitectura y tipo de red P2P, revísela con otros compañeros y reciba retroalimentación del profesor.
•	Tipo de red P2P:
o	La arquitectura incluye un tracker centralizado, que facilita el descubrimiento y la coordinación de los nodos.
•	Componentes clave:
o	Tracker: Registra nodos activos y proporciona información de otros nodos.
o	Nodo Peer: Actúa como cliente y servidor, intercambiando datos y comunicándose con el tracker para obtener información sobre otros peers.
o	Protocolos de comunicación: Se usa gRPC para facilitar las comunicaciones entre el tracker y los nodos, y también entre los propios nodos.

# Defina los servicios específicos que tendrá cada componente del sistema
Tracker:
Registro de nodos: Mantiene una lista de nodos activos.
Descubrimiento de nodos: Facilita la obtención de información de otros nodos.
Actualización de la red: Proporciona actualizaciones sobre los nodos que se conectan o desconectan.
o	RegisterPeer(PeerInfo): Registra un nuevo par en el sistema, incluyendo su dirección y los archivos que posee.
o	QueryPeers(FileRequest): Devuelve una lista de pares que poseen un archivo específico.
Nodo Peer:
Conexión al tracker: Registra su existencia en el tracker.
Descubrimiento de pares: Solicita información al tracker sobre otros nodos activos.
Intercambio de datos: Comunica e intercambia datos directamente con otros nodos.
o	UploadFile(FileChunk): Sube un trozo de archivo a otro par.
o	DownloadFile(FileRequest): Descarga un trozo de archivo desde otro par.
o	SearchFile(filename): Busca pares que poseen un archivo específico (a través del tracker).
o	RetrieveFile(filename): Descarga un archivo completo desde la red (coordinando la descarga de trozos desde múltiples pares).
gRPC Server: Gestiona la comunicación entre los nodos y el tracker.

# Definir el mecanismo de localización basado en índice central o distribuido (ideal distribuido)
Índice centralizado:
•	El tracker mantiene un índice centralizado que mapea nombres de archivo a listas de pares que poseen esos archivos.
•	Los pares consultan al tracker para descubrir otros pares que tienen los archivos que desean.
Defina las interacciones entre componentes, los tipos de comunicaciones y tipo de middleware específico que va a emplear (REST API, gRPC), debe emplear todos estos middlewares.
•	Interacciones:
o	Los pares se registran en el tracker al iniciar.
o	Los pares consultan al tracker para buscar archivos y obtener listas de pares.
o	Los pares se comunican directamente entre sí para transferir trozos de archivos.
•	Comunicaciones:
o	gRPC para la comunicación cliente-servidor entre pares y el tracker.
o	gRPC (o potencialmente un protocolo de transferencia de archivos más eficiente) para la comunicación directa entre pares.
•	Middleware:
o	gRPC se utiliza como middleware principal para la comunicación estructurada y la generación de código cliente/servidor.
o	REST API podría utilizarse para proporcionar una interfaz web para interactuar con el sistema o para exponer funcionalidades a otras aplicaciones.

# Plan de Desarrollo
1.	Victoria temprana: Comunicación básica entre pares y tracker 
o	Implementar los servicios gRPC básicos en el tracker y los pares.
o	Permitir que los pares se registren en el tracker y consulten la lista de pares para un archivo.
2.	Subida y descarga de archivos 
o	Implementar la lógica para dividir archivos en trozos y transferirlos entre pares.
o	Agregar la funcionalidad de subida y descarga de archivos en los pares.
3.	Búsqueda y recuperación de archivos 
o	Implementar la funcionalidad de búsqueda de archivos en los pares (a través del tracker).
o	Coordinar la descarga de múltiples trozos de archivo desde diferentes pares para recuperar un archivo completo.
4.	Replicación de archivos (implementado, pero puede mejorarse)
o	Implementar la lógica para replicar trozos de archivo en múltiples pares para aumentar la disponibilidad y tolerancia a fallos.


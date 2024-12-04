from spyne import Application, ServiceBase, rpc, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import logging

# Configuración de logging para guardar en un archivo, ajustado para evitar detalles extensos
logging.basicConfig(
    filename='soap_requests.log',  # El archivo donde se guardarán los logs
    level=logging.INFO,  # Usar INFO en lugar de DEBUG para menos detalle
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato de salida
)
logging.getLogger('zeep.transports').setLevel(logging.INFO)

# Definición del servicio SOAP
class MyService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b

# Crear la aplicación SOAP con el servicio
application = Application([MyService], tns='tns.example', in_protocol=Soap11(), out_protocol=Soap11())

# Configurar el servidor WSGI
wsgi_application = WsgiApplication(application)

# Ejecutar el servidor en localhost en el puerto 8000
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 8000, wsgi_application)
    print("Servidor SOAP corriendo en http://localhost:8000")
    server.serve_forever()




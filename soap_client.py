import zeep
import logging

# Configuración de logging para guardar en un archivo
logging.basicConfig(
    filename='soap_requests.log',  # El archivo donde se guardarán los logs
    level=logging.INFO,  # Usar INFO en lugar de DEBUG para menos detalle
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato de salida
)
logging.getLogger('zeep.transports').setLevel(logging.INFO)

# URL del servicio SOAP
url = 'http://localhost:8000/?wsdl'

# Crear un cliente con la URL del servicio WSDL
client = zeep.Client(url)

# Solicitar los números a sumar desde el usuario
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

# Realizar una llamada al servicio SOAP
result = client.service.add(a, b)

# Mostrar el resultado
print(f"Resultado de la suma: {result}")




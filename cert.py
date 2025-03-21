import ssl
import socket

def download_cert(host, port, cert_file, ca_cert_path):
    # Crear una conexión SSL al servidor usando el archivo CA
    context = ssl.create_default_context(cafile=ca_cert_path)
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)

    try:
        # Conectar al servidor y obtener el certificado
        conn.connect((host, port))
        cert = conn.getpeercert(True)  # Obtener el certificado en formato binario

        # Guardar el certificado en un archivo
        with open(cert_file, 'wb') as f:
            f.write(cert)

        print(f"Certificado guardado en {cert_file}")

    except Exception as e:
        print(f"Error al obtener el certificado: {e}")

    finally:
        # Cerrar la conexión
        conn.close()

# Parámetros
host = 'api.bcra.gob.ar'
port = 443
cert_file = './cert/CERT.pem'  # Ruta del archivo donde guardar el certificado
ca_cert_path = './cert/sectigo-ca.pem'  # Ruta del certificado raíz descargado de Sectigo

# Descargar el certificado
download_cert(host, port, cert_file, ca_cert_path)

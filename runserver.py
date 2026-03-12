from waitress import serve
from learning_log.wsgi import application  # Reemplaza 'mi_proyecto' por el nombre de tu carpeta

if __name__ == '__main__':
    print("Servidor Django corriendo en http://localhost:8080")
    serve(application, host='0.0.0.0', port=8080)
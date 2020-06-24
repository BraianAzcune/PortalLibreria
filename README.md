# PortalLibreria
proyecto para distribuido

#en linux usar
git clone <direccion>
# luego debe crear un entorno virtual, sin entrar a la carpeta PortalLibreria hacer:
python3 -m venv PortalLibreria
#luego entre al entorno virtual
source PortalLibreria/bin/activate
#finalmente ejecute pip para cargar las dependencias
pip install -r PortalLibreria/requirements.txt

#para ejecutar el servidor realice
python manage.py runserver 80

#si a cerrado la terminal, para volver a ejecutar necesita entrar al entorno virutal, se hace tal cual en la linea  9

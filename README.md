# Onestick
Prueba tecnica Onestick

Preparación del entorno de desarrollo
Para empezar con el desarrollo del proyecto, se deben instalar unos prerequisitos en el sistema.Suponemos un entorno de desarrollo linux.

Python
Se requiere de una instalación de Python 3.9. Se puede descargar el instalador para el sistema operativo de tu elección en la web oficial de Python.

python -V
Lo que nos debería dar una respuesta parecida a:

Python #.#.##
De lo contario, se deberá configurar correctamente.

Para sistemas Linux debera ejercutarse en terminal:

sudo apt-get update
sudo apt-get install python3.9

Pip
Pip es el administrador de paquetes que se usa en el proyecto. Normalmente viene preinstalado en Python, pero nos podemos asegurar ejecutando el siguiente comando en el terminal:

python -m ensurepip

Dependencias

Requiere python-multipart  pip install python-multipart
Descargaras el archivo prueba.zip y descomprimiras. Nos situamos dentro de la carpeta descomprimida y comenzamos con la instalacion de dependencias mediante una terminal.

El proyecto requiere que se instalen algunos paquetes de Python. Usaremos Pip, y el archivo requirements.txt con el siguiente comando:

python -m pip install -r requirements.txt

Una vez se tengan instaladas todas las dependencias, y el projecto descargado como esta en el repositorio se podrá proceder con el desarrollo o ejecución del proyecto.

La ejecución del programa se realizara con el siguiente comando en la carpeta donde se encuentre los archivos:

uvicorn main:app --reload

Las diferentes funciones se realizan en las siguientes url:

http://127.0.0.1:8000/docs

En ella podemos encontrar las diferentes funciones

Las tres primeras(total,compasxproducto,ranking) son los tres reportes. Para ejecutarlos debera hacer click en el que desea, despues en try out y finalmente enel boton execute. Los tres get devuelven el archivo generado en formato json.

/upload obtendra un archivo y lo guardara, si no tiene de nombre customers.csv,orders.csv o products.csv tambien se guarda pero no sustituye ninguno de estos

/download descargara un archivo que este almacenado se debera llenar el nombre ocn la extension del archivo

/delete borra un archivo que este almacenado se debera llenar el nombre ocn la extension del archivo

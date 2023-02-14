# Onestick
Prueba tecnica Onestick

Preparación del entorno de desarrollo
Para empezar con el desarrollo del proyecto, se deben instalar unos prerequisitos en el sistema.Suponemos un entorno de desarrollo linux.

Python
Se requiere de una instalación de Python. Se puede descargar el instalador para el sistema operativo de tu elección en la web oficial de Python.

python -V
Lo que nos debería dar una respuesta parecida a:

Python #.#.##
De lo contario, se deberá configurar correctamente.

Para sistemas Linux debera ejercutarse en terminal:

sudo apt-get update
sudo apt-get install python3.8

Pip
Pip es el administrador de paquetes que se usa en el proyecto. Normalmente viene preinstalado en Python, pero nos podemos asegurar ejecutando el siguiente comando en el terminal:

python -m ensurepip

Dependencias

Descargaras el archivo prueba.zip y descomprimiras. Nos situamos dentro de la carpeta descomprimida y comenzamos con la instalacion de dependencias mediante una terminal.

El proyecto requiere que se instalen algunos paquetes de Python. Usaremos Pip, y el archivo requirements.txt con el siguiente comando:

python -m pip install -r requirements.txt

Una vez se tengan instaladas todas las dependencias, y el projecto descargado como esta en el repositorio se podrá proceder con el desarrollo o ejecución del proyecto.

La ejecución del programa se realizara con el siguiente comando en la carpeta donde se encuentre los archivos:

uvicorn main:app --reload

Las diferentes funciones se realizan en las siguientes urls:

Reporte 1:

http://127.0.0.1:8000/total

Que generara el archivo order_prices.csv y retornara a la pagina web este archivo en formato json.

Reporte 2:

http://127.0.0.1:8000/comprasxproducto

Que generara el archivo products_customers.csv y retornara a la pagina web este archivo en formato json.

Reporte 3:

http://127.0.0.1:8000/ranking

Que generara el archivo customer_ranking.csv y el archivo order_prices.csv (necesitamos actualizar este archivo) y retornara a la pagina web el primer archivo en formato json.

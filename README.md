# actividad-c2-2bim
-----

### Primera Parte

* Realizar una lectura comprensiva del texto: La guía definitiva de Django: Desarrolla aplicaciones web de forma rápida y sencilla; exactamente de las páginas: 3 a la 8.
* Verificar que al menos una máquina del grupo tengo disponible Docker
* Realizar un organizador gráfico del contenido leído (creado a mano escrita)
* Subir la imagen del gráfico a la wiki de este repositorio

-----

### Segunda Parte

* Seguir indicaciones

* Copiar los archivos Dockerfile y hello.py a la carpeta ejemplo-cgi

* Dentro de la carpeta ejecutar en un terminal

  *   docker build -t apache-cgi .
  *   docker run -d -p 8080:80 apache-cgi

* En un navegador ingresar la siguiente dirección

  * http://localhost:8080/cgi-bin/hello.py

* En la wiki, crear una nueva página y explicar que está intentando hacer hello.py, subir una evidencia que el código fue ejecutado de manera exitosa

* Reformular la idea de hello.py, usando un framework MVC como flask, ubicar dicho código en la carpeta ejemplo-flask

* En un nueva hoja de la wiki, subir evidencia y explicar el funcionamiento

Run 'docker buildx build --help' for more information
luis@luis:~$ 

python app.py

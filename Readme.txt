Instalemos cosas necesarias para ejecutarlo
primero tenemos que saber que es un script escrito en python
por lo tanto vas a necesitar seguir los siguientes pasos

1. Ve al sitio web oficial de Python en https://www.python.org/downloads/.

2. En la página de descargas, verás las últimas versiones de Python disponibles. Selecciona la versión que deseas instalar. Si no tienes una preferencia específica, puedes elegir la versión estable más reciente.

3. A continuación, elige el instalador adecuado para tu sistema operativo. Hay instaladores para Windows, macOS y distribuciones de Linux. Asegúrate de seleccionar el instalador correcto para tu sistema.

4. Haz clic en el enlace de descarga del instalador seleccionado y guarda el archivo en tu computadora.

5. Una vez que se haya completado la descarga, ejecuta el archivo de instalación. En Windows, esto generalmente se realiza haciendo doble clic en el archivo `.exe` descargado.

6. En el instalador de Python, verás algunas opciones. Asegúrate de marcar la casilla "Agregar Python al PATH" para que Python se configure correctamente en tu sistema.

7. Puedes elegir la ubicación de instalación y otras opciones según tus preferencias. Para una instalación básica, puedes dejar las opciones predeterminadas y hacer clic en "Instalar".

8. El instalador comenzará a instalar Python en tu computadora. Esto puede llevar unos minutos.

9. Una vez que se haya completado la instalación, verás un mensaje indicando que Python se ha instalado correctamente. Haz clic en "Cerrar" para finalizar el instalador.

Después de instalar Python, puedes abrir una ventana de símbolo del sistema (CMD) y ejecutar el comando `python` para verificar que la instalación se haya realizado correctamente. También puedes ejecutar `pip` para instalar paquetes adicionales si es necesario.

Recuerda que los pasos pueden variar ligeramente según el sistema operativo que estés utilizando, pero en general, el proceso de instalación es similar.

Configuremos bien el script
1- entra al archivo que diga App2.py
2- anda a la linea numero 12 la cual tiene lo siguiente
    self.music_folder = 'C:/PycharmProject/MusicServer/MusicProject'
Cambia la ruta por la ruta donde tengas la musica que queres reproducir
no te olvides de cambiar \ por /.


Creamos un servicio NSSM
1- Descargamos el NSSM en la siguiente ruta https://nssm.cc/download (nssm 2.24.zip)
    1.1- Extraemos el contenido y lo guardamos en cualquier directorio (el que mas prefieras)
2- abrimos CMD y vamos la ruta donde tenemos el .exe que necesitamos (dentro del zip tenemos NSSM.exe tanto para windows 32 como 64)
3- Para instalar el siguiente servicio ejecutamos el siguiente codigo 
    nssm install NombreDelServicio "Ruta\Al\Python\python.exe" "Ruta\Al\Script\reproductor_musica.py"
Recorda cambiar NombreDelServicio por el nombre que quieras, "Ruta\Al\Python\python.exe"  por la ruta del interprete y 
"Ruta\Al\Script\reproductor_musica.py" por la ruta del Script
4- Hora de ejecutar el servicio
    4.1- Para iniciar usamos nssm restart "Mi Servicio de musica"
    4.2- Para parar el servicio usamos nssm stop "Mi Servicio de musica"
5- Para eliminar un servicio se usa el siguiente codigo en la CMD
nssm restart "Mi Servicio de musica"
Acordate de estar en la ruta donde esta guardado el NSSM.exe (win32 o win64)


NSSM no inicia automáticamente los servicios al iniciar sesión o al encender el dispositivo. Sin embargo, puedes configurar NSSM para que el servicio se inicie automáticamente al iniciar sesión en Windows utilizando el Programador de tareas.

Aquí hay algunos pasos para configurar NSSM y hacer que el servicio se inicie automáticamente al iniciar sesión:

1. Abre el Programador de tareas de Windows. Puedes buscar "Programador de tareas" en el menú de inicio o abrirlo desde el Panel de control.

2. En el panel izquierdo del Programador de tareas, haz clic con el botón derecho en "Biblioteca del Programador de tareas" y selecciona "Crear carpeta". Dale un nombre a la carpeta (por ejemplo, "Mis Servicios") y haz clic en "Aceptar" para crearla.

3. Haz clic con el botón derecho en la carpeta recién creada y selecciona "Crear tarea básica".

4. Sigue los pasos del asistente para crear la tarea básica. Asegúrate de configurar la tarea para que se ejecute al iniciar sesión en Windows. Puedes seleccionar la opción "Al iniciar sesión" o "Al iniciar el equipo", dependiendo de tus necesidades.

5. En la acción de la tarea, configura el programa o script para que ejecute NSSM con los parámetros adecuados para iniciar el servicio. Por ejemplo:
   ```
   C:\Ruta\A\nssm\nssm.exe start "NombreDelServicio"
   ```

   Asegúrate de reemplazar "NombreDelServicio" con el nombre real del servicio que has creado con NSSM.

6. Completa el resto de la configuración de la tarea según tus preferencias. Puedes ajustar la configuración de desencadenadores, condiciones y configuraciones adicionales según tus necesidades.

7. Haz clic en "Finalizar" para crear la tarea.

Una vez que hayas configurado la tarea en el Programador de tareas, NSSM se iniciará automáticamente al iniciar sesión en Windows y ejecutará el servicio especificado. Puedes reiniciar tu dispositivo y verificar que el servicio se inicie automáticamente después del inicio de sesión.

Recuerda que los pasos pueden variar ligeramente según la versión de Windows que estés utilizando, pero en general, el enfoque es similar.
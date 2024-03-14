# Desafío Guiado: Membresía

Este proyecto es un desafío que debo realizar

## Descripción

Este proyecto consiste en desarrollar la estructura de clases que permita crear membresías para usuarios suscriptores de una aplicación de streaming de videos de películas y series chilenas. Se deben implementar 5 tipos de membresías: Gratis, Básica, Familiar, Sin Conexión y Pro.

Cada tipo de membresía tiene características específicas en cuanto a costo, cantidad máxima de dispositivos permitidos y funcionalidades adicionales. Por ejemplo, la membresía Básica tiene un costo de $3000 y permite hasta 2 dispositivos, mientras que la membresía Pro tiene un costo de $7000 y permite hasta 6 dispositivos, además de permitir modificar el control parental y aumentar la cantidad máxima de contenido disponible para ver sin conexión.

El objetivo principal es diseñar la estructura de clases que permita crear estas membresías y realizar cambios de suscripción manteniendo la información del suscriptor (correo electrónico y número de tarjeta).

## Empezando 🚀

Estas instrucciones te guiarán para obtener una copia de este proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Prerrequisitos 📋

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

Sistema Operativo: (por ejemplo, Ubuntu 20.04, Windows 10)
Python: Este proyecto está desarrollado en Python. Necesitarás tener instalada al menos la versión 3.6.
Git: Necesitarás tener Git instalado en tu máquina para clonar el repositorio.
Editor de texto o IDE: Puedes usar cualquier editor de texto o un entorno de desarrollo integrado (IDE) de tu elección. Algunas opciones populares incluyen Visual Studio Code, PyCharm y Sublime Text.

### Instalación 🔧

Clonar el repositorio es el primer paso para obtener una copia del proyecto en tu computadora local. Este proceso implica descargar todos los archivos y el historial de cambios del repositorio remoto, que puede estar alojado en plataformas como GitHub, GitLab, entre otras, y almacenarlos en tu máquina para que puedas trabajar con ellos.

Aquí te detallo cada parte del proceso:

git clone: Esta es la instrucción de Git que le indica al sistema que deseas clonar un repositorio. Git es una herramienta ampliamente utilizada para el control de versiones en el desarrollo de software.

urlgit: Aquí es donde debes proporcionar la URL del repositorio que deseas clonar. Puedes obtener esta URL desde la plataforma de alojamiento de tu repositorio, como GitHub. La URL suele tener una estructura similar a https://github.com/tu_usuario/tu_repositorio.git.

Terminal: Es una interfaz de línea de comandos que te permite interactuar con tu sistema operativo mediante comandos de texto. En sistemas como Linux y macOS, esta terminal a menudo se llama simplemente "Terminal" o "Consola". En Windows, puedes utilizar el "Símbolo del sistema" o "Git Bash".

Ejecutar el comando: Una vez que hayas abierto tu terminal, simplemente escribe el comando git clone seguido de la URL del repositorio que deseas clonar. Después de presionar Enter, Git comenzará a descargar todos los archivos del repositorio en un directorio en tu máquina local.

Al seguir estos pasos, habrás clonado exitosamente el repositorio y estarás listo para comenzar a trabajar en él en tu propia computadora

## Estructura del proyecto📁

El proyecto está organizado de la siguiente manera:

membresia.py: Este archivo contiene las definiciones de las clases que representan los diferentes tipos de membresías disponibles en la aplicación de streaming. En este archivo se encuentran las implementaciones de las clases Gratis, Basica, Familiar, SinConexion y Pro, junto con sus métodos asociados. Aquí se establecen las propiedades y comportamientos específicos de cada tipo de membresía, como el costo, la cantidad máxima de dispositivos permitidos y las funcionalidades adicionales.

main.py: En este archivo se encuentran los ejemplos de uso de las clases de membresía definidas en membresia.py. Contiene código que muestra cómo crear instancias de diferentes tipos de membresías y realizar cambios de suscripción utilizando los métodos proporcionados por las clases. Este archivo sirve como una especie de "demo" o "prueba" del funcionamiento del sistema de membresías.

## Uso del programa 🚀

El programa principal main.py contiene ejemplos de cómo utilizar las clases de membresía para crear instancias de diferentes tipos de membresías y realizar cambios de suscripción.

Para ejecutar el programa, simplemente abre una terminal, navega hasta la carpeta del proyecto y ejecuta el siguiente comando:
python main.py
Esto mostrará en la consola los resultados de las pruebas realizadas con las clases de membresía

## Agradecimientos 🙏

Agradezco a Desafío Latam por proporcionar este desafío y la oportunidad de aprender y practicar habilidades de programación.

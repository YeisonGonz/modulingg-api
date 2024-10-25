# Modulingg API | 📦

## ¿En qué se basa este proyecto?

Modulatingg API es una base sólida diseñada para facilitar la creación de un backend escalable y organizado utilizando Python y FastAPI 🐍. La idea es proporcionar un entorno plug-and-play en el que los desarrolladores puedan construir módulos independientes con la estructura adecuada. Una vez configurados, solo es necesario añadir estos módulos a la carpeta correspondiente para que funcionen de inmediato.

## Como empezar a programar ? 🧑‍💻

Para iniciar con el desarrollo, sigue estos pasos:

1. **Descarga el proyecto en tu equipo**: Clona o descarga el repositorio en tu máquina local.

2. **Configura un entorno virtual de Python**: Esto te permitirá aislar las dependencias del proyecto del resto del sistema, asegurando que las versiones de las librerías utilizadas no interfieran con otros proyectos. 

Reemplaza path/to/venv con la ruta donde quieres almacenar tu entorno virtual.

```bash
# Crear el entrono virtual
python -m venv path/to/venv

# Activar el entorno virtual de Python
source path/to/venv/bin/activate
```


Ahora tendras el entorno virtual de Python activado, podras ver un distintivo en la consola, con el nombre del entorno virtual.

Y ahora solo quedara instalar **FastApi** y ejecutar el proyecto

```bash
# Instala FastAPI
pip install "fastapi[standard]"

# Esto solo se aplica para la version 1.0
# Ejecutar el proyecto FastApi en modo desarrollo
fastapi dev 
```

Para las versiones 1.1 y en adelante se ha integrado una CLI interna, para hacer mas sencillo la ejecucion del entorno y poder agregar en un futuro nuevas funcionalidades mas amplias y complejas.

Solo deberas ejecutar instalar la aplicación como un paquete y ya podras desarrollar, con el siguiente comando:

```bash
# Se instalara modulingg como un paquete
pip install -e .

# Para abrir abrir la aplicación
modulingg 
```

Con la aplicación lanzada solo quedara poner el comando para ejecutar FastApi:


```bash
# Lanzara FastApi junto a los modulos de la carpeta './modules'
run dev
```

Para conocer mas de los comandos de Modulingg puedes usar el comando ```help```

## Configuración ⚙️

### Modificar la configuración

Hay dos maneras de cambiar los parámetros de configuración en esta aplicación. Una opción es modificar el archivo `config.json` manualmente. Sin embargo, a partir de la versión **1.2**, se ha integrado un comando que facilita la modificación de los parámetros de configuración directamente desde la consola.

#### Uso del Comando `config`

Con el nuevo comando `config`, puedes consultar y actualizar la configuración sin tener que editar el archivo manualmente. A continuación se muestra cómo utilizarlo:

- **Consultar un parámetro**: Para obtener el valor de un parámetro, utiliza el comando `config [key] --get`.
- **Actualizar un parámetro**: Para modificar un valor, utiliza el comando `config [key] --set [value]`.

Ejemplo:

```bash
config module_launcher_name --get   # Muestra el valor actual del parámetro module_launcher_name .
```

```bash
config module_launcher_name --set init   # Cambia el volor de module_launcher_name
```

### Lista Blanca 📋

La configuración de la lista blanca permite seleccionar específicamente los módulos que se desean cargar en el sistema. Para habilitar esta opción, ajusta la variable:

- **`module_whitelist`**: 
  - **Tipo**: `boolean`
  - **Valor predeterminado**: `false`

Cuando la lista blanca está habilitada, puedes agregar los módulos permitidos en la variable:

- **`enabled_modules_whitelist`**: 
  - **Tipo**: `array`
  - **Valor predeterminado**: `[]`

### Módulos 📦

Configura aquí las opciones relativas a los módulos.

- **Nombre del fichero de arranque de cada módulo**:
  - **`module_launcher_name`**:
    - **Tipo**: `string`
    - **Valor predeterminado**: `main`

- **Nombre de la carpeta contenedora de los módulos**:
  - **`modules_folder_name`**:
    - **Tipo**: `string`
    - **Valor predeterminado**: `modules`

### Router

Configura aqui las opciones del router.

- **Habilita/Deshabilita que se cargue el router interno.**:
  - **`enable_internal_router`**:
    - **Tipo**: `boolean`
    - **Valor predeterminado**: `true`

## Módulos 📦

El núcleo del proyecto es la implementación de módulos. Cada uno debe seguir un estándar básico y coherente para garantizar su correcto funcionamiento dentro del sistema.

Todos los módulos desarrollados deben cumplir con el estándar **Modulingg**.

### Como crear un modulo ?

Crear un modulo es muy sencillo, **Modulingg** se encarga de crear una aplicacion FastAPI, y los modulos funcionan creando un router, con sus Endpoints, funcionalidad, ORM, lo que el desarrollador quiera. Y **Modulingg** carga el APIRouter de cada uno de los modulos en la aplicacion FastAPI principal, es necesario respetar el nombre de la variable **router**, ya que si el nombre difiere podria provocar problemas a la hora de cargar el módulo.

Cada uno de los modulos se almacena en una carperta con su fichero de arranque, el cual puedes configurar, y las funcionalidades. Aqui un ejemplo de un fichero de arranque basico.

```python
from fastapi import APIRouter
router = APIRouter() # Importante mantener el nombre de 'router'

@router.get('/api/v1')
async def read_root():
    return {"message": "Test Module v1"}
```
Fichero: example/main.py

Esto es una base, cada desarrollador puede agregar sus funcionalidades.

En el repositorio hay dos modulos de ejemplos.

### Manifest

Este tipo de archivo es útil para describir las características y propiedades básicas del módulo, permitiendo que otros desarrolladores o sistemas lo comprendan e interactúen con él. A continuación, detallo cada uno de los campos:

```json
{
    "name": "My Module Name",
    "short_name": "my-module-name",
    "description": "A simple module for demonstrating Modulingg usage.",
    "author": "Author Name",
    "version": "1.0.0"
}
```

---

Este proyecto ofrece una estructura flexible y modular que permite a los desarrolladores añadir fácilmente funcionalidades específicas al backend sin comprometer el orden ni la escalabilidad.
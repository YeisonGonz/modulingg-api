# Modulatingg API | 📦

## ¿En qué se basa este proyecto?

Modulatingg API es una base sólida diseñada para facilitar la creación de un backend escalable y organizado utilizando Python y FastAPI 🐍. La idea es proporcionar un entorno plug-and-play en el que los desarrolladores puedan construir módulos independientes con la estructura adecuada. Una vez configurados, solo es necesario añadir estos módulos a la carpeta correspondiente para que funcionen de inmediato.

## Configuración ⚙️

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

## Módulos 📦

El núcleo del proyecto es la implementación de módulos. Cada uno debe seguir un estándar básico y coherente para garantizar su correcto funcionamiento dentro del sistema.

Todos los módulos desarrollados deben cumplir con el estándar **Modulingg**.

---

Este proyecto ofrece una estructura flexible y modular que permite a los desarrolladores añadir fácilmente funcionalidades específicas al backend sin comprometer el orden ni la escalabilidad.
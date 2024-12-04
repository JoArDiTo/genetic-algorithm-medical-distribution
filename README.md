# SISTEMA EXPERTO: RECOMENDACIÓN DE PELÍCULAS

## Indice:
- [Descripción](#descripción)
- [Instalación](#instalación)
- [Consideración](#consideración)

## Descripción:

Este proyecto implementa un algoritmo genético para calcular la ruta óptima basada en varios factores como prioridad, accesibilidad, tiempo de espera y costo, además de las distancias entre los departamentos del norte del Perú. El objetivo es encontrar la mejor ruta que minimice el costo total y el tiempo de espera, mientras se maximiza la accesibilidad y se respeta la prioridad de las rutas. Utiliza técnicas avanzadas de algoritmos genéticos para explorar y explotar el espacio de soluciones posibles, proporcionando una solución eficiente y efectiva para problemas complejos de optimización de rutas.


## Instalación

Para instalar y ejecutar el proyecto, sigue los siguientes pasos:

1. **Clonar el repositorio:**
    ```bash
    git@github.com:JoArDiTo/genetic-algorithm-medical-distribution.git
    ```
2. **Dirígete a la carpeta raíz del proyecto**
    ```bash
    cd genetic-algorithm-medical-distribution  
    ```

3. **Crear y activar un entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

4. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Ejecutar el programa:**
    ```bash
    flask run
    ```

Esto iniciará el servidor Flask.

## Consideración

Para utilizar este servidor en una aplicación web, es importante que se define los permisos CORS, es por ello que se necesita de un entorno virtual (tal y como se presenta en el archivo .env.local)
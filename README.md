# Data Explorer Dashboard with Streamlit

## Descripción

Este proyecto es una **aplicación web interactiva** construida con **Streamlit**, que permite a los usuarios cargar un archivo CSV y explorar los datos de manera visual. Los usuarios pueden:

- Subir sus propios archivos CSV.
- Ver una vista previa de los datos cargados.
- Ver estadísticas descriptivas de los datos.
- Crear gráficos interactivos como histogramas y gráficos de dispersión.
- Descargar los datos procesados en formato CSV.

El objetivo es proporcionar una herramienta rápida y fácil para explorar conjuntos de datos sin necesidad de escribir código.

## Funcionalidades

- **Cargar un archivo CSV**: Permite al usuario cargar cualquier archivo CSV y visualizar sus primeros registros.
- **Estadísticas descriptivas**: Muestra un resumen de las estadísticas clave del conjunto de datos.
- **Visualización**: Permite la creación de gráficos como histogramas y gráficos de dispersión de las columnas numéricas.
- **Exportación de datos**: Los usuarios pueden descargar los datos procesados.

## Requisitos

Este proyecto depende de las siguientes librerías de Python:

- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`

## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/TU_USUARIO/streamlit-dashboard.git
    cd streamlit-dashboard
    ```

2. **Instala los requerimientos**:

    Si usas **pip**:

    ```bash
    pip install -r requirements.txt
    ```

    O si prefieres usar **conda**, puedes crear un entorno con el archivo `environment.yml`:

    ```bash
    conda env create -f environment.yml
    conda activate streamlit-dashboard
    ```

3. **Ejecuta la aplicación**:

    ```bash
    streamlit run streamlit_app.py
    ```

    La aplicación debería abrir automáticamente en tu navegador en [http://localhost:8501](http://localhost:8501).

## Despliegue en Streamlit Cloud

1. Crea una cuenta o inicia sesión en [Streamlit Cloud](https://streamlit.io/cloud).
2. Conecta tu cuenta de **GitHub**.
3. Haz clic en **New app** y selecciona tu repositorio.
4. Asegúrate de que el archivo de la app sea `streamlit_app.py`.
5. Haz clic en **Deploy** para ver la app en línea.

### Link al demo en Streamlit: [tuapp.streamlit.app](https://tuapp.streamlit.app)

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto o agregar nuevas funcionalidades, por favor abre un **issue** o haz un **pull request**.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

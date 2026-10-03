# Proyecto 01 - Inteligencia de Negocios - Equipo 1

## Tema 1: Cadena de supermercados y retail minorista

## Integrantes del equipo

- Fabián De Jesús Granados Rivera
- Daniel Avendaño Ulloa
- Ariel Esteban Rodríguez Trejos
- Melanie Parra Valverde
- Angélica De Jesús Granados Rivera

## Descripción del problema

La organización es una cadena de supermercados / retail minorista con varias sucursales. Necesita entender su desempeño comercial (ventas, unidades, margen), el comportamiento de compra de sus clientes (ticket promedio, frecuencia, canal, método de pago), el efecto de las promociones sobre las ventas, y la gestión de inventario (rotación, quiebres de existencias / bajo inventario).

## Arquitectura de la solución

Fuente transaccional (OLTP) → Proceso ETL → Modelo dimensional (bodega de datos) → Capa analítica / dashboard.

## Herramientas utilizadas

- Base de datos transaccional: PostgreSQL
- Proceso ETL: Pentaho Data Integration (Kettle) - Community Edition
- Modelo dimensional: PostgreSQL (esquema `supermercado_dw`)
- Capa analítica: Power BI Desktop
- Control de versiones: GitHub

## Estructura del repositorio

Proyecto1BI-Equipo1:

- README.md
- docs/
- sql/
- data/
- etl/
- dashboard/

## Contenido de cada sección del repositorio

- `docs`: Informe del proyecto y archivo de presentación.
- `sql`: Scripts del esquema transaccional, datos, modelo dimensional y validaciones.
- `data`: Script utilizado para la generación de datos sintéticos.
- `etl`: Transformaciones desarrolladas en Pentaho Data Integration.
- `dashboard`: Solución analítica desarrollada en Power BI.

## Instrucciones de ejecución

### 1. Crear la base de datos

Crear una base de datos en PostgreSQL para el proyecto.

### 2. Crear y cargar el modelo transaccional

Ejecutar los siguientes scripts en este orden:

1. `sql/supermercado.sql`
2. `sql/datos_supermercado.sql`

Estos scripts crean el esquema transaccional `supermercado` y cargan los datos utilizados en el proyecto.

### 3. Crear el modelo dimensional

Ejecutar:

`sql/modelo_dimensional.sql`

Este script crea el esquema `supermercado_dw`, sus dimensiones y las tablas de hechos.

### 4. Configurar Pentaho Data Integration

Abrir las transformaciones ubicadas en la carpeta `etl/` y configurar la conexión PostgreSQL con la base de datos creada.

### 5. Ejecutar las dimensiones

Ejecutar las transformaciones de dimensiones antes de las tablas de hechos:

- `etl_dim_fecha.ktr`
- `etl_dim_producto.ktr`
- `etl_dim_sucursal.ktr`
- `etl_dim_cliente.ktr`
- `etl_dim_canal.ktr`
- `etl_dim_metodo_pago.ktr`
- `etl_dim_promocion.ktr`

### 6. Ejecutar las tablas de hechos

Después de cargar las dimensiones, ejecutar:

- `etl_fact_ventas.ktr`
- `etl_fact_inventario.ktr`

### 7. Validar el modelo dimensional

Una vez cargadas las dimensiones y tablas de hechos, ejecutar: 

`sql/validaciones_modelo_dimensional.sql`

Este script permite comprobar la cantidad de registros cargados, la granularidad de las tablas de hechos y la consistencia de
algunas reglas del modelo dimensional. 

### 8. Capa analítica

Pendiente de implementación en Power BI Desktop.

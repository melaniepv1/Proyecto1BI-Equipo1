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
- Proceso ETL: Pentaho Data Integration (Kettle) — Community Edition
- Modelo dimensional: PostgreSQL (esquema dw_retail)
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
- docs: Informe del proyecto y archivo de presentación
- sql: Scripts de esquema transaccional y modelo dimensional
- data: Scripts de generación de datos sintéticos
- etl: Proceso ETL
- dashboard: Solución analítica

## Instrucciones de ejecución
PENDIENTE

-- ===============================================================
-- VALIDACIONES DEL MODELO DIMENSIONAL
-- ===============================================================

-- 1. Validar cantidad de registros cargados en cada dimensión
SELECT 'dim_fecha' AS tabla, COUNT(*) AS registros
FROM supermercado_dw.dim_fecha
UNION ALL
SELECT 'dim_producto', COUNT(*)
FROM supermercado_dw.dim_producto
UNION ALL
SELECT 'dim_sucursal', COUNT(*)
FROM supermercado_dw.dim_sucursal
UNION ALL
SELECT 'dim_cliente', COUNT(*)
FROM supermercado_dw.dim_cliente
UNION ALL
SELECT 'dim_canal', COUNT(*)
FROM supermercado_dw.dim_canal
UNION ALL
SELECT 'dim_metodo_pago', COUNT(*)
FROM supermercado_dw.dim_metodo_pago
UNION ALL
SELECT 'dim_promocion', COUNT(*)
FROM supermercado_dw.dim_promocion;


-- 2. Validar cantidad de registros en las tablas de hechos
SELECT 'fact_ventas' AS tabla, COUNT(*) AS registros
FROM supermercado_dw.fact_ventas
UNION ALL
SELECT 'fact_inventario', COUNT(*)
FROM supermercado_dw.fact_inventario;


-- 3. Verificar rango de fechas de la dimensión fecha
SELECT
    MIN(fecha) AS fecha_inicial,
    MAX(fecha) AS fecha_final,
    COUNT(*) AS cantidad_fechas
FROM supermercado_dw.dim_fecha;


-- 4. Verificar que las llaves naturales no estén duplicadas

SELECT id_producto_origen, COUNT(*)
FROM supermercado_dw.dim_producto
GROUP BY id_producto_origen
HAVING COUNT(*) > 1;

SELECT id_sucursal_origen, COUNT(*)
FROM supermercado_dw.dim_sucursal
GROUP BY id_sucursal_origen
HAVING COUNT(*) > 1;

SELECT id_cliente_origen, COUNT(*)
FROM supermercado_dw.dim_cliente
GROUP BY id_cliente_origen
HAVING COUNT(*) > 1;


-- 5. Validar granularidad de fact_ventas
-- No debe existir más de una fila con el mismo id_venta_detalle
SELECT
    id_venta_detalle,
    COUNT(*)
FROM supermercado_dw.fact_ventas
GROUP BY id_venta_detalle
HAVING COUNT(*) > 1;


-- 6. Validar granularidad de fact_inventario
-- No debe existir más de una fila para la misma fecha,
-- producto y sucursal
SELECT
    sk_fecha,
    sk_producto,
    sk_sucursal,
    COUNT(*)
FROM supermercado_dw.fact_inventario
GROUP BY
    sk_fecha,
    sk_producto,
    sk_sucursal
HAVING COUNT(*) > 1;


-- 7. Validar fila especial "Sin promoción"
SELECT *
FROM supermercado_dw.dim_promocion
WHERE sk_promocion = 0;


-- 8. Validar lógica del indicador de quiebre
SELECT COUNT(*) AS flags_quiebre_incorrectos
FROM supermercado_dw.fact_inventario
WHERE flag_quiebre <>
    CASE
        WHEN stock_actual = 0 THEN 1
        ELSE 0
    END;


-- 9. Validar lógica del indicador de bajo inventario
SELECT COUNT(*) AS flags_bajo_inventario_incorrectos
FROM supermercado_dw.fact_inventario
WHERE flag_bajo_inventario <>
    CASE
        WHEN stock_actual > 0
         AND stock_actual < stock_minimo THEN 1
        ELSE 0
    END;


-- 10. Validar cálculo de ganancia bruta
SELECT COUNT(*) AS ganancias_incorrectas
FROM supermercado_dw.fact_ventas
WHERE ganancia_bruta <> (monto_venta - costo_total);


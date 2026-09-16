CREATE SCHEMA IF NOT EXISTS supermercado;

CREATE TABLE supermercado.sucursal (
    id_sucursal    SERIAL PRIMARY KEY,
    nombre         VARCHAR(100) NOT NULL,
    ciudad         VARCHAR(100),
    region         VARCHAR(100),
    tipo_sucursal  VARCHAR(50)
);

CREATE TABLE supermercado.producto (
    id_producto     SERIAL PRIMARY KEY,
    nombre          VARCHAR(150) NOT NULL,
    categoria       VARCHAR(100),
    subcategoria    VARCHAR(100),
    marca           VARCHAR(100),
    costo_unitario  NUMERIC(10,2) NOT NULL CHECK (costo_unitario >= 0),
    precio_lista    NUMERIC(10,2) NOT NULL CHECK (precio_lista >= 0)
);

CREATE TABLE supermercado.cliente (
    id_cliente      SERIAL PRIMARY KEY,
    nombre          VARCHAR(150) NOT NULL,
    segmento        VARCHAR(50),
    fecha_registro  DATE NOT NULL,
    ciudad          VARCHAR(100)
);

CREATE TABLE supermercado.canal_venta (
    id_canal  SERIAL PRIMARY KEY,
    nombre    VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE supermercado.metodo_pago (
    id_metodo_pago  SERIAL PRIMARY KEY,
    nombre          VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE supermercado.promocion (
    id_promocion          SERIAL PRIMARY KEY,
    nombre                VARCHAR(150) NOT NULL,
    tipo_descuento        VARCHAR(50) NOT NULL,
    fecha_inicio          DATE NOT NULL,
    fecha_fin             DATE NOT NULL,
    alcance               VARCHAR(20) NOT NULL CHECK (alcance IN ('Producto','Categoria')),
    id_producto_alcance   INT REFERENCES supermercado.producto(id_producto),
    categoria_alcance     VARCHAR(100),
    CHECK (fecha_fin >= fecha_inicio),
    CHECK (
        (alcance = 'Producto' AND id_producto_alcance IS NOT NULL AND categoria_alcance IS NULL)
        OR
        (alcance = 'Categoria' AND categoria_alcance IS NOT NULL AND id_producto_alcance IS NULL)
    )
);

CREATE TABLE supermercado.venta (
    id_venta        SERIAL PRIMARY KEY,
    fecha           TIMESTAMP NOT NULL,
    id_sucursal     INT NOT NULL REFERENCES supermercado.sucursal(id_sucursal),
    id_cliente      INT NOT NULL REFERENCES supermercado.cliente(id_cliente),
    id_canal        INT NOT NULL REFERENCES supermercado.canal_venta(id_canal),
    id_metodo_pago  INT NOT NULL REFERENCES supermercado.metodo_pago(id_metodo_pago),
    total           NUMERIC(12,2) NOT NULL CHECK (total >= 0)
);

CREATE TABLE supermercado.detalle_venta (
    id_venta_detalle  SERIAL PRIMARY KEY,
    id_venta          INT NOT NULL REFERENCES supermercado.venta(id_venta),
    id_producto       INT NOT NULL REFERENCES supermercado.producto(id_producto),
    cantidad          INT NOT NULL CHECK (cantidad > 0),
    precio_unitario   NUMERIC(10,2) NOT NULL CHECK (precio_unitario >= 0),
    descuento         NUMERIC(10,2) NOT NULL DEFAULT 0 CHECK (descuento >= 0),
    id_promocion      INT REFERENCES supermercado.promocion(id_promocion)
);

CREATE TABLE supermercado.movimiento_inventario (
    id_movimiento    SERIAL PRIMARY KEY,
    fecha            TIMESTAMP NOT NULL,
    id_sucursal      INT NOT NULL REFERENCES supermercado.sucursal(id_sucursal),
    id_producto      INT NOT NULL REFERENCES supermercado.producto(id_producto),
    tipo_movimiento  VARCHAR(20) NOT NULL CHECK (tipo_movimiento IN ('Entrada','Salida','Ajuste')),
    cantidad         INT NOT NULL CHECK (cantidad > 0)
);

CREATE TABLE supermercado.inventario (
    id_inventario  SERIAL PRIMARY KEY,
    fecha          DATE NOT NULL,
    id_sucursal    INT NOT NULL REFERENCES supermercado.sucursal(id_sucursal),
    id_producto    INT NOT NULL REFERENCES supermercado.producto(id_producto),
    stock_actual   INT NOT NULL CHECK (stock_actual >= 0),
    stock_minimo   INT NOT NULL CHECK (stock_minimo >= 0),
    UNIQUE (fecha, id_sucursal, id_producto)
);

CREATE INDEX idx_venta_fecha           ON supermercado.venta(fecha);
CREATE INDEX idx_venta_sucursal        ON supermercado.venta(id_sucursal);
CREATE INDEX idx_detalle_venta_producto ON supermercado.detalle_venta(id_producto);
CREATE INDEX idx_mov_inv_producto      ON supermercado.movimiento_inventario(id_producto, id_sucursal);
CREATE INDEX idx_inventario_fecha      ON supermercado.inventario(fecha);

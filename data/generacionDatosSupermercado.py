import random
from datetime import date, timedelta

random.seed(42)

def q(v):
    if v is None:
        return "NULL"
    if isinstance(v, (int, float)):
        return f"{v:.2f}" if isinstance(v, float) else str(v)
    return "'" + str(v).replace("'", "''") + "'"

def insert(tabla, cols, filas, lote=100):
    out = []
    for i in range(0, len(filas), lote):
        vals = ",\n".join("(" + ", ".join(q(x) for x in f) + ")" for f in filas[i:i+lote])
        out.append(f"INSERT INTO supermercado.{tabla} ({', '.join(cols)}) VALUES\n{vals};\n")
    return "\n".join(out)

# 1. SUCURSAL
sucursales = [
    ("Hipermercado Escazú", "Escazú", "San José", "Hipermercado"),
    ("Supermercado Heredia Centro", "Heredia", "Heredia", "Supermercado"),
    ("Supermercado Cartago", "Cartago", "Cartago", "Supermercado"),
    ("Express Alajuela", "Alajuela", "Alajuela", "Express"),
    ("Express Liberia", "Liberia", "Guanacaste", "Express"),
]

# 2. PRODUCTO
P = [
 ("Leche entera 1L","Lácteos","Leche","Dos Pinos",1050),
 ("Leche semidescremada 1L","Lácteos","Leche","Dos Pinos",1050),
 ("Leche deslactosada 1L","Lácteos","Leche","Dos Pinos",1150),
 ("Leche entera 1L Coronado","Lácteos","Leche","Coronado",990),
 ("Yogurt natural 1L","Lácteos","Yogurt","Dos Pinos",1850),
 ("Yogurt de fresa 200g","Lácteos","Yogurt","Dos Pinos",650),
 ("Queso Turrialba 500g","Lácteos","Quesos","Dos Pinos",3200),
 ("Queso mozzarella rallado 200g","Lácteos","Quesos","Dos Pinos",2350),
 ("Natilla 500g","Lácteos","Cremas","Dos Pinos",1450),
 ("Mantequilla con sal 250g","Lácteos","Mantequillas","Dos Pinos",1900),
 ("Queso crema 250g","Lácteos","Quesos","Philadelphia",2100),
 ("Leche condensada 397g","Lácteos","Leches especiales","Nestlé",1300),
 ("Bebida de almendra 1L","Lácteos","Bebidas vegetales","Silk",2600),
 ("Queso palmito 400g","Lácteos","Quesos","Monteverde",2900),
 ("Papas tostadas clásicas 150g","Snacks","Papas","Tío Pelón",1450),
 ("Papas Pringles original 124g","Snacks","Papas","Pringles",2200),
 ("Tortillitas de maíz 200g","Snacks","Tortillas","Doritos",1650),
 ("Plátanos tostados 120g","Snacks","Plataninas","Tío Pelón",950),
 ("Maní salado 200g","Snacks","Frutos secos","Tío Pelón",1200),
 ("Galletas de chocolate 432g","Snacks","Galletas","Oreo",1800),
 ("Galletas María 400g","Snacks","Galletas","Pozuelo",1100),
 ("Galletas rellenas de vainilla 6 un","Snacks","Galletas","Pozuelo",850),
 ("Chocolate con leche 100g","Snacks","Chocolates","Nestlé",1250),
 ("Barra de granola 6 un","Snacks","Barras","Quaker",1950),
 ("Palomitas para microondas 3 un","Snacks","Palomitas","Act II",1350),
 ("Gomitas surtidas 100g","Snacks","Confitería","Haribo",1300),
 ("Coca-Cola 2.5L","Bebidas","Gaseosas","Coca-Cola",1750),
 ("Coca-Cola sin azúcar 2.5L","Bebidas","Gaseosas","Coca-Cola",1750),
 ("Fanta naranja 2L","Bebidas","Gaseosas","Fanta",1350),
 ("Agua purificada 600ml","Bebidas","Agua","Cristal",550),
 ("Agua con gas 600ml","Bebidas","Agua","Cristal",650),
 ("Jugo de naranja 1L","Bebidas","Jugos","Del Valle",1400),
 ("Bebida de frutas 1.5L","Bebidas","Jugos","Tropical",1200),
 ("Bebida energética 473ml","Bebidas","Energéticas","Monster",1500),
 ("Bebida hidratante 750ml","Bebidas","Deportivas","Gatorade",1100),
 ("Cerveza lata 350ml","Bebidas","Cervezas","Imperial",900),
 ("Cerveza Pilsen lata 350ml","Bebidas","Cervezas","Pilsen",900),
 ("Té verde 500ml","Bebidas","Tés","Lipton",850),
 ("Agua purificada 2.5L","Bebidas","Agua","Cristal",1100),
 ("Jugo de manzana 1L","Bebidas","Jugos","Del Valle",1400),
 ("Detergente en polvo 1kg","Limpieza","Detergentes","Irex",2600),
 ("Detergente líquido 2L","Limpieza","Detergentes","Ariel",5200),
 ("Suavizante de ropa 1L","Limpieza","Suavizantes","Suavitel",1900),
 ("Cloro 1L","Limpieza","Desinfectantes","Clorox",850),
 ("Desinfectante multiusos 1L","Limpieza","Desinfectantes","Poett",1300),
 ("Lavaplatos en crema 500g","Limpieza","Lavaplatos","Axión",1350),
 ("Papel higiénico 12 rollos","Limpieza","Papel","Nevax",4300),
 ("Toallas de cocina 3 rollos","Limpieza","Papel","Scott",2400),
 ("Bolsas para basura 10 un","Limpieza","Bolsas","Glad",1600),
 ("Limpiavidrios 500ml","Limpieza","Limpiadores","Windex",1750),
 ("Esponjas multiuso 3 un","Limpieza","Accesorios","Scotch-Brite",1100),
 ("Jabón en barra para ropa 400g","Limpieza","Jabones","Irex",700),
 ("Shampoo 400ml","Cuidado personal","Cabello","Pantene",3400),
 ("Acondicionador 400ml","Cuidado personal","Cabello","Pantene",3400),
 ("Jabón de tocador 3 un","Cuidado personal","Jabones","Protex",1700),
 ("Pasta dental 100ml","Cuidado personal","Higiene bucal","Colgate",1250),
 ("Cepillo dental","Cuidado personal","Higiene bucal","Colgate",1100),
 ("Desodorante en barra 50g","Cuidado personal","Desodorantes","Rexona",2300),
 ("Toallas sanitarias 10 un","Cuidado personal","Higiene femenina","Kotex",1650),
 ("Pañales etapa 3 30 un","Cuidado personal","Bebé","Huggies",8900),
 ("Crema corporal 400ml","Cuidado personal","Cuidado de la piel","Nivea",3800),
 ("Bloqueador solar SPF50 120ml","Cuidado personal","Cuidado de la piel","Banana Boat",6900),
 ("Enjuague bucal 500ml","Cuidado personal","Higiene bucal","Listerine",3100),
 ("Máquinas de afeitar 4 un","Cuidado personal","Afeitado","Gillette",3600),
 ("Helado de vainilla 1L","Congelados","Helados","Dos Pinos",2600),
 ("Helado de chocolate 1L","Congelados","Helados","Dos Pinos",2600),
 ("Pizza congelada de pepperoni","Congelados","Pizzas","DiGiorno",4800),
 ("Nuggets de pollo 500g","Congelados","Pollo","Pipasa",3200),
 ("Papas a la francesa 1kg","Congelados","Vegetales congelados","McCain",2900),
 ("Vegetales mixtos 500g","Congelados","Vegetales congelados","Sabemas",1500),
 ("Filete de tilapia 500g","Congelados","Mariscos","Pescanova",3900),
 ("Empanadas de carne 6 un","Congelados","Listos para hornear","Sabemas",2700),
 ("Camarones precocidos 400g","Congelados","Mariscos","Pescanova",5400),
 ("Paletas de fruta 6 un","Congelados","Helados","Dos Pinos",2200),
 ("Pan cuadrado blanco 500g","Panadería","Pan de molde","Bimbo",1500),
 ("Pan integral 500g","Panadería","Pan de molde","Bimbo",1750),
 ("Pan baguette","Panadería","Pan artesanal","Musmanni",900),
 ("Pan para hamburguesa 8 un","Panadería","Pan de molde","Bimbo",1550),
 ("Tortillas de harina 10 un","Panadería","Tortillas","Bimbo",1400),
 ("Tostadas 180g","Panadería","Tostadas","Bimbo",1200),
 ("Queque de vainilla","Panadería","Repostería","Musmanni",2100),
 ("Cangrejitos 4 un","Panadería","Repostería","Musmanni",1600),
 ("Pan dulce 6 un","Panadería","Pan dulce","Musmanni",1200),
 ("Tortillas de maíz 10 un","Panadería","Tortillas","Del Maíz",800),
 ("Arroz 99% grano entero 1.8kg","Abarrotes","Granos","Tío Pelón",2250),
 ("Arroz 80% grano entero 2kg","Abarrotes","Granos","Luisiana",1950),
 ("Frijoles negros 800g","Abarrotes","Granos","Tío Pelón",1400),
 ("Frijoles rojos 800g","Abarrotes","Granos","Tío Pelón",1450),
 ("Azúcar blanca 2kg","Abarrotes","Azúcar","Doña María",1600),
 ("Aceite vegetal 1L","Abarrotes","Aceites","Clover",2100),
 ("Atún en aceite 140g","Abarrotes","Enlatados","Sardimar",1150),
 ("Sardinas en salsa de tomate 155g","Abarrotes","Enlatados","Sardimar",850),
 ("Café molido 500g","Abarrotes","Café","Café Rey",3300),
 ("Café instantáneo 100g","Abarrotes","Café","Nescafé",2800),
 ("Salsa Lizano 700ml","Abarrotes","Salsas","Lizano",1950),
 ("Pasta spaghetti 400g","Abarrotes","Pastas","Roma",700),
 ("Salsa de tomate 400g","Abarrotes","Salsas","Kerns",900),
 ("Harina de trigo 1kg","Abarrotes","Harinas","Selecta",950),
 ("Sal refinada 1kg","Abarrotes","Condimentos","Sal Sol",450),
 ("Avena en hojuelas 400g","Abarrotes","Cereales","Quaker",1250),
]
assert len(P) == 100
margen = {"Lácteos":(.18,.26),"Snacks":(.30,.42),"Bebidas":(.25,.35),"Limpieza":(.24,.34),
          "Cuidado personal":(.30,.40),"Congelados":(.22,.32),"Panadería":(.28,.40),"Abarrotes":(.12,.22)}
productos = []
for n,c,s,m,pr in P:
    lo,hi = margen[c]
    costo = round(pr*(1-random.uniform(lo,hi)),2)
    productos.append((n,c,s,m,costo,float(pr)))
pid = {p[0]: i+1 for i,p in enumerate(productos)}

# 3. CLIENTE
nombres = ["María","José","Ana","Luis","Carmen","Carlos","Laura","Jorge","Sofía","Daniel","Andrea","Andrés",
 "Valeria","Diego","Gabriela","Fernando","Natalia","Esteban","Paola","Mauricio","Karla","Alejandro","Mónica",
 "Pablo","Adriana","Ricardo","Daniela","Kevin","Fabiola","Josué","Melissa","Randall","Tatiana","Óscar","Silvia",
 "Marco","Rebeca","Sebastián","Priscilla","Allan","Jimena","Emilio","Wendy","Rodrigo","Lucía","Francisco",
 "Hellen","Mario","Camila","Gustavo","Verónica","Rafael","Yorleny","Iván","Mariela","Johan","Ariana","Víctor"]
apellidos = ["Rodríguez","Jiménez","Mora","Vargas","Rojas","Araya","Sánchez","Hernández","Solano","Castro",
 "Ramírez","Chaves","Alvarado","Quesada","Salazar","Fernández","Brenes","Calderón","Madrigal","Arias",
 "Segura","Campos","Villalobos","Zúñiga","Méndez","Soto","Gómez","Cordero","Umaña","Porras","Valverde",
 "Trejos","Granados","Alfaro","Murillo","Ulate","Cascante","Picado","Obando","Montero"]
ciudades = ["Escazú","Heredia","Cartago","Alajuela","Liberia","San José","Santa Ana","Curridabat",
            "Santo Domingo","Tres Ríos","Grecia","Nicoya"]
pesos_ciudad = [16,14,13,13,10,10,5,5,4,4,3,3]

def fecha_rand(a, b):
    return a + timedelta(days=random.randint(0, (b - a).days))

clientes = []
for _ in range(500):
    seg = random.choices(["Frecuente","Ocasional","Nuevo"], weights=[25,45,30])[0]
    if seg == "Frecuente":
        fr = fecha_rand(date(2019,1,1), date(2023,6,30))
    elif seg == "Ocasional":
        fr = fecha_rand(date(2020,1,1), date(2024,9,30))
    else:
        fr = fecha_rand(date(2024,10,1), date(2025,6,30))
    nom = f"{random.choice(nombres)} {random.choice(apellidos)} {random.choice(apellidos)}"
    ciu = random.choices(ciudades, weights=pesos_ciudad)[0]
    clientes.append((nom, seg, fr.isoformat(), ciu))

# 4-5
canales = [("Tienda física",),("En línea",),("App",)]
metodos = [("Efectivo",),("Tarjeta débito",),("Tarjeta crédito",),("Transferencia",)]

# 6. PROMOCION
PR = [
 ("Festival de Lácteos","Porcentaje","2024-10-07","2024-10-20","Categoria",None,"Lácteos"),
 ("2x1 Galletas Oreo","2x1","2024-10-14","2024-10-27","Producto","Galletas de chocolate 432g",None),
 ("Black Friday Bebidas","Porcentaje","2024-11-18","2024-12-01","Categoria",None,"Bebidas"),
 ("Navidad en Panadería","Porcentaje","2024-12-02","2024-12-29","Categoria",None,"Panadería"),
 ("Descuento Café Rey","Monto fijo","2024-12-09","2024-12-22","Producto","Café molido 500g",None),
 ("Oferta Yogurt de fresa","Porcentaje","2025-01-06","2025-01-19","Producto","Yogurt de fresa 200g",None),
 ("Regreso a clases Snacks","Porcentaje","2025-01-20","2025-02-16","Categoria",None,"Snacks"),
 ("2x1 Detergente Irex","2x1","2025-02-03","2025-02-09","Producto","Detergente en polvo 1kg",None),
 ("Mes de la limpieza","Monto fijo","2025-03-03","2025-03-30","Categoria",None,"Limpieza"),
 ("Semana Santa Abarrotes","Porcentaje","2025-04-07","2025-04-20","Categoria",None,"Abarrotes"),
 ("Oferta Atún Sardimar","Monto fijo","2025-04-07","2025-04-27","Producto","Atún en aceite 140g",None),
 ("2x1 Helado de vainilla","2x1","2025-05-05","2025-05-18","Producto","Helado de vainilla 1L",None),
 ("Temporada de Congelados","Porcentaje","2025-05-12","2025-06-22","Categoria",None,"Congelados"),
 ("Descuento Aceite Clover","Monto fijo","2025-06-02","2025-06-15","Producto","Aceite vegetal 1L",None),
 ("Vacaciones de medio año Bebidas","Porcentaje","2025-06-30","2025-07-13","Categoria",None,"Bebidas"),
 ("2x1 Coca-Cola 2.5L","2x1","2025-07-07","2025-07-20","Producto","Coca-Cola 2.5L",None),
 ("Día de la Madre Cuidado personal","Porcentaje","2025-08-04","2025-08-17","Categoria",None,"Cuidado personal"),
 ("Descuento Leche Dos Pinos","Monto fijo","2025-08-11","2025-08-24","Producto","Leche entera 1L",None),
 ("Mes Patrio Abarrotes","Porcentaje","2025-09-01","2025-09-14","Categoria",None,"Abarrotes"),
 ("2x1 Pan cuadrado Bimbo","2x1","2025-09-08","2025-09-21","Producto","Pan cuadrado blanco 500g",None),
]
promociones = []
for n,t,i,f,a,p,c in PR:
    d = (date.fromisoformat(f) - date.fromisoformat(i)).days + 1
    assert 7 <= d <= 42, n
    promociones.append((n,t,i,f,a,pid[p] if p else None,c))

FECHA_INICIO = date(2024, 10, 1)
FECHA_FIN = date(2025, 9, 30)
N_VENTAS = 6000

producto_by_id = {i + 1: p for i, p in enumerate(productos)}

clientes_info = [(i + 1, date.fromisoformat(c[2]), c[1]) for i, c in enumerate(clientes)]
peso_segmento = {"Frecuente": 3, "Ocasional": 2, "Nuevo": 1}

promos_parsed = [
    (i + 1, tipo, date.fromisoformat(ini), date.fromisoformat(fin), alcance, idprod, cat)
    for i, (nombre, tipo, ini, fin, alcance, idprod, cat) in enumerate(promociones)
]

def cliente_valido(fecha_venta):
    validos = [c for c in clientes_info if c[1] <= fecha_venta]
    ids = [c[0] for c in validos]
    pesos = [peso_segmento[c[2]] for c in validos]
    return random.choices(ids, weights=pesos)[0]

def promo_aplicable(producto_id, categoria, fecha_venta):
    return [
        pr for pr in promos_parsed
        if pr[2] <= fecha_venta <= pr[3]
        and ((pr[4] == "Producto" and pr[5] == producto_id) or (pr[4] == "Categoria" and pr[6] == categoria))
    ]

# 7-8. VENTA Y DETALLE_VENTA
ventas = []
detalles = []
movimientos = []
inventarios = []

for _ in range(N_VENTAS):
    fecha_venta = fecha_rand(FECHA_INICIO, FECHA_FIN)
    id_sucursal = random.randint(1, len(sucursales))
    id_cliente = cliente_valido(fecha_venta)
    id_canal = random.randint(1, len(canales))
    id_metodo = random.randint(1, len(metodos))

    n_lineas = random.randint(1, 5)
    total_venta = 0.0
    lineas_venta = []
    for _ in range(n_lineas):
        id_producto = random.randint(1, len(productos))
        nombre_p, categoria_p, _, _, _, precio_lista_p = producto_by_id[id_producto]
        cantidad = random.randint(1, 4)
        precio_unitario = precio_lista_p
        descuento = 0.0
        id_promocion = None

        elegibles = promo_aplicable(id_producto, categoria_p, fecha_venta)
        if elegibles and random.random() < 0.6:
            id_promocion, tipo_promo = random.choice([(p[0], p[1]) for p in elegibles])
            if tipo_promo == "2x1":
                cantidad = 2
                descuento = round(precio_unitario, 2)
            elif tipo_promo == "Porcentaje":
                descuento = round(precio_unitario * cantidad * random.uniform(0.10, 0.30), 2)
            else:
                monto = random.choice([200, 300, 400, 500])
                descuento = round(min(monto, precio_unitario * cantidad * 0.9), 2)

        subtotal = round(precio_unitario * cantidad - descuento, 2)
        total_venta += subtotal
        lineas_venta.append((id_producto, cantidad, precio_unitario, descuento, id_promocion))

    id_venta = len(ventas) + 1
    ventas.append((fecha_venta.isoformat(), id_sucursal, id_cliente, id_canal, id_metodo, round(total_venta, 2)))
    for (id_producto, cantidad, precio_unitario, descuento, id_promocion) in lineas_venta:
        detalles.append((id_venta, id_producto, cantidad, precio_unitario, descuento, id_promocion))

# 9. MOVIMIENTO_INVENTARIO
for _ in range(10000):
    fecha_mov = fecha_rand(FECHA_INICIO, FECHA_FIN)
    tipo_mov = random.choices(["Entrada", "Salida", "Ajuste"], weights=[0.4, 0.5, 0.1])[0]
    movimientos.append((
        fecha_mov.isoformat(), random.randint(1, len(sucursales)), random.randint(1, len(productos)),
        tipo_mov, random.randint(1, 200)
    ))

# 10. INVENTARIO
fecha_actual = FECHA_INICIO
while fecha_actual <= FECHA_FIN:
    for id_suc in range(1, len(sucursales) + 1):
        for id_prod in range(1, len(productos) + 1):
            stock_min = random.randint(5, 30)
            stock_act = max(0, stock_min + random.randint(-10, 100))
            inventarios.append((fecha_actual.isoformat(), id_suc, id_prod, stock_act, stock_min))
    fecha_actual += timedelta(days=7)

sql = [
 insert("sucursal", ["nombre","ciudad","region","tipo_sucursal"], sucursales),
 insert("producto", ["nombre","categoria","subcategoria","marca","costo_unitario","precio_lista"], productos),
 insert("cliente", ["nombre","segmento","fecha_registro","ciudad"], clientes),
 insert("canal_venta", ["nombre"], canales),
 insert("metodo_pago", ["nombre"], metodos),
 insert("promocion", ["nombre","tipo_descuento","fecha_inicio","fecha_fin","alcance","id_producto_alcance","categoria_alcance"], promociones),
 insert("venta", ["fecha","id_sucursal","id_cliente","id_canal","id_metodo_pago","total"], ventas),
 insert("detalle_venta", ["id_venta","id_producto","cantidad","precio_unitario","descuento","id_promocion"], detalles),
 insert("movimiento_inventario", ["fecha","id_sucursal","id_producto","tipo_movimiento","cantidad"], movimientos),
 insert("inventario", ["fecha","id_sucursal","id_producto","stock_actual","stock_minimo"], inventarios),
]
open("datos_supermercado.sql","w",encoding="utf-8").write("\n".join(sql))

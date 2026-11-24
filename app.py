# NLYTREND - TU ESTILO, TU TENDENCIA
# CRUD + PEDIDO + STOCK AUTOMATIZADO - EN VISUAL STUDIO CODE

inventario = [
    {"id": 1, "categoria": "Blusas de dama", "emoji": "👚", "talla": "M", "color": "Blanco", "precio": 35000, "cantidad": 5},
    {"id": 2, "categoria": "Vestidos", "emoji": "👗", "talla": "S", "color": "Negro", "precio": 55000, "cantidad": 3},
    {"id": 3, "categoria": "Jean de dama", "emoji": "👖", "talla": "28", "color": "Azul", "precio": 60000, "cantidad": 4},
    {"id": 4, "categoria": "Jean de caballero", "emoji": "👖", "talla": "32", "color": "Azul", "precio": 65000, "cantidad": 4},
    {"id": 5, "categoria": "Bermudas", "emoji": "🩳", "talla": "6", "color": "Azul", "precio": 30000, "cantidad": 6},
    {"id": 6, "categoria": "Conjuntos de niños", "emoji": "🧒", "talla": "4", "color": "Verde", "precio": 45000, "cantidad": 3},
    {"id": 7, "categoria": "Conjuntos de niñas", "emoji": "👧", "talla": "4", "color": "Rosado", "precio": 45000, "cantidad": 3},
    {"id": 8, "categoria": "Camiseta de caballero", "emoji": "👕", "talla": "L", "color": "Negro", "precio": 50000, "cantidad": 2},
    {"id": 9, "categoria": "Conjuntos de caballeros", "emoji": "👔", "talla": "L", "color": "Azul", "precio": 70000, "cantidad": 2},
    {"id": 10, "categoria": "Blusas de niña", "emoji": "👚", "talla": "8", "color": "Blanco", "precio": 25000, "cantidad": 5},
    {"id": 11, "categoria": "Short de niña", "emoji": "🩳", "talla": "8", "color": "Azul", "precio": 28000, "cantidad": 4},
    {"id": 12, "categoria": "Jean de niña", "emoji": "👖", "talla": "8", "color": "Azul", "precio": 40000, "cantidad": 4},
]

def leer():
    print("\n🖤✨ NLYTREND - TU ESTILO, TU TENDENCIA ✨🖤")
    print("ID | Prenda | Categoria | Talla | Color | Precio | Cant")
    print("------------------------------------------------------")
    for p in inventario:
        print(f"{p['id']} | {p['emoji']} | {p['categoria']} | {p['talla']} | {p['color']} | ${p['precio']} | {p['cantidad']}")
    print("------------------------------------------------------")
    input("presiona enter para volver...")

def crear():
    print("\n--- CREAR ---")
    cat = input("Categoria: ")
    talla = input("Talla: ")
    color = input("Color: ")
    precio = int(input("Precio: "))
    cant = int(input("Cantidad: "))
    nuevo_id = max([x["id"] for x in inventario]) + 1 if inventario else 1
    inventario.append({"id": nuevo_id, "categoria": cat, "emoji": "✨", "talla": talla, "color": color, "precio": precio, "cantidad": cant})
    print("✅ Creado!")
    automatizar_stock()

def actualizar():
    leer()
    id_buscar = int(input("¿Que ID quieres EDITAR? "))
    for p in inventario:
        if p["id"] == id_buscar:
            p["precio"] = int(input(f"Nuevo precio (antes {p['precio']}): "))
            p["cantidad"] = int(input(f"Nueva cantidad (antes {p['cantidad']}): "))
            print("✅ Editado!")
            automatizar_stock()
            return
    print("❌ No existe ese ID")

def eliminar():
    leer()
    id_buscar = int(input("¿Que ID quieres BORRAR? "))
    for p in inventario:
        if p["id"] == id_buscar:
            inventario.remove(p)
            print("🗑️ Borrado!")
            return
    print("❌ No existe ese ID")

def automatizar_stock():
    print("\n🤖 AUTOMATIZANDO STOCK...")
    for p in inventario[:]:
        if p["cantidad"] == 0:
            print(f"⚠️ Se acabo {p['categoria']}, se elimino SOLITO!")
            inventario.remove(p)
        elif p["cantidad"] <= 2:
            print(f"⚠️ OJO! Quedan pocos de {p['categoria']}: solo {p['cantidad']}")
    print("✅ Stock actualizado solito!")
    leer()

def pedir():
    print("\n🛒 --- HACER PEDIDO NLYTREND ---")
    leer()
    id_buscar = int(input("¿Que ID quieres pedir? "))
    cant_pedir = int(input("¿Cuantos quieres pedir? "))
    for p in inventario:
        if p["id"] == id_buscar:
            if cant_pedir > p["cantidad"]:
                print(f"❌ No hay suficientes, solo quedan {p['cantidad']}")
                return
            total = cant_pedir * p["precio"]
            p["cantidad"] = p["cantidad"] - cant_pedir
            print(f"✅ Pedido listo! {cant_pedir} x {p['categoria']} = ${total}")
            print(f"👉 Antes tenias mas, ahora te quedan: {p['cantidad']}")
            automatizar_stock()
            return
    print("❌ No existe ese ID")

while True:
    print("\n===== MENU NLYTREND =====")
    print("1. Ver catalogo (Leer)")
    print("2. Crear")
    print("3. Editar (Actualizar)")
    print("4. Borrar (Eliminar)")
    print("5. Hacer Pedido (Automatizar Stock)")
    print("6. Salir")
    opcion = input("Elige una opcion (1-6): ")
    if opcion == "1":
        leer()
    elif opcion == "2":
        crear()
    elif opcion == "3":
        actualizar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        pedir()
    elif opcion == "6":
        print("Gracias por comprar en NLYTREND! 🖤")
        break
    else:
        print("Opcion no valida, intenta de nuevo")
        
        
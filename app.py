import streamlit as st

# NLYTREND - TU ESTILO, TU TENDENCIA
# CRUD + PEDIDO + STOCK AUTOMATIZADO - EN STREAMLIT

if "inventario" not in st.session_state:
    st.session_state.inventario = [
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

inventario = st.session_state.inventario

def automatizar_stock():
    st.write("🤖 AUTOMATIZANDO STOCK...")
    for p in inventario[:]:
        if p["cantidad"] == 0:
            st.warning(f"⚠️ Se acabo {p['categoria']}, se elimino SOLITO!")
            inventario.remove(p)
        elif p["cantidad"] <= 2:
            st.warning(f"⚠️ OJO! Quedan pocos de {p['categoria']}: solo {p['cantidad']}")
    st.success("✅ Stock actualizado solito!")

def leer():
    st.subheader("🖤✨ NLYTREND - TU ESTILO, TU TENDENCIA ✨🖤")
    st.table(inventario)

st.title("🖤✨ NLYTREND - TU ESTILO, TU TENDENCIA ✨🖤")

opcion = st.sidebar.radio("===== MENU NLYTREND =====",
    ["1. Ver catalogo (Leer)", "2. Crear", "3. Editar (Actualizar)", "4. Borrar (Eliminar)", "5. Hacer Pedido (Automatizar Stock)", "6. Salir"])

if opcion == "1. Ver catalogo (Leer)":
    leer()

elif opcion == "2. Crear":
    st.header("--- CREAR ---")
    cat = st.text_input("Categoria:")
    talla = st.text_input("Talla:")
    color = st.text_input("Color:")
    precio = st.number_input("Precio:", min_value=0, step=1000)
    cant = st.number_input("Cantidad:", min_value=0, step=1)
    if st.button("Crear"):
        nuevo_id = max([x["id"] for x in inventario]) + 1 if inventario else 1
        inventario.append({"id": nuevo_id, "categoria": cat, "emoji": "✨", "talla": talla, "color": color, "precio": precio, "cantidad": cant})
        st.success("✅ Creado!")
        automatizar_stock()
        leer()

elif opcion == "3. Editar (Actualizar)":
    st.header("--- EDITAR ---")
    leer()
    id_buscar = st.number_input("¿Que ID quieres EDITAR?", min_value=1, step=1)
    if st.button("Buscar para editar"):
        for p in inventario:
            if p["id"] == id_buscar:
                st.session_state.editar_id = id_buscar
                break
        else:
            st.error("❌ No existe ese ID")
    if "editar_id" in st.session_state:
        for p in inventario:
            if p["id"] == st.session_state.editar_id:
                nuevo_precio = st.number_input(f"Nuevo precio (antes {p['precio']}):", min_value=0, value=p["precio"])
                nueva_cant = st.number_input(f"Nueva cantidad (antes {p['cantidad']}):", min_value=0, value=p["cantidad"])
                if st.button("Guardar cambios"):
                    p["precio"] = nuevo_precio
                    p["cantidad"] = nueva_cant
                    st.success("✅ Editado!")
                    automatizar_stock()
                    del st.session_state.editar_id

elif opcion == "4. Borrar (Eliminar)":
    st.header("--- BORRAR ---")
    leer()
    id_buscar = st.number_input("¿Que ID quieres BORRAR?", min_value=1, step=1)
    if st.button("Borrar"):
        for p in inventario:
            if p["id"] == id_buscar:
                inventario.remove(p)
                st.success("🗑️ Borrado!")
                break
        else:
            st.error("❌ No existe ese ID")

elif opcion == "5. Hacer Pedido (Automatizar Stock)":
    st.header("🛒 --- HACER PEDIDO NLYTREND ---")
    leer()
    id_buscar = st.number_input("¿Que ID quieres pedir?", min_value=1, step=1)
    cant_pedir = st.number_input("¿Cuantos quieres pedir?", min_value=1, step=1)
    if st.button("Hacer Pedido"):
        for p in inventario:
            if p["id"] == id_buscar:
                if cant_pedir > p["cantidad"]:
                    st.error(f"❌ No hay suficientes, solo quedan {p['cantidad']}")
                    break
                total = cant_pedir * p["precio"]
                p["cantidad"] = p["cantidad"] - cant_pedir
                st.success(f"✅ Pedido listo! {cant_pedir} x {p['categoria']} = ${total}")
                st.write(f"👉 Antes tenias mas, ahora te quedan: {p['cantidad']}")
                automatizar_stock()
                break
        else:
            st.error("❌ No existe ese ID")

elif opcion == "6. Salir":
    st.write("Gracias por comprar en NLYTREND! 🖤")
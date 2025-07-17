from sqlalchemy.orm import Session
from typing import List
from ..models import listado_rutas_destino
from ..schemas.ruta import RutaCreate

def create_ruta(db: Session, ruta: RutaCreate):
    # Crear la ruta principal
    db_ruta = listado_rutas_destino.ListadoRutas(
        destino_id=ruta.destino_id,
        img=ruta.img,
        nombre=ruta.nombre,
        calificacion=ruta.calificacion,
        dificultad=ruta.dificultad,
        tiempo=ruta.tiempo,
        terreno=ruta.terreno,
        distancia=ruta.distancia,
        descripcion=ruta.descripcion,
        etiquetas=ruta.etiquetas,
        veces_recomendada=ruta.veces_recomendada,
        completaron_ruta=ruta.completaron_ruta,
        items=ruta.items
    )
    db.add(db_ruta)
    db.flush()  # Para obtener el ID de la ruta creada

    # Crear categoría
    db_categoria = listado_rutas_destino.Categorias(
        ruta_id=db_ruta.id,  # Asignar el ID de la ruta
        senderismo=ruta.categoria.senderismo,
        bici_tour=ruta.categoria.bici_tour,
        moto=ruta.categoria.moto,
        automovil=ruta.categoria.automovil
    )
    db.add(db_categoria)

    # Crear instrucciones
    db_instrucciones = listado_rutas_destino.Instrucciones(
        ruta_id=db_ruta.id,  # Asignar el ID de la ruta
        recomendaciones=ruta.instrucciones.recomendaciones,
        accesibilidad=ruta.instrucciones.accesibilidad,
        conservacion=ruta.instrucciones.conservacion
    )
    db.add(db_instrucciones)

    # Crear imágenes
    for imagen in ruta.imagenes:
        db_imagen = listado_rutas_destino.Imagenes(
            ruta_id=db_ruta.id,
            url=imagen.url
        )
        db.add(db_imagen)

    # Crear estaciones
    for estacion in ruta.estaciones:
        db_estacion = listado_rutas_destino.Estaciones(
            ruta_id=db_ruta.id,  # Asignar el ID de la ruta
            nombre=estacion.nombre,
            dificultad=estacion.dificultad,
            lat=estacion.lat,
            lng=estacion.lng,
            img=estacion.img,
            description=estacion.description,
            numero_estacion=estacion.numero_estacion
        )
        db.add(db_estacion)

    # Crear coordenadas principales
    db_coordenadas = listado_rutas_destino.CoordenadasPrincipales(
        ruta_id=db_ruta.id,
        cordenadas=ruta.coordenadas_principales.cordenadas
    )
    db.add(db_coordenadas)

    db.commit()
    db.refresh(db_ruta)
    return db_ruta
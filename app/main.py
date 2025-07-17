from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Importaciones de los routers
from .api.v1.endpoints import destino
from .api.v1.endpoints import restaurante_details
from .api.v1.endpoints import bar_details
from .api.v1.endpoints import actividad_details
from .api.v1.endpoints import evento_details
from .api.v1.endpoints import alojamiento_details
from .api.v1.endpoints import listado_rutas
from .api.v1.endpoints import descripcion_ruta
from .api.v1.endpoints import coordenada_ruta
from .api.v1.endpoints import ruta

from .api.v1.endpoints import registrarVendor
from .api.v1.endpoints import registerUser

from .api.v1.endpoints.dashboardEstablecimientos import restauranteBar
from .api.v1.endpoints.dashboardEstablecimientos import actividades
from .api.v1.endpoints.dashboardEstablecimientos import alojamientos

from .api.v1.endpoints.envioFormulario import restaurantes
from .api.v1.endpoints.envioFormulario import bares
from .api.v1.endpoints.envioFormulario import actividadesForm
from .api.v1.endpoints.envioFormulario import alojamientosForm

from .api.v1.endpoints.dashboardEdit import restauranteUpdate
from .api.v1.endpoints.dashboardEdit import baresUpdate
from .api.v1.endpoints.dashboardEdit import actividadUpdate
from .api.v1.endpoints.dashboardEdit import alojamientosUpdate
from .api.v1.endpoints.dashboardEdit import bloquearFechas

from .api.v1.endpoints import destinosFiltros

from .api.v1.endpoints import listadoBaresRestaurantes
from .api.v1.endpoints import listadoDemasEstablecimientos

from .api.v1.endpoints import comentarios_rutas
from .api.v1.endpoints import contador_arboles_basico
from .api.v1.endpoints import seccion_impacto_ambiental

from .api.v1.endpoints import batalla_burger

from .api.v1.endpoints import listadoBlogs
from .api.v1.endpoints import blogIndividual

from .api.v1.endpoints import learning_daily
from .api.v1.endpoints import listadoArticulosAndresPage
from .api.v1.endpoints import articuloIndividualAndresPage
from .api.v1.endpoints import listadoProyectosAndresPage
from .api.v1.endpoints import projects
from .api.v1.endpoints import comentariosAndresPage

from .core.config import settings
from .db.session import engine, Base


# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar FastAPI
app = FastAPI(
    title="API Turismo Local",
    description="API para el MVP de la aplicación de turismo local",
    version="1.0.0"
)

# Configuración más específica de CORS
origins = [
    "http://localhost:3000",
    "http://192.168.1.34:3000",  # Tu URL de desarrollo
    "https://tree-suesca.vercel.app",
    "https://new-vendor.vercel.app",
    "https://tree-suesca.vercel.app",
    "https://new-route-nine.vercel.app"
]

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Temporalmente para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

# Prefix para todas las rutas de la API
API_V1_PREFIX = "/api/v1"

app.include_router(
    comentariosAndresPage.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["Comentarios"]
)

app.include_router(
    projects.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/project"]
)

app.include_router(
    listadoProyectosAndresPage.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/previews/projects"]
)

app.include_router(
    articuloIndividualAndresPage.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/blog"]
)

app.include_router(
    listadoArticulosAndresPage.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/previews/andres/page"]
)

app.include_router(
    learning_daily.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/questions/answers/fun/facts"]
)

app.include_router(
    blogIndividual.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/blog"]
)


app.include_router(
    listadoBlogs.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/preview"]
)


app.include_router(
    batalla_burger.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/votes"]
)

# Incluir los routers
app.include_router(
    destino.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["destinos"]
)
app.include_router(
    restaurante_details.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["restaurante"]
)
app.include_router(
    bar_details.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["bar"]
)
app.include_router(
    actividad_details.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["actividad"]
)
app.include_router(
    evento_details.router,
    prefix=f"{API_V1_PREFIX}",
    tags = ["evento"]
)
app.include_router(
    alojamiento_details.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["alojamiento"]
)
app.include_router(
    listado_rutas.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["rutas"]
)
app.include_router(
    descripcion_ruta.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["caracteristicas"]
)
app.include_router(
    coordenada_ruta.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["mapa"]
)
app.include_router(
    ruta.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["new"]
)
app.include_router(
    registrarVendor.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/type/register"]
)
app.include_router(
    registerUser.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/register"]
)
app.include_router(
    restauranteBar.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/dashboard"]
)
app.include_router(
    actividades.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["actividad/dashboard"]
)
app.include_router(
    alojamientos.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/dashboard/aloja"]
)
app.include_router(
    restaurantes.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/restaurantes/register"]
)
app.include_router(
    restauranteUpdate.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/restaurantes/update"]
)
app.include_router(
    bares.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/bares/register"]
)
app.include_router(
    baresUpdate.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/bares/update"]
)
app.include_router(
    actividadesForm.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/actividades/register"]
)
app.include_router(
    actividadUpdate.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/act/update"]
)
app.include_router(
    alojamientosForm.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/alojamientos/register"]
)
app.include_router(
    alojamientosUpdate.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/aloja/update"]
)
app.include_router(
    destinosFiltros.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/destinos/filtros"]
)
app.include_router(
    listadoBaresRestaurantes.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/listados"]
)
app.include_router(
    listadoDemasEstablecimientos.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/listados/demas"]
)
app.include_router(
    bloquearFechas.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/fechas-bloqueadas"]
)
app.include_router(
    comentarios_rutas.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/ruta/comentarios"]
)

app.include_router(
    contador_arboles_basico.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/contador/arboles"]
)

app.include_router(
    seccion_impacto_ambiental.router,
    prefix=f"{API_V1_PREFIX}",
    tags=["/arboles-info"]
)


# Ruta de verificación de salud de la API
@app.get("/", tags=["health"])
async def health_check():
    return JSONResponse(
        content={
            "status": "ok",
            "message": "API funcionando correctamente"
        }
    )

# Manejador de errores global
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    import traceback
    error_trace = traceback.format_exc()
    
    print(f"Error detallado: {error_trace}")  # Para ver el error en los logs
    
    return JSONResponse(
        status_code=500,
        content={
            "message": "Error interno del servidor",
            "detail": str(exc),
            "trace": error_trace if app.debug else None  # Solo en desarrollo
        }
    )

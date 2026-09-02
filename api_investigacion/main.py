"""
main.py — El arranque de la API del módulo Investigación.

Arma la aplicación y registra el router. Nada más: la lógica vive en las
capas, no aquí.

Arranque:  uvicorn main:app --port 8025 --reload
Contratos: http://localhost:8025/docs
"""

from fastapi import FastAPI

from controllers.area_conocimiento_controller import router as router_area

app = FastAPI(
    title="API Investigación",
    description="Módulo de Investigación — versión 1: el catálogo de "
                "áreas de conocimiento.",
    version="v1",
)

app.include_router(router_area)


@app.get("/")
async def diagnostico():
    """Responde sin tocar la base: sirve para saber si la API está viva."""
    return {"mensaje": "API Investigación — módulo de áreas de conocimiento",
            "version": "v1", "contratos": "/docs"}

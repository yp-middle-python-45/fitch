from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette_exporter import PrometheusMiddleware, handle_metrics

from src.api.main import api_router
from src.core.config import settings


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

app.include_router(api_router, prefix=settings.API_V1_STR)

app.add_middleware(
    PrometheusMiddleware,
    app_name=settings.PROJECT_NAME,
    prefix="fastapi",
    labels={
        "env": settings.ENVIRONMENT,
    },
    skip_paths=["/health", "/version", "/metrics"],
    skip_methods=["OPTIONS"],
)
app.add_route("/metrics", handle_metrics)

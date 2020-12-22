from fastapi import FastAPI

from app.apis.casts import casts
from app.databases.casts import engine, metadata, database

metadata.create_all(engine)

app = FastAPI(
    openapi_url="/api/v1/casts/openapi.json", docs_url="/api/v1/casts/docs"
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(casts, prefix="/api/v1/casts", tags=["casts"])

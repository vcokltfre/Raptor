from hmac import compare_digest
from os import environ

from fastapi import FastAPI, Request, Response

from .db.tortoise import init as db_init
from .routes import router

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
async def on_start() -> None:
    await db_init()


@app.middleware("http")
async def auth_middleware(req: Request, nxt) -> Response:
    if not compare_digest(
        req.headers.get("Authorization", ""), environ["MAIN_API_KEY"]
    ):
        return Response("Invalid authentication.", status_code=401)

    return await nxt(req)

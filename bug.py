import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine

from starlette.applications import Starlette
from starlette.testclient import TestClient
from starlette.routing import Route
from starlette.responses import JSONResponse


engine = create_async_engine('postgresql+asyncpg://postgres:postgres@localhost/postgres')
engine2 = sa.create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')

async def run(*args, **kwargs):
    print('start')
    async with engine.begin() as conn:
        result = await conn.execute(sa.text("select 1"))
        records = dict(result.mappings().first())

    print(records)
    return JSONResponse(records)

def run2(*args, **kwargs):
    print('start')
    with engine2.begin() as conn:
        result = conn.execute(sa.text("select 1"))
        records = dict(result.mappings().first())

    print(records)
    return JSONResponse(records)


app = Starlette(debug=True, routes=[
    Route('/run', run),
    Route('/run2', run2),
])

def test_run():
    client = TestClient(app)
    client.get('/run')
    client.get('/run2')


if __name__ == "__main__":
    test_run()

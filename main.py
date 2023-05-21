from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# url指定、変数受け取る時これ
@app.get("/items/{item_id}")
async def read_item(item_id: int):  # ? asyncつく理由
    return {"item_id": item_id}  # JSON

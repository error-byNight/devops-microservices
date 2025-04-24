from fastapi import FastAPI
app = FastAPI()

@app.get("/products")
def get_products():
    return [{"id": 101, "name": "Laptop"}]
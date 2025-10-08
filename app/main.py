from fastapi import FastAPI

app = FastAPI()

def add(a: int, b: int) -> int:
    """Simple function to add two integers (covered by tests)."""
    return a + b

@app.get("/")
def read_root():
    return {"message": "Hello from CI/CD demo"}

@app.get("/add")
def read_add(a: int, b: int):
    return {"result": add(a, b)}

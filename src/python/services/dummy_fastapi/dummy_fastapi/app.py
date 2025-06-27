from fastapi import FastAPI

app = FastAPI(
    title="Dummy FastAPI Service",
    description="A minimal FastAPI application",
    version="1.0.0",
)


@app.get("/")  # type: ignore[misc]
async def root() -> str:
    """Root endpoint"""
    return "Hello from Dummy FastAPI Service!"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

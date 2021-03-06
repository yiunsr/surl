import uvicorn

from config import create_app  # pylint: disable=no-name-in-module
app = create_app()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8018)

from fastapi import FastAPI

app = FastAPI(title="Project API")

 

@app.get("/health")
def health():
    return {"status": "healthy"}

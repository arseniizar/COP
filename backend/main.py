from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import analysis

app = FastAPI(title="Code Observability Platform API")

origins = [
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis.router, prefix="/api/v1", tags=["Analysis"])

@app.get("/")
def read_root():
    return {"message": "API is running. Go to /docs for documentation."}

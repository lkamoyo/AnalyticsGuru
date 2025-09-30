from fastapi import FastAPI
from routers import data, insights, dashboard, export
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data.router)
app.include_router(insights.router)
app.include_router(dashboard.router)
app.include_router(export.router)
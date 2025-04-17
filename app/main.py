print("Hello from main!")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import sms
import uvicorn

app = FastAPI(
    title="SMS Gateway API",
    description="API pour envoyer et recevoir des SMS via un module GSM",
    version="1.0.0"
)

# Configuration CORS pour permettre les requêtes cross-origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pour la production, limitez aux origines spécifiques
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(sms.router, tags=["SMS"])

@app.get("/", tags=["Status"])
async def root():
    """Vérifier que l'API est en ligne"""
    return {"status": "online", "message": "SMS Gateway API is running"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
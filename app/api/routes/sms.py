# app/api/routes/sms.py
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.models.sms import SmsCreate, SmsResponse, SmsInboxResponse
from app.services.gsm_service import GSMService
from app.core.auth import get_current_user
from app.services.storage import StorageService
from app.models.user import UserInDB

router = APIRouter()
storage_service = StorageService()
gsm_service = GSMService(storage_service)

@router.post("/sms", response_model=SmsResponse, summary="Envoyer un SMS")
async def send_sms(
    sms: SmsCreate,
    current_user: UserInDB = Depends(get_current_user)
):
    """
    Envoie un SMS au numéro spécifié.
   
    - **phone_number**: Numéro complet avec indicatif international
    - **message**: Contenu du SMS à envoyer
    """
    try:
        result = await gsm_service.send_sms(sms)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'envoi du SMS: {str(e)}")

@router.get("/sms/inbox", response_model=List[SmsResponse], summary="Lister tous les SMS reçus")
async def get_inbox(
    limit: Optional[int] = Query(50, description="Nombre maximum de SMS à retourner"),
    current_user: UserInDB = Depends(get_current_user)
):
    """
    Récupère tous les SMS reçus.
    """
    try:
        inbox = await gsm_service.get_inbox()
        return inbox[:limit]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des SMS: {str(e)}")
@router.get("/sms/sent", response_model=List[SmsResponse], summary="Lister tous les SMS envoyés")
async def get_sent_messages(
    limit: Optional[int] = Query(50, description="Nombre maximum de SMS à retourner"),
    current_user: UserInDB = Depends(get_current_user)
):
    """
    Récupère tous les SMS envoyés (sortants).
    """
    try:
        sent_messages = await storage_service.get_sent_messages()
        return sent_messages[:limit]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des SMS envoyés: {str(e)}")

@router.get("/logs", response_model=List[dict], summary="Voir les logs des SMS")
async def get_logs(
    limit: Optional[int] = Query(100, description="Nombre maximum de logs à retourner"),
    level: Optional[str] = Query(None, description="Filtre par niveau de log (INFO, WARNING, ERROR, etc.)"),
    component: Optional[str] = Query(None, description="Filtre par composant"),
    current_user: UserInDB = Depends(get_current_user)
):
    """
    Récupère l'historique et le statut de tous les SMS envoyés.
    """
    try:
        logs = await storage_service.get_logs(limit=limit)
        
        # Basic in-memory filtering
        if level:
            logs = [log for log in logs if log["level"] == level.upper()]
        if component:
            logs = [log for log in logs if log["component"] == component.upper()]
            
        return logs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des logs: {str(e)}")
@router.post("/sms/simulate-receive", response_model=SmsResponse)
async def simulate_received_sms(
    phone_number: str = Query(..., description="Numéro de téléphone de l'expéditeur"),
    message: str = Query(..., description="Contenu du message reçu"),
    current_user: UserInDB = Depends(get_current_user)
):
    """
    Simule la réception d'un SMS (uniquement pour les tests/développement).
    """
    try:
        result = await gsm_service.simulate_received_sms(phone_number, message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la simulation: {str(e)}")
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.sms import SmsCreate, SmsResponse
from app.services.gsm_service import GSMService
from app.core.security import get_api_key

router = APIRouter()
gsm_service = GSMService()

@router.post("/sms", response_model=SmsResponse, summary="Envoyer un SMS")
async def send_sms(
    sms: SmsCreate,
    api_key: str = Depends(get_api_key)
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
    api_key: str = Depends(get_api_key)
):
    """
    Récupère tous les SMS reçus.
    """
    try:
        inbox = await gsm_service.get_inbox()
        return inbox
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des SMS: {str(e)}")

@router.get("/logs", response_model=List[SmsResponse], summary="Voir les logs des SMS")
async def get_logs(
    api_key: str = Depends(get_api_key)
):
    """
    Récupère l'historique et le statut de tous les SMS envoyés.
    """
    try:
        logs = await gsm_service.get_sent_messages()
        return logs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des logs: {str(e)}")
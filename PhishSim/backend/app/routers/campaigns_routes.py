from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(prefix="/api/campaigns", tags=["campaigns"])

@router.post("", response_model=schemas.CampaignOut)
def create_campaign(data: schemas.CampaignCreate, db: Session = Depends(get_db), user=Depends(auth.get_current_user)):
    tpl = db.query(models.Template).get(data.template_id)
    if not tpl:
        raise HTTPException(status_code=404, detail="Template not found")
    if db.query(models.Campaign).filter(models.Campaign.name == data.name).first():
        raise HTTPException(status_code=400, detail="Campaign already exists")
    c = models.Campaign(name=data.name, template_id=data.template_id)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c

@router.get("", response_model=List[schemas.CampaignOut])
def list_campaigns(db: Session = Depends(get_db), user=Depends(auth.get_current_user)):
    return db.query(models.Campaign).all()

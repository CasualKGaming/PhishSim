from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(prefix="/api/templates", tags=["templates"])

@router.post("", response_model=schemas.TemplateOut)
def create_template(data: schemas.TemplateCreate, db: Session = Depends(get_db), user=Depends(auth.get_current_user)):
    if db.query(models.Template).filter(models.Template.name == data.name).first():
        raise HTTPException(status_code=400, detail="Template already exists")
    t = models.Template(**data.dict())
    db.add(t)
    db.commit()
    db.refresh(t)
    return t

@router.get("", response_model=List[schemas.TemplateOut])
def list_templates(db: Session = Depends(get_db), user=Depends(auth.get_current_user)):
    return db.query(models.Template).all()

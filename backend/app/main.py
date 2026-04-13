from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from . import crud,models,schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Manager API")

@app.get("/categories/", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@app.get("/categories/{category_id}/total")
def get_category_total(category_id: int, db: Session = Depends(get_db)):
    total = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.category_id == category_id).scalar()

    return {"category_id": category_id, "total": total or 0}

@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db:Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)
@app.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    result = crud.delete_category(db, category_id=category_id)
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"status": "success", "message": f"Category {category_id} deleted"}

@app.get("/transactions/", response_model=List[schemas.Transaction])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_transactions(db, skip=skip, limit=limit)

@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transaction=transaction)

@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    result = crud.delete_transaction(db, transaction_id=transaction_id)
    if not result:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"status": "success", "message": f"Transaction {transaction_id} deleted"}

@app.get("/")
def root():
    return {"message": "Finance Manager API is runningfafea"}
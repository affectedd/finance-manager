from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True,index=True, nullable=False)

    transactions = relationship("Transaction", back_populates="category_owner", cascade="all, delete-orphan")


class Transaction(Base):
    __tablename__="transactions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))

    category_owner = relationship("Category", back_populates="transactions")

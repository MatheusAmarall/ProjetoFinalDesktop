from infra.configs.base import Base
from sqlalchemy import Column, String, Integer

class Pedido(Base):
    __tablename__ = 'pedido'

    id = Column(Integer, unique=True, primary_key=True)
    numero = Column(String(255), nullable=False)
    cliente = Column(String(100), nullable=False)
    data = Column(String(100), nullable=False)
    
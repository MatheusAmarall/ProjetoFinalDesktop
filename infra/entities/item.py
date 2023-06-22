from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, unique=True, primary_key=True)
    descricao = Column(String(100), nullable=False)
    quantidade = Column(Integer, nullable=False)
    id_pedido = Column(Integer, ForeignKey('pedido.id'), nullable=False)
    
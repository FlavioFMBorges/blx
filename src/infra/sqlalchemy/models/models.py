from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlachemy.config.database import Base

class Produto():

    id = Column(Integer, primary_key=True, index=True)
    nome =  Column(String)
    descricao = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)


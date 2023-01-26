from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models



class RepositorioProduto():

    def __init__(self, db: Session):  #parametro db do tipo Session
        self.db = db   #o segundo db é o parametro que chega e o primeiro e o que fica disponivel por toda a minha classe

    def criar(self, produto: schemas.Produto):
        db_produto =

    def listar(self):
        pass

    def obter(self):
        pass

    def remover(self):
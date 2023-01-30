from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models



class RepositorioProduto():

    def __init__(self, db: Session):  #parametro db do tipo Session
        self.db = db   #o segundo db é o parametro que chega e o primeiro e o que fica disponivel por toda a minha classe

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome=produto.nome,
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.preco)  #transformando schemas em modelos
        self.db.add(db_produto) #bd, adicione esse produto ai
        self.db.commit() #depois que vc gravar pode confirmar essa operacao
        self.db.refresh(db_produto)
        return db_produto #retorno para quem me pediu para criar

    def listar(self):
        produtos = self.db.query(models.Produto).all
        return produtos

    def obter(self):
        pass

    def remover(self):
        pass
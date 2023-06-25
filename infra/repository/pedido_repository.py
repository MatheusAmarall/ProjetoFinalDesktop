from infra.configs.connection import DBConnectionHandler
from infra.entities.pedido import Pedido

class PedidoRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Pedido).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Pedido).filter(Pedido.id == id).first()
            return data

    def insert(self, pedido:Pedido):
        with DBConnectionHandler() as db:
            try:
                db.session.add(pedido)
                db.session.commit()
                db.session.refresh(pedido)
                return pedido.id
            except Exception as e:
                db.session.rollback()
                return e

    def delete(self, id):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Pedido).filter(Pedido.id == id).delete()
                db.session.commit()
                return "OK"
            except Exception as e:
                db.session.rollback()
                return e

    def update(self, pedido=Pedido):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Pedido).filter(Pedido.id == pedido.id).update({
                Pedido.cliente: pedido.cliente
            })
                db.session.commit()

                return "OK"
            except Exception as e:
                db.session.rollback()
                return e


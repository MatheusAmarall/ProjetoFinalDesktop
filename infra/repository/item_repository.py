from infra.configs.connection import DBConnectionHandler
from infra.entities.item import Item

class ItemRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Item).all()
            return data

    def select(self, pedido_id):
        with DBConnectionHandler() as db:
            data = db.session.query(Item).filter(Item.id_pedido == pedido_id).first()
            return data

    def insert(self, item):
        with DBConnectionHandler() as db:
            try:
                db.session.add(item)
                db.session.commit()
                return "OK"
            except Exception as e:
                db.session.rollback()
                return e

    def delete(self, id):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Item).filter(Item.id == id).delete()
                db.session.commit()
                return "OK"
            except Exception as e:
                db.session.rollback()
                return e

    def update(self, item=Item):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Item).filter(Item.id == item.id).update({
                    Item.descricao: item.descricao,
                    Item.quantidade: item.quantidade
                })
                db.session.commit()

                return "OK"
            except Exception as e:
                db.session.rollback()
                return e


from app.base.services import BaseService


class OrderBuyer(BaseService):
    def __init__(self, order):
        self.order = order

    def act(self):
        self.set_order_status()
        self.order.save()
        return self.order

    def set_order_status(self):
        self.order.status = 'BOUGHT'

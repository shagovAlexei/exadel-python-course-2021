

class Good:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    def __str__(self):
        return f"product_id: {self.product_id}\tname: {self.name}\tprice: {self.price}"

class Order:
    def __init__(self, order_id, order_date, client_id):
        self.order_id = order_id
        self.order_date = order_date
        self.client_id = client_id
        self._price = None
        self._goods = []

class OrderRepository:
    order: Order = None
    order_id: int = None
    latest: int = None


good1 = Good("123", "mouse", 34)
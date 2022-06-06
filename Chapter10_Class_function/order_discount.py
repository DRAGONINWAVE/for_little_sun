from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional,Callable,NamedTuple

# import Dec as Dec
# import item as item
# from pint import quantity


class Customer(NamedTuple):
    name:str
    fidelity:int

class LineItem(NamedTuple):
    product:str
    quantity:int
    price:Decimal

    def total(self):
        return self.price * self.quantity

@dataclass(frozen=True)
class Order : # the Context
    customer:Customer
    cart:Sequence[LineItem]
    promotion:Optional[Callable[['Order'],Decimal]] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals,start=Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f'<ORder total :{self.total():.2f} due:' \
               f'{self.due():.2f}'

def fidelity_promo(order:Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity points"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)

def bulk_item_promo(order:Order) -> Decimal:
    """10% discount for each LineItem with 20 or more units"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount

def large_order_promo(order:Order) -> Decimal:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items  = {item.product for item in order.cart}

    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)
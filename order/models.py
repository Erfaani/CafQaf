from django.db import models
from product.models import Product, Table
from account.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    table = models.ForeignKey(Table, null=True, on_delete=models.SET_NULL)
    canceled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self) -> int:
        return sum(item.total_price for item in self.orderitem_set.all())


    def __str__(self) -> str:
        return str(self.user.username) + ' : ' + str(self.id)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_price(self) -> int:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return str(self.id)
    
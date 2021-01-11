from django.db import models
from .products import Product
from .customer import Customer
import datetime

class Order(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    Product = models.ForeignKey('Product', on_delete=models.CASCADE)
    Customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    Quantity = models.BigIntegerField(default=1)
    Price = models.BigIntegerField(null=True)
    Phone = models.BigIntegerField(default=0)
    Address = models.CharField(max_length=100, default='')
    Arrival_Date = models.DateField(default=datetime.datetime.now())
    Order_Date = models.DateField(default=datetime.datetime.now())
    Status = models.BooleanField(default = False)

    def place_order(self):
        self.save()

    def get_customer_by_id(customer_id):
        #return Order.objects.filter(Customer = customer_id)
        sql = (''' select * from store_order where "Customer_id"=%s ''')
        return Order.objects.raw(sql, [customer_id])